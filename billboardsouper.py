"""Scraping Billboard Top 100"""
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


class BillboardScraper:
    """
    A class that scrapes Billboard top 100 data.
    """
    def __init__(self, year):
        self.year = year
        self.target_date = None
        self.target_url = self.create_link_to_page(year)
        self.song_list = self.get_music_titles()

    def create_link_to_page(self, year):
        """
        Returns a link to the billboard page for the given year.
        """
        today = datetime.today()
        day, month = today.day, today.month
        self.target_date = datetime.strptime(f'{day}/{month}/{year}',
                                             '%d/%m/%Y')
        if self.target_date.weekday() == 6:
            self.target_date += timedelta(days=5)
        elif self.target_date.weekday() == 5:
            pass
        else:
            self.target_date += timedelta(days=5 - self.target_date.weekday())

        return f'http://www.billboard.com/charts/hot-100/\
{self.target_date.strftime("%Y-%m-%d")}/'

    def get_billboard_soup(self, url):
        """
        Returns a BeautifulSoup object of the given URL.
        """
        resp = requests.get(url)

        return BeautifulSoup(resp.text, 'html.parser')

    def get_music_titles(self):
        """
        Returns a list of the music titles from Billboard top 100 form the
        given Year.
        """
        url = self.target_url
        print(f'Scraping {url}')
        soup = self.get_billboard_soup(url)
        chart = soup.find('div', class_='chart-results-list')
        rows = chart.find_all('div',
                              class_='o-chart-results-list-row-container')
        song_list = []
        artists = []
        for row in rows:
            song_list.append(row.find("h3", class_="c-title").text.strip())
            result = row.select_one(selector="li .o-chart-results-list__item")
            artists.append(result.find("span", class_="c-label").text.strip())

        return list(zip(song_list, artists))
