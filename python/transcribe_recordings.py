import src


def transcribe_recordings(filepaths, sample_rates=[]):
    """
    """
    sample_rates = src.get_sample_rates(filepaths, sample_rates)
    bucket_name, uris = src.upload_audio_files(filepaths)

    transcripts = []
    for gcs_uri, rate in zip(uris, sample_rates):
        try:
            print(f"\nStarting transcription for `{gcs_uri}`")
            response = src.long_transcribe(gcs_uri, sample_rate_hertz=rate)
            print(f"Completed transcription for `{gcs_uri}`.")

        except Exception as e:
            print(f"Transcription of {gcs_uri} failed.")
            print(f"\nAPI Error: {e}\n")
            response = bucket_name

        transcripts.append(response)

    src.delete_everything(bucket_name)

    for response, filepath in zip(transcripts, filepaths):
        src.parse_and_save_file(response, filepath)


if __name__ == "__main__":
    filepaths = ['../audio/10_SteveAlexis.wav']
    transcribe_recordings(filepaths)
