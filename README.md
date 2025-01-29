# README for `adieu.py`

## Overview
`adieu.py` is a Python program that prompts the user to input names, one per line, until the user enters `Ctrl-D` (EOF). Once the user stops entering names, the program will print a farewell message, properly formatting the list of names with commas and "and" based on how many names were entered. The program uses the `inflect` module to handle the correct grammatical formatting.

## Features
- Prompts the user to input names one by one.
- Supports continuous input until the user enters `Ctrl-D` (EOF).
- Outputs a farewell message, formatting the list of names correctly:
  - Two names are separated by "and".
  - Three or more names are separated by commas with an "and" before the last name.

## Example Usage
```
$ python adieu.py
Name: Alice
Name: Bob
Name: Charlie
# Press Ctrl-D to end input

Adieu, adieu, to Alice, Bob, and Charlie
```

## Requirements
- Python 3.x
- `inflect` library (Install via `pip install inflect`)

## How to Run
1. Install the necessary package by running:
   ```
   pip install inflect
   ```
2. Run the program by executing:
   ```
   python adieu.py
   ```
3. Input names one by one.
4. Press `Ctrl-D` (or `Ctrl-Z` on Windows) to finish input and see the formatted farewell message.

## Notes
- The program assumes at least one name will be entered.
- The `inflect` library is used to handle the grammatical formatting of the farewell message.
