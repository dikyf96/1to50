from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL of the car rental service
driver.get('https://rentalservice.com/') #example url

# Select Cars Product
driver.find_element(By.ID, 'cars_product').click()

# Select tab Without Driver
driver.find_element(By.ID, 'without_driver_tab').click()

# Select Pick-up Location
driver.find_element(By.ID, 'pickup_location').send_keys('Jakarta')

# Select Pick-up Date & Time
driver.find_element(By.ID, 'pickup_date_time').send_keys('today+2d 09:00')

# Select Drop-off Date & Time
driver.find_element(By.ID, 'dropoff_date_time').send_keys('today+5d 11:00')

# Click button Search Car
driver.find_element(By.ID, 'search_car_button').click()

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'car_results')))

# Select Car
driver.find_element(By.ID, 'select_car').click()

# Select Car Provider
driver.find_element(By.ID, 'select_provider').click()

# Click button Continue in Product Detail
driver.find_element(By.ID, 'continue_button').click()

# Select Pick-up Location in “Rental Office”
driver.find_element(By.ID, 'pickup_location_rental').send_keys('Rental Office')

# Select Drop-off Location in “Other Location”
driver.find_element(By.ID, 'dropoff_location_other').send_keys('Other Location')

# Click button Book Now
driver.find_element(By.ID, 'book_now_button').click()

# Fill Contact Details
driver.find_element(By.ID, 'contact_details').send_keys('Your Contact Details')

# Fill Driver Details
driver.find_element(By.ID, 'driver_details').send_keys('Your Driver Details')

# Click Continue
driver.find_element(By.ID, 'continue_button').click()

# Check all rental requirements
driver.find_element(By.ID, 'rental_requirements').click()

# Click Continue
driver.find_element(By.ID, 'continue_button').click()

# Select payment method and proceed payment
driver.find_element(By.ID, 'payment_method').click()
driver.find_element(By.ID, 'proceed_payment').click()

# Close the WebDriver
driver.quit()