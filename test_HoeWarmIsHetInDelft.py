from bs4 import BeautifulSoup
from HoeWarmIsHetInDelft import WEATHER_URL, getHtmlSoup, getTemperatureFromHTML


def test_weather_data() -> None:
    weather_soup = getHtmlSoup(WEATHER_URL)
    assert type(weather_soup) is BeautifulSoup


def test_html_extraction() -> None:
    with open("test_data.html", "r") as f:
        html = f.read()
    temperature = getTemperatureFromHTML(html)
    assert temperature is not None
