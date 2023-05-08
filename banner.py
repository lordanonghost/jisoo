import requests
from bs4 import BeautifulSoup
import argparse
def get_website_info(url):
    try:
        # Send a GET request to fetch the HTML content of the website
        response = requests.get(url)
        if response.status_code == 200:
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the website title
            website_title = soup.title.string.strip()

            # Extract the website description
            website_description = soup.find('meta', attrs={'name': 'description'})
            if website_description:
                website_description = website_description.get('content').strip()

            # Extract the website keywords
            website_keywords = soup.find('meta', attrs={'name': 'keywords'})
            if website_keywords:
                website_keywords = website_keywords.get('content').strip()

            # Extract the website headings (h1 to h6)
            website_headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

            # Extract the website links
            website_links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

            # Extract the website images
            website_images = [image.get('src') for image in soup.find_all('img') if image.get('src')]

            # Print the extracted information
            print(f"Website URL: {url}")
            print(f"Website Title: {website_title}")
            print(f"Website Description: {website_description}")
            print(f"Website Keywords: {website_keywords}")
            print(f"Website Headings: {website_headings}")
            print(f"Website Links: {website_links}")
            print(f"Website Images: {website_images}")
        else:
            print(f"Failed to fetch the website content. Status code: {response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred while fetching the website: {error}")
def parse_arguments():
    parser = argparse.ArgumentParser(description='Website Information Tool')
    parser.add_argument('url', help='URL of the website to retrieve information from')
    return parser.parse_args()
args = parse_arguments()
website_url = args.url
get_website_info(website_url)
if name == 'main':
    args = parse_arguments()
    website_url = args.url
    get_website_info(website_url)
