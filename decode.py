import wave
import struct
import bitarray
import sys

def wav_values(wavfile):
    """ Implements a generator to return raw waveform values from a wav file

    Raw values will be yielded as a floating-point value from -1 to 1

    >>> f"{next(wav_values('message.wav')):0.2f}"
    '-0.09'

    >>> f"{list(wav_values('message.wav'))[320]:0.2f}"
    '0.83'
    """
    
    with wave.open(wavfile, 'rb') as w:
        for pos in range(0, sys.maxsize):
            frame = w.readframes(1)
            if not frame:
                break
            yield struct.unpack('<h', frame)[0] / 2 ** 15

def decode_bits(wavfile):
    """ Implements a generator to return a decoded bitstream from wavfile 

    >>> next(decode_bits('message.wav'))
    0
    
    >>> list(decode_bits('message.wav'))[0:10]
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]

    Hint: enumerate can be used to iterate over the values in the file including a numeric index
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

    Hint: bitarray can be used to convert bits to bytes
        https://pypi.org/project/bitarray/
    Hint2: Raw byte values can be converted to strings using `bytes.decode`:
        https://docs.python.org/3/library/stdtypes.html#bytes.decode
    """

def decode(wavfile):
    """ Decode a wav file containing an NRZ encoded message

    >>> ''.join(decode('message.wav'))
    'Now you know how to decode messages transmitted using non-return-to-zero encoding!'
    """

if __name__ == '__main__':
    print(''.join(decode(sys.argv[1])))
        