# TP2 Report — Modern Python Tooling and Fintech Payments

## 1. Project Overview

This project is a Python command-line application that retrieves Stripe account balance information using the Stripe API in test mode. It displays the results in a formatted terminal table using Rich.

## 2. Environment Setup

The project uses Python, `uv` for dependency management and packaging, and a virtual environment.

An Application Control policy blocked the original project virtual environment interpreter. I used an alternative Python interpreter to install dependencies, execute the application, and run tests.

The environment inspection script was used to examine Python executable paths, environment prefixes, and import search paths. `uv` helps manage project dependencies and execute commands in an isolated environment without requiring manual activation.

## 3. API Integration and Secret Management

The application retrieves account balance information from Stripe using the `STRIPE_API_KEY` environment variable, loaded from `.env` during local development.

The successful API response was:

```text
Status: LIVE_SUCCESS
Currency: EUR
Available Balance: 0.0
Livemode: False
```

The response confirms that the request succeeded in Stripe test mode.

The `.env` file is excluded through `.gitignore`, while `.env.template` provides a public configuration template without real credentials. Environment variables keep secrets separate from source code and make it easier to use different configurations across environments.

## 4. Dependencies and Packaging

The project uses these dependencies:

- `requests` — sends HTTP requests to the Stripe API.
- `python-dotenv` — loads environment variables from `.env`.
- `rich` — formats CLI output.
- `pytest` — runs unit tests.

The `uv.lock` file records resolved dependency versions and package hashes to support reproducible installations and help detect unexpected changes to downloaded packages.

I inspected the dependency tree using `uv tree`. Direct dependencies are declared in `pyproject.toml`, while transitive dependencies are installed to support those packages.

### Semantic Versioning

- `requests = "^2.31.0"` allows compatible versions from `2.31.0` up to, but not including, `3.0.0`.
- `urllib3 = "~=2.2.1"` allows compatible releases from `2.2.1` up to, but not including, `2.3.0`.
- `rich = "==13.7.1"` allows only version `13.7.1`.

If a breaking `requests` version `3.0.0` is released, the constraint `^2.31.0` does not allow it. `pyproject.toml` declares dependency requirements, while `uv.lock` records the specific resolved versions.

## 5. Command-Line Interface and TestPyPI Deployment

The CLI uses Rich to display the Stripe response in a formatted table containing status, currency, available balance, and live-mode status.

The `stripe-balance` command is configured in `pyproject.toml` using the project script entry point.

The package was built with `uv build`, producing a wheel and a source distribution. Version `0.1.1` was published to TestPyPI.

I installed version `0.1.1` from TestPyPI and verified the CLI module import successfully.

TestPyPI package:
https://test.pypi.org/project/sahana-sridhar-fintechpayments/0.1.1/

A wheel contains files in a format that can generally be installed directly without rebuilding the package from source. A source distribution contains the source files and build metadata, and may require a build step during installation.

## 6. Testing

The client unit test was executed using pytest.

Result: **1 test passed.**

The HTTP response was mocked so the test could validate the client behavior without depending on a live API request.

## 7. Debugging Challenge

The debugging challenge initially failed because the parsed `volume` and `weight` values were strings instead of numeric values.

Using the debugger, I inspected the parsed values and corrected the parsing logic by converting both values to `float`.

The script produced the expected results:

```text
Aggregate Result: {
    'successful_entries': 3,
    'total_volume': 650.0,
    'avg_volume': 216.66666666666666,
    'high_impact_count': 1
}
```

The successful entries were `REC_001`, `REC_003`, and `REC_004`. Only `REC_003` had an impact greater than 500.

The call stack should be described based on the frames actually observed in the debugger. The expected logical sequence is the module-level code, `aggregate_telemetry`, and `compute_weighted_metric`.

## 8. Security and Git

The `.gitignore` file excludes `.env`, virtual environments, Python cache files, and build artifacts. The `.env.template` file contains only placeholder configuration values.

The source code was pushed to the Group 0 GitHub repository:

https://github.com/sahu0429/Group0-Sahana

The Stripe secret key was exposed during development, so it must be rotated or revoked. No real API keys or TestPyPI tokens should be included in the GitHub repository or submission archive.

## 9. Final Submission Checklist

- [x] Build the package with `uv build`.
- [x] Publish version `0.1.1` to TestPyPI.
- [x] Install the published package and verify the