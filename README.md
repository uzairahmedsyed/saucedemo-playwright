# Saucedemo E2E Test Suite

Automated end-to-end test suite for [saucedemo.com](https://www.saucedemo.com) built with Playwright and Python, using the Page Object Model (POM) design pattern.

## Tests Covered

| Test | Description |
|------|-------------|
| `test_invalid_login` | Invalid credentials and missing username/password — exact error message and login page verify |
| `test_locked_user` | Locked account — exact error message and denied login verify |
| `test_logout` | Logout — return to login page verify |
| `test_product_sorting` | Name A–Z/Z–A and price low–high/high–low verify |
| `test_remove_products` | Remove products from inventory and cart — badge updates and empty cart verify |
| `test_checkout_totals` | Product prices, subtotal, rounded 8% tax and final total verify |
| `test_valid_login` | Valid login — inventory page verify |
| `test_add_product_to_cart` | Add products to cart — badge count verify |
| `test_carticon_to_checkout` | Open cart — cart URL and item names verify |
| `test_checkout` | Fill checkout form — step two URL and item names verify |
| `test_checkout_form_validation` | Missing checkout fields (parametrized) — error message verify |
| `test_order_confirmation` | Complete order — confirmation message verify |

There is also `tests/test_api.py`, a standalone script that calls the [reqres.in](https://reqres.in) API using a key from `.env`.

## Project Structure

The UI suite contains 22 parametrized test cases. Expected login errors, product prices and the tax rate are defined in `Data/test_data.json`.

```
saucedemo-playwright/
├── Pages/
│   ├── LoginPage.py
│   ├── ProductPage.py
│   ├── CartPage.py
│   ├── CheckoutPage.py
│   └── OrderConfirmationPage.py
├── Data/
│   └── test_data.json
├── tests/
│   ├── test_saucedemo.py
│   └── test_api.py
├── conftest.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Design Pattern

This project uses the **Page Object Model (POM)**. Each page of the application has its own class containing:
- Locators specific to that page
- Methods representing user actions on that page

Tests import these page classes and chain their methods (via fixtures in `conftest.py`) to build complete user flows, keeping test logic separate from element locators.

Test data (credentials, product IDs, checkout inputs, validation cases) is centralized in `Data/test_data.json` rather than hardcoded in tests.

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Install browsers
playwright install

# Run tests
pytest tests/test_saucedemo.py -v

# Run with browser visible
pytest tests/test_saucedemo.py -v --headed
```

### Environment variables

`tests/test_api.py` requires an `API_KEY` for reqres.in. Create a `.env` file in the project root:

```
API_KEY=your_api_key_here
```

## Tech Stack

- Python 3.x
- Playwright
- pytest / pytest-playwright
- requests + python-dotenv (for `test_api.py`)
