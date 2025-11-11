import requests
from bs4 import BeautifulSoup

'''
Install Required Libraries: Run pip install requests beautifulsoup4 to install the necessary libraries.

Adjust Selectors: Replace 'div', class_='product', 'h2', class_='product-name', and 'span', class_='product-price' with the actual HTML structure of the target website.

Respect Robots.txt: Check the website's robots.txt file to ensure compliance with its scraping policies.

Dynamic Content: If the website uses JavaScript to load content, consider using a library like Selenium or Playwright.


'''


#class formats:
#names:
#FenderProductTile__CoreText-sc-i6pg8u-9 FenderProductTile__ProductName-sc-i6pg8u-11 PuifI ifIbwu product-name
#prices:
#FenderProductTile__CoreText-sc-i6pg8u-9 FenderProductTile__Price-sc-i6pg8u-10 PuifI hEvWPN

# URL of the website to scrape
url = "https://www.fender.com/collections/electric-guitars"

# Define the HTML element classes or IDs to target
PRODS = 'FenderProductTile__CoreText-sc-i6pg8u-9'  
Name_var = 'FenderProductTile__ProductName-sc-i6pg8u-11'  
Price_var = 'FenderProductTile__Price-sc-i6pg8u-10'  
# Send a GET request to the website

