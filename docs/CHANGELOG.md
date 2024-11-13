# Changelog

All notable changes to this project will be documented in this file.

---

## [v1.0.0] - 2024-11-13

### Added
- **Core Functionality**:
- Implemented the primary operations of **InfoCalc**:
    - **Entropy Calculation**: Computes entropy for a given probability distribution.
    - **Average Length Calculation**: Calculates the average code length based on given lengths and probabilities.
    - **Efficiency Calculation**: Determines the efficiency of a code based on entropy and average length.
- Integrated **Tkinter** interface to provide an interactive GUI for selecting operations and entering values.
- **Modules and Structure**:
- Separated core functionality into distinct files:
    - `src/gui.py` for GUI setup and control flow.
    - `src/utils.py` for calculation functions (`calculate_entropy`, `calculate_avg_length`, `calculate_efficiency`).
    - `src/validators.py` for input validation of user entries.
- Configured project with modular folder structure including:
    - `docs/` for documentation files.
    - `tests/` for unit testing of calculations and validation functions.
- **Validation Layer**:
- Created `validators.py` with robust input validation:
    - Verifies correct probability values and length inputs.
    - Ensures non-negative and normalized probability distributions.
- **Unit Testing**:
- Developed unit tests for all major functions:
    - Tests for entropy, average length, and efficiency calculations.
    - Tests for validator functions to check input consistency.
- **Documentation**:
- Drafted user documentation in the `docs/` folder:
    - **User Guide**: Basic usage of InfoCalc's interface and features.
- Added project metadata and setup configuration in `setup.py`.

### Fixed
- **Calculation Errors**:
  - Resolved division-by-zero errors in entropy calculations when probability is `1.0` or `0.0`.
- **Executable Compatibility**:
  - Corrected issues with missing modules (`tkinter`, `ttk`) in executable packaging by enforcing `--hidden-import` directives.
  - Adjusted `auto-py-to-exe` settings to ensure `tkinter` modules load correctly within the executable.
