'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get('https://example.com')

# Wait for the JavaScript to render
time.sleep(5)

# Extract the rendered content
content = driver.find_element(By.ID, 'content-id').text
print(content)

# Close the WebDriver
driver.quit()



#none of ts works lmao
# response = requests.get(url)
my_response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
# Check if the request was successful
if my_response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(my_response.text, 'html.parser')
    
    # Example: Extract product names and prices
    products = soup.find_all('div', class_=PRODS)  # Adjust based on the website's structure
    for product in products:
        name = product.find('h2', class_=Name_var).text.strip()  # Adjust selectors
        price = product.find('span', class_=Price_var).text.strip()  # Adjust selectors
        print(f"Product: {name}, Price: {price}")
else:
    print(f"Failed to retrieve the webpage. Status code: {my_response.status_code}")


import requests
from requests_html import HTMLSession
# Initialize the session
session = HTMLSession()
# Get the page content
response = session.get('https://example.com')
# Render JavaScript
response.html.render()
# Extract the rendered content
content = response.html.find('#content-id', first=True).text
print(content)


'''
import dryscrape
from bs4 import BeautifulSoup



#class formats:
#names:
#FenderProductTile__CoreText-sc-i6pg8u-9 FenderProductTile__ProductName-sc-i6pg8u-11 PuifI ifIbwu product-name
#prices:
#FenderProductTile__CoreText-sc-i6pg8u-9 FenderProductTile__Price-sc-i6pg8u-10 PuifI hEvWPN

# URL of the website to scrape
url = "https://www.fender.com/collections/electric-guitars"

session = dryscrape.Session()
session.visit(url)
response = session.body()
soup = BeautifulSoup(response)
soup.find(id="intro-text")