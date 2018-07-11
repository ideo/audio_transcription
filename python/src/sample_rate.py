from warnings import warn

import audiotools


def get_sample_rates(filepaths, sample_rates):
    """
    Return the sample rate of the audiofile. Right now, this only works for
    `.wav` files
    """
    if not sample_rates:
        for audio_file in filepaths:
            if file_is_not_wav(audio_file):
                sample_rates.append(44100)
            else:
                rate = audiotools.open(audio_file).sample_rate()
                sample_rates.append(rate)
        return sample_rates

    else:
        return sample_rates


def file_is_not_wav(filepath):
    """
    Currently, audiotools is only configured for `.wav` files. Theoretically,
    it's possible to get it to work for all types.
    """
    ext = filepath.split('.')[-1]
    ext_is_not_wav = (ext != 'wav')

    if ext_is_not_wav:
        msg = ('Currently, the audiotools library is only configured for '
            '`.wav` files. The program will assume a sample rate of 44100 Hz. '
            'If this is incorrect, please specify the sample rate for each '
            'audiofile. You can find the sample rate by right clicking on a '
            'file and choosing "Get Info."')
        warn(msg)

    return ext_is_not_wav
