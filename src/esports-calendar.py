from bs4 import BeautifulSoup
import requests

def has_data_league(tag):
    return tag.has_attr('data-league')

def list_leagues():
    url = "https://lolesports.com/en-US/schedule"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for tag in soup.find_all(has_data_league):
        print(tag['data-league'])

if __name__=="__main__":
    list_leagues()