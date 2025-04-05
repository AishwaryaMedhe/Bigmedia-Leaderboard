from .models import MediaOutlet, Article
from .leaderboard import update_outlet_score
import requests
from bs4 import BeautifulSoup

def extract_outlet_name(url):
    return url.split("//")[1].split("/")[0]

def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No title"

    shares = 100  # Simulated
    views = 300  # Simulated
    outlet_name = extract_outlet_name(url)

    outlet, _ = MediaOutlet.objects.get_or_create(name=outlet_name)

    Article.objects.create(
        url=url,
        title=title,
        outlet=outlet,
        shares=shares,
        views=views
    )

    update_outlet_score(outlet, shares+views)



