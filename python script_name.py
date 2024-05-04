import requests
from bs4 import BeautifulSoup

# Function to handle the extraction of a single page
def scrape_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

# Specify the URL of the main page you want to start scraping
url = 'YOUR_MAIN_PAGE_URL_HERE'
soup = scrape_page(url)

if soup:
    # Extract and follow all internal links
    links = set(a['href'] for a in soup.find_all('a', href=True) if 'gcaw.com' in a['href'])
    # Specify your desired file path here
    file_path = 'output.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        # Process each link
        for link in links:
            linked_page = scrape_page(link)
            if linked_page:
                # Use 'string' instead of 'text' to comply with new BeautifulSoup usage
                strings = linked_page.find_all(string=True)
                for string in strings:
                    file.write(string.strip() + '\n')
        print("Extended data written to:", file_path)
