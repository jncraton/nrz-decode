import wave
import struct
import sys


def get_samples(wavfile):
    """Returns a list of raw waveform values from a wav file

    Raw values will be returned as floating-point values from -1 to 1

    For simplicity, this function need only support wav files up to 1 MiB

    >>> f"{get_samples('message.wav')[0]:0.2f}"
    '-0.09'

    >>> f"{get_samples('message.wav')[320]:0.2f}"
    '0.83'
    """

    with wave.open(wavfile, "rb") as w:
        return [f[0] / 2 ** 15 for f in struct.iter_unpack("<h", w.readframes(1e6))]


def decode_bits(samples):
    """Returns a list of bits decoded from wave file samples

    >>> decode_bits([-.5]*1000)[0]
    0

    >>> decode_bits([.5]*1000)[0]
    1

    >>> decode_bits(get_samples('message.wav'))[0:10]
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
    """


def get_char(bits):
    """Converts a list of 8 bits to a Python character

    >>> get_char([0, 1, 1, 1, 0, 0, 1, 0])
    'N'

    >>> get_char([0, 0, 0, 0, 1, 0, 1, 0])
    'P'

    >>> get_char([0, 1, 0, 0, 1, 1, 1, 0])
    'r'
    """


def parse_byte(byte):
    """Processes 1 byte of data (10 total bits) off the bitstream

    Note that byte here does not refer to the Python byte data type. A byte
    here refers to a 10 bit sequence including the stop and start bit on
    the wire.

    The stop and start bits should be verified before the string is returned.

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


def decode_string(bits):
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


def decode(wavfile):
    """Decode a wav file containing an NRZ encoded message

    >>> ''.join(decode('message.wav'))
    'Now you know how to decode messages transmitted using non-return-to-zero encoding!'
    """

    samples = get_samples(wavfile)
    bits = decode_bits(samples)

    return decode_string(bits)


if __name__ == "__main__":
    print("".join(decode(sys.argv[1])))
