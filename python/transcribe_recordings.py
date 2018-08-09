import src
import pathlib
import wave
import subprocess

def convert_to_mono(filepaths):
    new_filepaths = []
    for p in filepaths:
        cur_path = pathlib.Path(p)
        data = wave.open(p, 'rb')
        nchannels = data.getnchannels()
        data.close()
        if nchannels == 1:
            new_filepaths.append(p)
            continue
        if nchannels == 2:
            new_name = cur_path.stem + '_mono' + cur_path.suffix
            old_path = str(cur_path)
            new_path = str(cur_path.parent / new_name)
            print(old_path)
            cmd = ['ffmpeg', '-i', old_path, '-ac', '1', new_path]
            print(cmd)
            subprocess.run(cmd)
            new_filepaths.append(new_path)

    return new_filepaths


def transcribe_recordings(filepaths, sample_rates=[]):
    """
    """
    filepaths = convert_to_mono(filepaths)
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
            # Helpful to see the URI of a failed transcription
            response = gcs_uri

        transcripts.append(response)

    src.delete_everything(bucket_name)

    for response, filepath in zip(transcripts, filepaths):
        src.parse_and_save_file(response, filepath)


if __name__ == "__main__":
    filepaths = ['/Users/chris/Dropbox (IDEO)/Partners Healthcare Phoenix 36507/Work In Progress/00_Beacon/06_Photo:Video/20180726 Nancy Hiltz/20180726-Nancy Hiltz.WAV']
    #'/Users/chris/Documents/cheesereel/cheesereel/public/static/audio/14 Dr. Mohan.WAV']
    transcribe_recordings(filepaths)
