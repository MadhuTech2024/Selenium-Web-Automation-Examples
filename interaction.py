from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set up Chrome options to keep the browser open after script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start the Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

try:
    # Wait for the search box to be clickable
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "search"))
    )
    # Enter "python" and press ENTER
    search_box.send_keys("python", Keys.ENTER)
except Exception as e:
    print(f"An error occurred: {e}")

# Optionally, you can close the driver at the end
# driver.quit()