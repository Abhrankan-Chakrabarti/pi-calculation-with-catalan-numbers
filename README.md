# Catalan π Algorithm

This repository contains an implementation of a newly discovered algorithm for calculating the digits of π using Catalan numbers, derived from ![6 arcsin(0.5)](https://latex.codecogs.com/svg.latex?6%20%5Carcsin%280.5%29). The algorithm uses high-precision arithmetic and optimized series summation to achieve efficient computation.

## Introduction

Calculating the digits of π has been a topic of interest for mathematicians and computer scientists alike. This project introduces a novel algorithm for π calculation that leverages Catalan numbers and fixed-point arithmetic.

## Algorithm

The series representation for π used in this algorithm is derived from the inverse sine function:

![\pi = 6 arcsin(0.5)](https://latex.codecogs.com/svg.latex?%5Cpi%20%3D%206%20%5Carcsin%280.5%29)

By expanding ![arcsin(x)](https://latex.codecogs.com/svg.latex?%5Carcsin%28x%29) as a series, we get:

![series](https://latex.codecogs.com/svg.latex?%5Carcsin%28x%29%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7B%282n%29%21%7D%7B4%5En%20%28n%21%29%5E2%20%282n%20%2B%201%29%7D%20x%5E%7B2n%20%2B%201%7D)

Substituting ![x = 0.5](https://latex.codecogs.com/svg.latex?x%20%3D%200.5) and multiplying by 6, we derive the series:

![series](https://latex.codecogs.com/svg.latex?%5Cpi%20%3D%203%20%2B%206%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7B%282n%20-%201%29%20%5Ccdot%20C_%7Bn-1%7D%7D%7B%282n%20%2B%201%29%20%5Ccdot%2016%5En%7D)

Where ![C_n](https://latex.codecogs.com/svg.latex?C_n) is the nth Catalan number.

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out via GitHub or email.