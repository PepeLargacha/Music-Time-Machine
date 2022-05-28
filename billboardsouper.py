"""Scraping Billboard Top 100"""
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


def create_link_to_page(year):
    """
    Returns a link to the billboard page for the given year.
    """
    today = datetime.today()
    day, month = today.day, today.month
    target_date = datetime.strptime(f'{day}/{month}/{year}', '%d/%m/%Y')
    if target_date.weekday() == 6:
        target_date += timedelta(days=5)
    elif target_date.weekday() == 5:
        pass
    else:
        target_date += timedelta(days=5 - target_date.weekday())

    return f'http://www.billboard.com/charts/hot-100/\
{target_date.strftime("%Y-%m-%d")}/'


def get_billboard_soup(url):
    """
    Returns a BeautifulSoup object of the given URL.
    """
    resp = requests.get(url)

    return BeautifulSoup(resp.text, 'html.parser')


def get_music_titles(year):
    """
    Returns a list of the music titles from Billboard top 100 form the
    given Year.
    """
    url = create_link_to_page(year)
    soup = get_billboard_soup(url)
    chart = soup.find('div', class_='chart-results-list')
    rows = chart.find_all('div', class_='o-chart-results-list-row-container')
    song_list = []
    artists = []
    for row in rows:
        song_list.append(row.find("h3", class_="c-title").text.strip())
        result = row.select_one(selector="li .o-chart-results-list__item")
        artists.append(result.find("span", class_="c-label").text.strip())

    return list(zip(song_list, artists))
