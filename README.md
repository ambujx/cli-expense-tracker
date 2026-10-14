# Expense Tracker

A simple, menu-driven command-line expense tracker written in Python. Log your expenses, organize them by category, view totals, and delete entries. Data is saved locally in a JSON file.

## Features

- ➕ Add expenses with a name, amount, and category
- 🗂️ Categories are built up as you go — pick an existing one or create a new one
- 📋 View all expenses with a running total
- 📊 View expenses by category, with per-category totals
- 🗑️ Delete a single expense or clear all of them (with confirmation)
- 💾 Automatic saving to `expenses.json`
- ↩️ Enter `0` at most prompts to go back

## Requirements

- Python 3.6+
- No external dependencies
- A terminal that supports the `clear` command (Linux, macOS, or Windows terminals such as Git Bash / WSL)

## Project Structure

```
expense-tracker/
├── main.py          # Main application (the script containing the menu logic)
├── ui.py            # Provides the section_heading() helper
├── expenses.json    # Created automatically when you add your first expense
├── README.md
└── LICENSE
```

> **Note:** The app imports `section_heading` from a local `ui.py` module, so make sure that file sits alongside the main script.

## Usage

Run the script:

```bash
python main.py
```

You'll see the main menu:

```
MAIN MENU
1 -> Add Expense
2 -> View Expenses
3 -> Delete Expense
4 -> Exit
```

### Adding an expense

1. Enter a name (names can't be purely numeric).
2. Enter an amount (must be greater than zero).
3. Choose an existing category or create a new one.

Enter `0` at any prompt to cancel and return to the menu.

### Viewing expenses

- **View All** — lists every expense and the overall total.
- **View By Category** — shows each category with its total, then lists the expenses in the one you choose.

### Deleting expenses

Pick an expense by its number and confirm with `y`, or enter `-1` to delete **all** expenses.

## Data Storage

Expenses are stored in `expenses.json` in the directory you run the script from, in this format:

```json
[
    {
        "name": "Coffee",
        "amount": 3.5,
        "category": "Food"
    }
]
```

You can back up or edit this file manually if needed.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
