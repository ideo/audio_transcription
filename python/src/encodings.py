from google.cloud.speech import enums


ENCODINGS = {
    "FLAC":     enums.RecognitionConfig.AudioEncoding.FLAC,
    "LINEAR16": enums.RecognitionConfig.AudioEncoding.LINEAR16,
    "MULAW":    enums.RecognitionConfig.AudioEncoding.MULAW,
    "AMR":      enums.RecognitionConfig.AudioEncoding.AMR,
    "AMR_WB":   enums.RecognitionConfig.AudioEncoding.AMR_WB,
    "OGG_OPUS": enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
    "SPEEX_WITH_HEADER_BYTE":   enums.RecognitionConfig.AudioEncoding.SPEEX_WITH_HEADER_BYTE,
}
