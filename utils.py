from bs4 import BeautifulSoup
import urllib.request as request
import praw
import os
from dotenv import load_dotenv

load_dotenv(".env")

def scrape_info(url):

    page = request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    target = soup.find('h4', class_="news-list-item-title").find('a')
    href = target.get('href')
    title = str(target.contents[0])

    return href, title

def reddit_login():

    r = praw.Reddit(
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="testing..."
    )

    print (os.getenv("REDDIT_USERNAME"))

    print ("Login Successful.")

    return r


def run_bot(base_url, ext):

    r = reddit_login()
    href, title = scrape_info(base_url + ext)
    r.subreddit("test").submit(title, url=base_url+href)