# Company LinkedIn Info Scraper

## Overview

This Python script retrieves LinkedIn URLs and employee counts for a list of companies provided in a CSV file. It utilizes the googlesearch-python library to find LinkedIn URLs through Google search and playwright for web scraping to extract employee counts from LinkedIn company pages.

## Prerequisites

1. **Install Python:** Ensure you have Python installed on your machine.

2. **Install Playwright:** Ensure you have Playwright installed on your machine.

2. **Install Dependencies:** Use the following command to install the required dependencies:

```bash
pip install pandas googlesearch-python playwright
```

2. **Install Playwright:** Use the following command to install Playwright:

```bash
playwright install
```

## Usage

### Input CSV File

1. Prepare a CSV file (input_companies.csv) containing a column named "Company" with the names of the companies you want to search for.
(or use the default version of this repository)

### Run the Script

1. Execute the script by running the following command:

```bash
python script.py
```

### Output CSV File

1. The script will generate an output CSV file (output_companies.csv) with the LinkedIn URLs and employee counts (if available) for the corresponding companies.

## Important Notes

1. Ensure your input CSV file is correctly formatted with a column named "Company" containing the names of the companies.

2. This script relies on Google search to find LinkedIn URLs, so an internet connection is required during execution.

## What's Next?

While the current script provides basic functionality, there are opportunities for further enhancement:

### Error Handling

Implement robust error handling to manage potential issues during web scraping or Google searches. This includes handling network errors, page load failures, or changes in the HTML structure of LinkedIn pages.

### Concurrency

Explore options for introducing concurrency to improve the script's performance, especially when dealing with a large number of companies. This can be achieved using libraries like asyncio or concurrent.futures to make multiple requests concurrently.

### User Interaction

Consider adding user interaction features, such as a progress bar or logging, to provide better feedback during script execution. This enhances the user experience and helps in troubleshooting any issues.

### Customization Options

Allow users to customize the script behavior, such as specifying the number of search results to consider or adjusting timeouts for web scraping.

### Testing

Implement unit tests to ensure the script's reliability and maintainability. This is crucial, especially if the script evolves or if additional features are added in the future.

### GUI Implementation

Create a graphical user interface (GUI) to make the script more accessible to users who are not comfortable with the command line. Tools like tkinter in Python can be used for this purpose.

### Expand Data Retrieval

Consider adding functionality to extract additional information from LinkedIn, such as company descriptions, locations, or other relevant details.