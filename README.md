# Package Sorting Robot

This project contains a function for Thoughtful’s robotic automation factory. It dispatches packages to the correct stack based on their size and weight.

## Sorting Rules

- **Bulky**: Volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm
- **Heavy**: Mass ≥ 20 kg

## Stacks

- **STANDARD**: Not bulky or heavy
- **SPECIAL**: Either bulky or heavy
- **REJECTED**: Both bulky and heavy

## How to Run

1. Make sure you have Python installed.
2. Run the tests with:

```bash
python test.py
