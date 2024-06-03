# Lecture 0: Representing Numbers, Text, Images, Video, & Sounds. Algorithms.

## What is Computer Science?
- problem solving, precision and it's methodical.
- Generating a solution to our problem

## Representing Numbers:
__Unary System:__ Each digit represents single value, 1. EG: Counting with our fingers.
__Decimal System:__ To count up to 10
__Binary System:__ For computers, 0s and 1s. Each of the 0s or 1s(binary digits) are called Bits. 
| Binary System | Decimal System |
|---------------|----------------|
|   000         |   0            |
|   001         |   1            |
|   010         |   2            |
|   011         |   3            |
|   100         |   4            |
|   101         |   5            |
|   110         |   6            |
|   111         |   7            |

Numbers > 7, need another bit. Most computers use 8 bits = 1 byte. For eg, __00000101__ = 5

To derive the binary system: 
- Using decimal system, eg 123
- ones place = 3, tenths place = 2, hundreths place = 1
- 123 = 100 * 1 + 10 * 2 + 1 * 3
- 123 = 10^2 * 1 + 10^1 * 2 + 10^1 * 3

| 10^2 | 10^1 | 10^0 |
|------|------|------|
|   1  |   2  |   3  |

__Linking it to binary, we replace 10 with 2 (dec = 10 & bi = 2):__
| 2^2 | 2^1 | 2^0 |
|-----|-----|-----|
|  4  |  2  |  1  |

Decimal value, 0 = 000
|  4  |  2  |  1  |
|-----|-----|-----|
|  0  |  0  |  0  |

Decimal value, 3 = 011
|  4  |  2  |  1  |
|-----|-----|-----|
|  0  |  1  |  1  |
- 3 = 2^1 + 1^1

## Representing Texts: ASCII and Unicode
- __ASCII__ has upper and lowercase and punctuations
- __Unicode__ is used to represent letters with accent marks or symbols or emojis (since only description of emoji is standardised, emojis may differ between software companies)

- "A" = 65 = 01000001
- "B" = 66

one byte = 8 bits. Therefore, we can have 2^8 = 256 different values (incld 0)
__Highest value we can count up to = 255__

## Representing Images, Video and Sounds
RGB = amount of red, green n blue in a colour
- 1 number = 8 bits = 1 byte
- 3 numbers = 24 bits = 3 byte = represent many colours

RGB = 72,73,33 = Dark yellow

- Images made up of pixels
- Videos made up of changing images
- Music represented w bits. Each bit can represent the note, duration and volume (search about MIDI)

## Algorithms
Definition: Instruction/procdeure to solve a recurring problem
- Different algortihms have different efficacy levels