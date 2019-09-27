NRZ Decoder
===========

The following project provides the scaffold to build a basic non-return-to-zero decoder.

Protocol Description
--------------------

The included `message.wav` file is a playable sound file that encodes a message using the following scheme (very similar to RS232)

The message is first encoded using UTF-8 and then split into bytes. Prior to sending a byte, a single stop bit (0) is transmitted followed by the 8 bits in the bytes, beginning with the least significant bit. A stop bit (1) is sent at the end of the message.

The transmission uses a baud rate of 300.
