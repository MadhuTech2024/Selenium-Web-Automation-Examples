from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Get all upcoming event times and names
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Collect events as a list of dictionaries
events = []
for time_elem, name_elem in zip(event_times, event_names):
    events.append({
        "time": time_elem.text,
        "name": name_elem.text
    })

# Print events in a readable format
for idx, event in enumerate(events, 1):
    print(f"{idx}. {event['time']} - {event['name']}")

# driver.quit()