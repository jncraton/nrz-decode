import wave
import struct
import bitarray
import sys

def decode_bits(wavfile):
    """ Implements a generator to return a decoded bitstream from wavfile 

    >>> next(decode_bits('message.wav'))
    0
    
    >>> list(decode_bits('message.wav'))[0:10]
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
    """

def bits_to_string(bits):
    """ Generator to map an iterator of bits to an iterator of characters

    >>> next(bits_to_string(iter([0, 0, 1, 1, 1, 0, 0, 1, 0, 1])))
    'N'

    >>> next(bits_to_string(iter([1, 0, 1, 1, 1, 0, 0, 1, 0, 1])))
    Traceback (most recent call last):
    ...
    ValueError: Invalid start bit

    >>> next(bits_to_string(iter([0, 0, 1, 1, 1, 0, 0, 1, 0, 0])))
    Traceback (most recent call last):
    ...
    ValueError: Invalid stop bit
    """

def decode(wavfile):
    """ Decode a wav file containing an NRZ encoded message

    >>> ''.join(decode('message.wav'))
    'Now you know how to decode messages transmitted using non-return-to-zero encoding!'
    """

if __name__ == '__main__':
    print(''.join(decode(sys.argv[1])))
        