
# ASCE 7 Chapter 30 - Wind Components and Cladding

This repository contains a Python implementation of Chapter 30 of the ASCE 7 standard, which deals with wind components and cladding. The code helps in calculating wind loads on different structures based on the guidelines provided in the standard.

## Features

- Calculation of GCp values for various figures and zones as specified in ASCE 7 Chapter 30.
- Support for structures with and without overhangs.
- Easy-to-use functions and classes for wind load calculations.

## Installation

To use this code, clone the repository and ensure you have Python installed on your system. The required dependencies can be installed using:

```bash
pip install numpy
```

## Usage

Here's a basic example of how to use the code:

```python
from chapter30 import Figure_30_3__1, Figure_30_3__2A

# Example usage for Figure 30.3-1
fig_30_3_1 = Figure_30_3__1(theta=45, A=100, without_overhang=True)
print(fig_30_3_1.GCp_values)

# Example usage for Figure 30.3-2A
fig_30_3_2A = Figure_30_3__2A(theta=30, A=200, without_overhang=False)
print(fig_30_3_2A.GCp_values)
```

## Files

- `chapter30.py`: Main module containing classes and methods for wind load calculations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License.

## Contact

For any queries or support, please contact Faheem at sd.faheemuddin@gmail.com.
