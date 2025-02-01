import requests
from bs4 import BeautifulSoup

def scrape_guardian(scrape_html_tag = 'p', url="https://www.theguardian.com/technology/2025/jan/28/donald-trump-china-deepseek-ai-chatbot-shares"):

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f'Failed to retrieve content from \"{url}\".')

    soup = BeautifulSoup(html_content, "html.parser")
    # %%

    texts = soup.find_all(scrape_html_tag)

    return texts

