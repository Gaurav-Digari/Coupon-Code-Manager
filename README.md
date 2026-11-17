# Coupon Code Manager

A simple command-line tool written in Python. It creates random coupon codes, saves them in a file, and lets you redeem each code only once.

Codes are generated with the `secrets` module, which is made for random values that are safe to use for codes, tokens and passwords.

## Features

- Generate 1 to 10 random coupon codes at a time
- Codes look like `XXXX-XXXX-XXXX` and use only capital letters and numbers
- Duplicate codes are never created
- Redeem a coupon (works with small or capital letters)
- A coupon can only be used once
- Show all coupons with their status and a count of active and used ones
- Coupons are saved in a file, so they are still there the next time you run the program

## Requirements

- Python 3.10 or newer (the script uses `match`)
- No extra installation needed. `secrets`, `os` and `sys` come built into Python.

## Usage

```bash
python coupon_manager.py
```

The menu keeps showing until you choose 4:

```
COUPON MANAGER
==============
1. Generate coupons
2. Redeem coupon
3. Show all coupons
4. Exit
Enter choice:
```

| Option | What it does |
|---|---|
| 1. Generate coupons | Asks how many (1-10), creates that many new codes and saves them as `ACTIVE` |
| 2. Redeem coupon | Asks for a code and changes it from `ACTIVE` to `USED` |
| 3. Show all coupons | Lists every coupon with its status, then the active and used counts |
| 4. Exit | Closes the program |

## Example

```
Enter choice: 1
How many coupons (1-10)? 3
Generated:
K7Q2-M9XB-4TNA
R3ZD-81PW-VY5C
H6LF-2JQE-X9MU

Enter choice: 2
Enter coupon code: r3zd-81pw-vy5c
Coupon redeemed successfully.

Enter choice: 2
Enter coupon code: r3zd-81pw-vy5c
This coupon was already used.

Enter choice: 2
Enter coupon code: AAAA-BBBB-CCCC
Invalid coupon code.

Enter choice: 3
ALL COUPONS
===========
K7Q2-M9XB-4TNA       ACTIVE
R3ZD-81PW-VY5C       USED
H6LF-2JQE-X9MU       ACTIVE

Active : 2
Used   : 1
```

Your codes will be different every time you generate them.

## Messages

| Message | When it appears |
|---|---|
| `Coupon redeemed successfully.` | The code was active and is now used |
| `This coupon was already used.` | The code exists but was redeemed before |
| `Invalid coupon code.` | The code is not in the file |
| `No coupons found.` | No coupon has been generated yet |
| `Number must be between 1 and 10.` | The number of coupons is outside the range |
| `Invalid choice.` | The menu choice is not 1, 2, 3 or 4 |

## How Coupons Are Saved

Coupons are stored in `coupons.txt`, which the program creates by itself. Each line has the code and its status:

```
K7Q2-M9XB-4TNA : ACTIVE
R3ZD-81PW-VY5C : USED
H6LF-2JQE-X9MU : ACTIVE
```

Generating more coupons adds new lines at the end and keeps the old ones. Redeeming a coupon changes only that coupon's line.

## Project Structure

| File | Purpose |
|---|---|
| `coupon_manager.py` | The main script |
| `coupons.txt` | Saved coupons, created when you generate the first one |
| `README.md` | Project description |

## Notes

- Type whole numbers for the menu choice and for the number of coupons. Text in those places is not handled.
- Delete `coupons.txt` if you want to start again with no coupons.