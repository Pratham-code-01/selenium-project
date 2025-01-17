# Selenium Script to Scroll and Load More Items

This script uses Selenium WebDriver to automate the process of scrolling through a webpage and clicking the 'Load More' button until all items are loaded.

## Prerequisites

1. **Install Python**:
   Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Selenium**:
   Install the Selenium package using pip:
   ```bash
   pip install selenium
   ```

3. **WebDriver**:
   Download the appropriate WebDriver for your browser. For example:
   - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - Ensure the WebDriver is added to your system's PATH.

4. **Set Up the Web Page URL**:
   Replace `https://www.radiustheme.com/demo/wordpress/themes/zilly/` in the script with the URL of the webpage you want to automate.

## Script Overview

### Purpose
The script automates the following tasks:
- Scrolls the webpage to ensure the 'Load More' button is visible.
- Clicks the 'Load More' button to load additional content.
- Repeats the process until all items are loaded.

### Script Logic
1. **Initialization**:
   - Launches the browser using Selenium WebDriver.
   - Opens the specified webpage.

2. **Scrolling and Clicking**:
   - Scrolls down to a specific coordinate (`x = 0`, `y = 1800`) to make the 'Load More' button visible.
   - Locates the 'Load More' button using its XPath.
   - Clicks the button and waits for new content to load.

3. **Exit Condition**:
   - Exits the loop when the 'Load More' button is no longer found.

## How to Run the Script

1. Save the script to a file, e.g., `scroll_load_more.py`.
2. Open a terminal or command prompt in the directory containing the script.
3. Run the script using:
   ```bash
   python zilly.py
   ```

## Notes
- **Adjustments**:
  - Modify the `x` and `y` values in the `driver.execute_script()` method to suit the scrolling behavior of the target webpage.
  - Update the XPath for the 'Load More' button to match the structure of your webpage.
- **Error Handling**:
  - The script gracefully exits when the 'Load More' button is not found.

## Troubleshooting
- Ensure the WebDriver version matches your browser version.
- Verify that the XPath for the 'Load More' button is correct.
- If the script fails to scroll properly, experiment with different `x` and `y` values in the `driver.execute_script()` call.

