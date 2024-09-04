import pytest
from bs4 import BeautifulSoup
from HoeWarmIsHetInDelft import (
    WEATHER_URL,
    getHtmlSoup,
    getTemperatureFromHTML,
    getRoundedTemperature,
    main,
)


def test_getHtmlSoup_returns_html() -> None:
    weather_soup = getHtmlSoup(WEATHER_URL)
    assert type(weather_soup) is BeautifulSoup


def test_getHTMLSoup_timeout() -> None:
    BAD_URL = "https://99fakedelft.com"
    with pytest.raises(Exception):
        getHtmlSoup(BAD_URL)


def test_html_extraction() -> None:
    with open("test_data.html", "r") as f:
        raw_html = f.read()
    html = BeautifulSoup(raw_html, "html.parser")
    temperature = getTemperatureFromHTML(html)
    assert temperature == 2.4


def test_getRoundedTemperature_down() -> None:
    temp = 2.4
    roundedTemp = getRoundedTemperature(temp)
    assert roundedTemp == "2 degrees Celsius"


def test_getRoundedTemperature_up() -> None:
    temp = 2.6
    roundedTemp = getRoundedTemperature(temp)
    assert roundedTemp == "3 degrees Celsius"


def test_main(capfd) -> None:
    main()
    captured = capfd.readouterr()
    assert captured.out.endswith(" degrees Celsius\n")
