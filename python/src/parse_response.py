import pickle


def parse_response(response):
    """
    For each excerpt, the response returns the transcript, a confidence level
    (or multiple alternative transcripts and their respective confidence
    levels), and the start and end time of each word in the transcript. This
    parses out just the most confident transcript and the start time of its
    first word (in seconds).
    """
    transcription = []
    for ii, result in enumerate(response.results):
        start_time = result.alternatives[0].words[0].start_time
        excerpt = {'transcript': result.alternatives[0].transcript,
                  'time':       start_time.seconds + start_time.nanos * 1e-9}
        transcription.append(excerpt)
    return transcription


def save_file_as_tsv(transcript, filepath):
    """
    Pickle the transcription response to a file with the same name.
    ---
    Args:
        response:   (google.cloud.speech_v1.types.LongRunningRecognizeResponse)
                    The output of the Google speech API
        filepath:   (str) The filepath to the audio recording, not the filepath
                    to save under. That is created here.
    """
    filename = filepath.split('/')[-1]
    filename = filename.split('.')[0]
    filepath = f'../transcriptions/{filename}_transcription.tsv'

    with open(filepath, 'w') as outfile:
        for excerpt in transcript:
            outfile.write(f"{excerpt['time']}\t{excerpt['transcript']}\n")
    print(f'Saved transcript to {filepath}.')


def save_file_as_pickle(response, filepath):
    filename = filepath.split('/')[-1]
    filename = filename.split('.')[0]
    filepath = f'../transcriptions/{filename}_speech_to_text_object.pkl'

    with open(filepath, 'wb') as pkl_file:
        pickle.dump(response, pkl_file)
    print(f'Pickled API output to {filepath}.')


def parse_and_save_file(response, filepath):
    if not isinstance(response, str):
        # When transcription fails it simply returns the gcs_uri as a string
        save_file_as_pickle(response, filepath)
        transcript = parse_response(response)
        save_file_as_tsv(transcript, filepath)
