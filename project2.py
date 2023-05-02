import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create table to store data
c.execute('''CREATE TABLE IF NOT EXISTS products
             (name TEXT, price REAL)''')

# URL of the website to scrape
url = '#https://www.example.com/products'

#Send request to the website and get HTML content
response = requests.get(url)
html_content = response.content

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all products on the website
products = soup.find_all('div', {'class': 'product'})

# Loop through each product and extract name and price
for product in products:
    name = product.find('h2').text.strip()
    price = float(product.find('span', {'class': 'price'}).text.strip().replace('$', ''))

    # Insert data into the database
    c.execute("INSERT INTO products VALUES (?, ?)", (name, price))
    conn.commit()

# Close database connection
conn.close()
