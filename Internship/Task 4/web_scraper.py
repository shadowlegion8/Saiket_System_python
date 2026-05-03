import requests
from bs4 import BeautifulSoup
import csv

print("===== Advanced Web Scraper =====")

# User Input URL
url = input("Enter Website URL: ")

# Browser Header
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Request Website
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # ===================================
    # Website Title
    # ===================================
    print("\nPage Title:")
    print(soup.title.string if soup.title else "No Title Found")

    # ===================================
    # Extract Headings
    # ===================================
    print("\n===== Headings =====")
    headings = soup.find_all(["h1", "h2", "h3"])

    for i, heading in enumerate(headings, start=1):
        print(f"{i}. {heading.get_text(strip=True)}")

    # ===================================
    # Extract Links
    # ===================================
    print("\n===== Links =====")

    links = soup.find_all("a", href=True)

    for i, link in enumerate(links[:10], start=1):   # first 10 links
        print(f"{i}. {link['href']}")

    # ===================================
    # Save to CSV
    # ===================================
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Type", "Data"])

        # Save Title
        writer.writerow(["Title", soup.title.string if soup.title else "No Title"])

        # Save Headings
        for heading in headings:
            writer.writerow(["Heading", heading.get_text(strip=True)])

        # Save Links
        for link in links:
            writer.writerow(["Link", link["href"]])

    print("\nData saved successfully in scraped_data.csv")

except Exception as e:
    print("Error:", e)