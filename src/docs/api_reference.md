# API Reference

The **InfoCalc** API includes core calculation functions and validation utilities.

## Calculations

### `calcola_entropia(probabilities)`
- **Description**: Calculates entropy based on given probabilities.
- **Parameters**: 
    - `probabilities` (list of floats): Probabilities must sum to 1.
- **Returns**: Entropy (float).
- **Example**: `calcola_entropia([0.2, 0.3, 0.5])`

### `calcola_lunghezza_media(lengths, probabilities)`
- **Description**: Calculates average length.
- **Parameters**:
  - `lengths` (list of ints): Lengths corresponding to probabilities.
  - `probabilities` (list of floats): Probabilities must sum to 1.
- **Returns**: Average length (float).
- **Example**: `calcola_lunghezza_media([1, 2, 3], [0.3, 0.4, 0.3])`

### `calcola_efficienza(entropy, average_length)`
- **Description**: Calculates efficiency based on entropy and average length.
- **Parameters**:
  - `entropy` (float): The entropy of the source.
  - `average_length` (float): The average code length.
- **Returns**: Efficiency (float).
- **Example**: `calcola_efficienza(2.0, 2.5)`

## Validators

### `validate_probabilities(probabilities)`
- **Description**: Checks if a list of probabilities is valid.
- **Parameters**: `probabilities` (list of floats).
- **Returns**: Boolean.

### `validate_lengths_and_probabilities(lengths, probabilities)`
- **Description**: Checks if lengths and probabilities are compatible.
- **Parameters**: 
  - `lengths` (list of ints).
  - `probabilities` (list of floats).
- **Returns**: Boolean.
