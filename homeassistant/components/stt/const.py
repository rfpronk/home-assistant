"""STT constante."""
from enum import Enum

DOMAIN = "stt"


class AudioCodecs(Enum):
    """Supported Audio codecs."""

    PCM = "pcm"
    OPUS = "opus"


class AudioFormats(Enum):
    """Supported Audio formats."""

    WAV = "wav"
    OGG = "ogg"


class AudioBitrates(Enum):
    """Supported Audio bitrates."""

    BITRATE_8 = 8
    BITRATE_16 = 16
    BITRATE_24 = 24
    BITRATE_32 = 32


class AudioSamplerates(Enum):
    """Supported Audio samplerates."""

    SAMPLERATE_8000 = 8000
    SAMPLERATE_11000 = 11000
    SAMPLERATE_16000 = 16000
    SAMPLERATE_18900 = 18900
    SAMPLERATE_22000 = 22000
    SAMPLERATE_32000 = 32000
    SAMPLERATE_37800 = 37800
    SAMPLERATE_44100 = 44100
    SAMPLERATE_48000 = 48000
