from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def long_transcribe(gcs_uri, sample_rate_hertz=44100):
    """
    Asynchronously transcribe an audio file that is longer than one minute,
    given its google cloud stroage uri.
    """
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate_hertz,
        language_code="en-US",
        enable_word_time_offsets=True)

    operation = client.long_running_recognize(config, audio)

    print("Waiting for operation to complete...")
    response = operation.result()

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    # for result in response.results:
        # The first alternative is the most likely one for this portion.
        # print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        # print('Confidence: {}'.format(result.alternatives[0].confidence))
    return response
