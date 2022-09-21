from typing import List
import wave
import struct
import sys


def get_samples(wavefile: str) -> List[float]:
    """Returns a list of raw waveform values from a wav file

    Raw values will be returned as floating-point values from -1 to 1

    For simplicity, this function need only support wav files up to 1 MiB

    >>> f"{get_samples('message.wav')[0]:0.2f}"
    '-0.09'

    >>> f"{get_samples('message.wav')[320]:0.2f}"
    '0.83'
    """

    with wave.open(wavefile, "rb") as w:
        return [
            f[0] / 2**15 for f in struct.iter_unpack("<h", w.readframes(int(1e6)))
        ]


def decode_bits(samples: List[float]) -> List[int]:
    """Returns a list of bits decoded from wave file samples

    >>> decode_bits([-.5]*500)
    [0, 0, 0]

    >>> decode_bits([.5]*500)
    [1, 1, 1]

    >>> decode_bits(get_samples('message.wav'))[0:10]
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
    """


def get_char(bits: List[int]) -> str:
    """Converts a list of 8 bits to a Python character

    Conversion assumes that bits are stored with the least significant
    bit first.

    >>> get_char([0, 1, 1, 1, 0, 0, 1, 0])
    'N'

    >>> get_char([0, 0, 0, 0, 1, 0, 1, 0])
    'P'

    >>> get_char([0, 1, 0, 0, 1, 1, 1, 0])
    'r'
    """


def parse_byte(byte: List[int]) -> str:
    """Converts 10 bits with start and stop bit to a single character

    The stop and start bits are verified before the character is returned.

    >>> parse_byte([0, 0, 1, 1, 1, 0, 0, 1, 0, 1])
    'N'

    >>> parse_byte([1, 0, 1, 1, 1, 0, 0, 1, 0, 1])
    Traceback (most recent call last):
    ...
    ValueError: Invalid start bit

    >>> parse_byte([0, 0, 1, 1, 1, 0, 0, 1, 0, 0])
    Traceback (most recent call last):
    ...
    ValueError: Invalid stop bit
    """


def decode_string(bits: List[int]) -> str:
    """Creates a string from a list of raw bits

    >>> decode_string([0, 0, 1, 1, 1, 0, 0, 1, 0, 1])
    'N'

    >>> decode_string([0, 0, 1, 1, 1, 0, 0, 1, 0, 1]*3)
    'NNN'

    >>> next(decode_string([1, 0, 1, 1, 1, 0, 0, 1, 0, 1]))
    Traceback (most recent call last):
    ...
    ValueError: Invalid start bit

    >>> next(decode_string([0, 0, 1, 1, 1, 0, 0, 1, 0, 0]))
    Traceback (most recent call last):
    ...
    ValueError: Invalid stop bit
    """


def decode(wavefile: str) -> str:
    """Decode a wav file containing an NRZ encoded message

    >>> ''.join(decode('message.wav'))[0]
    'N'
    >>> ''.join(decode('message.wav'))[1]
    'o'
    >>> ''.join(decode('message.wav'))[-1]
    '!'
    >>> ''.join(decode('message.wav'))[-2]
    'g'
    >>> len(''.join(decode('message.wav')))
    82
    """

    samples = get_samples(wavefile)
    bits = decode_bits(samples)

    return decode_string(bits)


if __name__ == "__main__":
    print("".join(decode(sys.argv[1])))
