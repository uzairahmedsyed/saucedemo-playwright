# Saucedemo E2E Test Suite

Automated end-to-end test suite for [saucedemo.com](https://www.saucedemo.com) built with Playwright and Python, using the Page Object Model (POM) design pattern.

## Tests Covered

| Test | Description |
|------|-------------|
| `test_invalid_login` | Invalid credentials — error message verify |
| `test_valid_login` | Valid login — inventory page verify |
| `test_add_product_to_cart` | Add product to cart — badge count verify |
| `test_carticon_to_checkout` | Open cart — cart URL verify, proceed to checkout |
| `test_checkout` | Fill checkout form — step one URL verify |
| `test_order_confirmation` | Complete order — confirmation message verify |

## Project Structure
saucedemo-playwright/

├── Pages/

│   ├── LoginPage.py

│   ├── ProductPage.py

│   ├── CartPage.py

│   ├── CheckOutPage.py

│   └── OrderConfirmationPage.py

├── helpers/

│   └── actions.py

├── tests/

│   └── test_saucedemo.py

├── conftest.py

├── .gitignore

└── README.md

## Design Pattern

This project uses the **Page Object Model (POM)**. Each page of the application has its own class containing:
- Locators specific to that page
- Methods representing user actions on that page

Tests import these page classes and chain their methods to build complete user flows, keeping test logic separate from element locators.

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