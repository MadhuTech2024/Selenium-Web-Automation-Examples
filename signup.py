from selenium import webdriver
from selenium.webdriver.common.by import By     
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# Wait for the input fields to be present
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "fName"))
)   
last_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "lName"))
)
email = WebDriverWait(driver, 10).until(        
    EC.presence_of_element_located((By.NAME, "email"))
)
# Fill in the input fields
first_name.send_keys("John")
last_name.send_keys("Doe")
email.send_keys("madhu@gmail.com")

# Click the submit button
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "form button"))        
)
submit_button.click()