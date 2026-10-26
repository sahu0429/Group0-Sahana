# TP2 Report — Modern Python Tooling and Fintech Payments

## 1. Project Overview

This project is a Python command-line application that retrieves Stripe account balance information using the Stripe API in test mode. It displays the results in a formatted table using Rich.

## 2. Environment Setup

The project uses Python, `uv` for dependency management and packaging, and a virtual environment.

An Application Control policy blocked the project's original virtual environment interpreter. I used an alternative Python interpreter to install dependencies, run tests, and execute the application.

## 3. API Integration and Secret Management

The application retrieves account balance information from Stripe using an API key stored in the `.env` file.

The application successfully returned the account currency, available balance, and `livemode` status. The API response confirmed that test mode was being used.

The `.env` file is excluded through `.gitignore`. The `.env.template` file provides a template without the actual secret key.

## 4. Dependencies and Packaging

The project uses the following dependencies:

- `requests` — HTTP requests to the API.
- `python-dotenv` — loading environment variables.
- `rich` — formatted command-line output.
- `pytest` — unit testing.

The `uv.lock` file records the resolved dependency versions. The dependency tree was inspected using `uv tree`.

The package was successfully built using `uv build`, producing a source distribution and a wheel.

## 5. Command-Line Interface

The CLI retrieves the Stripe account information and displays it in a formatted table with fields for status, currency, available balance, and live-mode status.

The project defines the `stripe-balance` command in `pyproject.toml`.

## 6. Testing

The client unit test was executed using pytest.

Result: **1 test passed.**

The HTTP response was mocked so the test could validate the result without relying on a live API request.

## 7. Debugging Challenge

The debugging challenge initially failed with a `TypeError` because the parsed `volume` and `weight` values were strings.

I inspected the variables using the VS Code debugger and identified the type mismatch. I corrected the parsing logic by converting both values to `float`.

The script then produced the expected results:

- Successful entries: 3
- Total volume: 650.0
- Average volume: approximately 216.67
- High-impact count: 1

## 8. Security and Git

The `.gitignore` file excludes the real `.env` file, virtual environments, Python cache files, and build artifacts.

The project files were staged with Git, and `uv.lock` was included.

## 9. Remaining Work

- Publish the package to TestPyPI and verify installation.
- Prepare and verify the final submission ZIP.
