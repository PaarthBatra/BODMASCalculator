# BODMAS Calculator

A desktop calculator built with **Python** and **PyQt6** that evaluates mathematical expressions following the **BODMAS** (Bracket, Order, Division, Multiplication, Addition, Subtraction) rule of precedence.

Originally authored by **Paarth Batra** (2013), updated to PyQt6 with bug fixes and security improvements.

---

## Features

- ✅ Full **BODMAS** expression evaluation
- ✅ **Brackets** `(` `)` — nested bracket support
- ✅ **Power** `^` operator (e.g. `2^8 = 256`)
- ✅ **Square root** `√` button
- ✅ **Reciprocal** `1/x` button
- ✅ **Percentage** `%` calculation
- ✅ **Negate** `+-` toggle (positive ↔ negative)
- ✅ **Show Expression** `Expression =` — displays full expression in upper display
- ✅ **Copy / Copy-Expression / Paste** via Edit menu (`Ctrl+C`, `Ctrl+E`, `Ctrl+V`)
- ✅ Full **keyboard input** support

---

## Keyboard Shortcuts

| Key | Action |
|---|---|
| `0–9`, `.` | Digit / decimal input |
| `+` `-` `*` `/` | Arithmetic operators |
| `^` (`Shift+6`) | Power operator |
| `(` `)` | Brackets |
| `Enter` / `Return` | Equals (`=`) |
| `Backspace` | Delete last character |
| `Escape` | Clear All (`C`) |
| `Delete` | Clear Entry (`CE`) |
| `Ctrl+C` | Copy result |
| `Ctrl+E` | Copy expression |
| `Ctrl+V` | Paste expression |
| `F1` | Open Help contents |

---

## Requirements

- Python 3.8+
- PyQt6

Install dependencies:

```bash
pip install PyQt6
```

---

## Running the App

```bash
python Calculator.py
```

---

## Project Structure

| File | Description |
|---|---|
| `Calculator.py` | Main window, UI layout, keyboard & button event wiring |
| `CalculatorInputLogic.py` | Expression state machine — all input/calculation logic |
| `About.py` | Modal "About Us" dialog |
| `Contents.py` | Scrollable Help/Documentation dialog |
| `setup.py` | Build script (used to create the distributable `.exe`) |
| `Exe/` | Compiled executable output |

---

## Architecture

The app uses two cooperating state variables displayed on screen:

| Variable | Role |
|---|---|
| `lineE` | Current number / partial expression shown in the **lower** display |
| `lineEU` | Full running expression shown in the **upper** display |

All button clicks and key presses funnel through `Calculator.CallAddTxt()` → `CalculatorInputLogic.addTxt()`, which is a state machine (if/elif chain) that decides how to update `lineE` / `lineEU` based on the current state and input.

Final evaluation uses `CalculatorInputLogic.safe_eval()` — an **AST-based safe evaluator** that supports only whitelisted arithmetic operations (no arbitrary Python code execution).

---

## Recent Fixes (v3.0.x)

| # | Issue | Fix |
|---|---|---|
| 1 | **`^` power button did nothing** | Added `^` to all state-machine branches; `safe_eval` converts `^` → `**`; `Shift+6` keyboard shortcut added |
| 2 | **`eval()` security risk** | Replaced all `eval()` calls with `safe_eval()` (AST-based, whitelisted operators only) |
| 3 | **`Copy()` method missing** | `Ctrl+C` was wired but `Copy()` was never defined — would crash; method added |
| 4 | **Negate `+-` typo in brackets** | `replace("(,", "-(")` had an extra comma — fixed to `replace("(", "-(")` |

---

## Version History

All versions authored by **Paarth Batra**.

| Version | Date | Changes |
|---|---|---|
| **1.0** | Aug 2013 | Initial release — basic BODMAS calculator with PyQt GUI |
| **2.0** | Aug 18, 2013 | Added `About Me` modal dialog; `findOperator` and `calculateStrVal` logic; no file handling — calculations on the fly |
| **2.1** | Aug 22, 2013 | Set default focus on main `QLineEdit`; About dialog made modal |
| **2.2** | Aug 23, 2013 | Moved `SimulateBackspace` into `CalculatorInputLogic` module; changed `QLineEdit` → `QLabel` for display |
| **2.3** | Aug 24, 2013 | Standalone `sqrt`, `1/x`, and `%` (percentage) functions; Negate (`+-`) implemented |
| **2.5** | Aug 24, 2013 | Moved all code out of `UI_Window` into `Calculator(QMainWindow)` to enable `keyPressEvent` on label |
| **2.7** | Aug 25, 2013 | Support for `(` brackets at any position; bracket count tracking; multiple new `elif` branches in `addTxt` |
| **2.8** | Aug 27, 2013 | Negate function fixed for bracket expressions; `showExpression` (`SE=`) added — shows full expression in upper display |
| **2.8.2** | — | `()` bracket support via `CalculatorInputLogic v2.7` |
| **2.8.3** | — | Brackets `(` `)` can now be inputted via keyboard |
| **2.8.4** | — | `SE=` (Show Expression) button added |
| **2.8.5** | — | Made `SE=` button larger; added Copy/Paste; added `www.versionpb.co.in` link |
| **2.9** | Oct 2, 2013 | Compiled with new About and Contents help menu item |
| **3.0.0.0** | Jun 29, 2016 | Added "Register Free" link; Contents opens web link; icon changed from author photo to calculator image; migrated to PyQt6 |
| **3.0.x** | Jun 2026 | **Bug fixes:** `^` power operator fully implemented; replaced all `eval()` with AST-based `safe_eval()`; fixed missing `Copy()` method; fixed negate `+-` typo in bracket mode |

---

## License

BODMAS Calculator is **free software** for non-profit use.  
Feel free to share it with friends. Ideas and suggestions are welcome.

---

## Contact

**Author:** Paarth Batra  
**Version:** 3.0.x  
**Website:** [www.versionpb.co.in](http://www.versionpb.co.in)
