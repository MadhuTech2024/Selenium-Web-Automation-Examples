# Selenium Web Automation Examples

This repository contains Python scripts that demonstrate how to use Selenium WebDriver for automating browser tasks such as searching, scraping event data, and submitting forms.

## Contents

- **main.py**  
  Extracts and prints upcoming event times and names from [python.org](https://www.python.org/).

- **interaction.py**  
  Automates a search for "python" on the [Wikipedia main page](https://en.wikipedia.org/wiki/Main_Page).

- **signup.py**  
  Fills out and submits a signup form at [secure-retreat-92358.herokuapp.com](https://secure-retreat-92358.herokuapp.com/).

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- Chrome browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (matching your Chrome version)

## Setup

1. Install Selenium:
    ```bash
    pip install selenium
    ```
2. Download and place ChromeDriver in your PATH.

## Usage

Run any script with:
```bash
python main.py
python interaction.py
python signup.py
```

## License

This project is for educational purposes.