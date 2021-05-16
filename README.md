# CSI2108

LFSR:
A basic linear shift feedback register for turning random numbers into more slightly more random numbers.
It outputs a 256 bit random number. it has a period length of 128 (repeats values after 128 cycles).

Hash:
Creates a hash (message digest) of an ascii/unicode value:
First it converts the message to binary bits and groups blocks together by 32 bits.
Then it pads the bits out to 48 bits with 0's so all blocks are equal and generate massive integers.
Then it adds all the blocks integers together, and the product of the integers is multiplied
by the prime number 2557 mod 65535, to output a final 16-bit number.

Created by Darcy for my CSI2108 Cryptographic concepts class
