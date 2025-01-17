import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Handle HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h2')  # Adjust tag/class based on the website
        print("News Headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline.get_text(strip=True)}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

url = input("Enter the URL of the news website: ")
scrape_headlines(url)
