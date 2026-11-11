# Walkthrough — python-fundamentals

What each notebook covers, in learning order, plus the bugs that were fixed so
everything runs top-to-bottom.

## The learning notebooks

1. **01_python_basics** — the very first steps: `print()`, arithmetic, strings, and variables.
2. **02_more_basics** — operators, converting between types (`int`, `str`, `float`), and reading input.
3. **03_collections** — the four built-in containers: lists, tuples, sets, dictionaries, and the methods that operate on them (`append`, `pop`, `remove`, indexing).
4. **04_conditionals** — decision-making with `if` / `elif` / `else`.
5. **05_loops** — repeating work with `for` and `while`, plus `break` and `continue`.
6. **06_functions** — defining functions, parameters, return values, and scope.
7. **07_comprehensions** — building lists and dictionaries in one line.
8. **08_comprehensions_and_lambdas** — comprehensions combined with `lambda`, `map`, and `filter`.
9. **09_exception_handling** — catching errors with `try` / `except` / `finally`.
10. **10_file_handling** — opening, reading, and writing text files.
11. **11_intro_to_oop** — classes, objects, attributes, and methods.

## Projects (`projects/`)

Each project is a small, self-contained program:

- **simple_calculator** — takes two numbers and an operator, returns the result.
- **number_guessing_game** — the computer picks a number; you guess with "higher/lower" hints.
- **rock_paper_scissors** — classic game against a random computer choice.
- **temperature_converter** — converts between Celsius and Fahrenheit.
- **number_base_converter** — converts a decimal number to octal, hexadecimal, and binary.

These use `input()`, so run them cell-by-cell.

## Bugs fixed during cleanup

- **03_collections** — a cell called `cars.remove("Jeep")` after `Jeep` had already been popped, so a top-to-bottom run crashed. Changed it to remove an item that still exists.
- **10_file_handling** — the file path was hardcoded to a Google Colab Drive location (`/content/drive/...`) that only exists inside Colab. Repointed it at a local `sample1.txt` (included in the repo) so it runs anywhere.
- **11_intro_to_oop** — the `square` class referenced an undefined name `size` and multiplied `self.square`. Rewrote it as a proper `Square(size)` class with a working `area()` method.
- Removed the duplicate `LICENCE` file, the misspelled `.gitingore`, and the stale Colab badges that pointed at old filenames.
