# π Calculation with Catalan Numbers

This repository contains a Python script to calculate the digits of π using Catalan numbers and fixed-point arithmetic.

## Introduction

Calculating the digits of π has been a topic of interest for mathematicians and computer scientists alike. This project introduces a novel algorithm for π calculation that leverages Catalan numbers and fixed-point arithmetic.

## Algorithm

The series representation used in this algorithm is:

\[ \pi = 3 + 6 \sum_{n=1}^{\infty} \frac{(2n - 1) \cdot C_n}{(2n + 1) \cdot 16^n} \]

Where \( C_n \) is the nth Catalan number.

## Implementation

The implementation of the algorithm in Python can be found in the `pi_gmpy.py` file.

## Usage

To use the script, run the following command in your terminal:

```sh
python pi_gmpy.py
```

You will be prompted to enter the number of digits of π you want to calculate.

## Example

```sh
$ python pi_gmpy.py
How many digits of π? : 100
π = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679...∞
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.