import requests
from bs4 import BeautifulSoup


def scrape_latest_articles():
    url = "https://edition.cnn.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("span", attrs={"data-editable": "headline"})

    article_data = []

    for article in articles:
        title = article.get_text()
        link = article.find_parent("a")["href"]
        data = {"title": {title}, "url": url + link}
        article_data.append(data)
    return article_data[:5]


result = scrape_latest_articles()
print(result)
