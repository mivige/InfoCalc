# InfoCalc: Calculator for Information Theory

**InfoCalc** is an interactive Python-based calculator for information theory, designed to make it easy to calculate entropy, average length, and efficiency. It features a simple graphical interface built with `Tkinter`, making it ideal for students, researchers, or information theory enthusiasts.

## Features

- **Entropy Calculation**: Computes entropy based on a given probability distribution.
- **Average Length Calculation**: Determines the average code length given lengths and probabilities.
- **Efficiency Calculation**: Calculates code efficiency based on entropy and average length.

## Installation

To install **InfoCalc**, download the `.exe` file from the repository. Run the file directly without needing to install Python.

## Usage

1. Select the operation you want (Entropy, Average Length, or Efficiency) from the dropdown menu.
2. Enter the values:
    - For entropy: a comma-separated list of probabilities (e.g., `0.2, 0.3, 0.5`).
    - For average length: a comma-separated list of lengths and a corresponding list of probabilities (e.g., `1, 2, 3`, probabilities: `0.2, 0.3, 0.5`).
    - For efficiency: enter the values of entropy and average length.
3. Press **Calculate** to see the result.

## Example

### Entropy
**Input**: `0.35, 0.15, 0.50`  
**Output**: `Entropy: 1.440645 bits`

### Average Length
**Input**:  
  - Lengths: `2, 3, 4, 4, 1`  
  - Probabilities: `0.20, 0.15, 0.05, 0.15, 0.45`  
**Output**: `Average Length: 2.100000`

### Efficiency
**Input**:  
  - Entropy: `2.01997`  
  - Average Length: `2.1`  
**Output**: `Efficiency: 0.961890`

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss potential improvements.

## License

This project is licensed under the MIT License.