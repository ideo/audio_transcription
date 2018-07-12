from google.cloud import speech
# from google.cloud.speech import enums
from google.cloud.speech import types

from .sample_rate import determine_encoding_format


def long_transcribe(gcs_uri, sample_rate_hertz=44100):
    """
    Asynchronously transcribe an audio file that is longer than one minute,
    given its google cloud stroage uri.
    """
    client = speech.SpeechClient()
    encoding = determine_encoding_format(sample_rate_hertz)

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        # encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        encoding=encoding,
        sample_rate_hertz=sample_rate_hertz,
        language_code="en-US",
        enable_word_time_offsets=True)

    operation = client.long_running_recognize(config, audio)

    print("Waiting for operation to complete...")
    response = operation.result()
    return response
