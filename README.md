# Saucedemo E2E Test Suite

Automated end-to-end test suite for [saucedemo.com](https://www.saucedemo.com) built with Playwright and Python.

## Tests Covered

| Test | Description |
|------|-------------|
| `test_invalid_login` | Invalid credentials — error message verify |
| `test_valid_login` | Valid login — inventory page verify |
| `test_add_to_cart` | Add product to cart — badge count verify |
| `test_open_cart` | Open cart — cart URL verify |
| `test_proceed_to_checkout` | Checkout button — step one URL verify |
| `test_fill_checkout_form` | Fill checkout form — step two URL verify |
| `test_confirm_order` | Place order — confirmation message verify |

## Project Structure

## Setup & Run

```bash
# Install dependencies
pip install playwright pytest-playwright

# Install browsers
playwright install

# Run tests
pytest tests/test_saucedemo.py -v

# Run with browser visible
pytest tests/test_saucedemo.py -v --headed
```

## Tech Stack

- Python 3.x
- Playwright
- pytest