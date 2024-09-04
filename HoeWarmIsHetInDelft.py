import httpx
from bs4 import BeautifulSoup

WEATHER_URL = "https://weerindelft.nl/WU/55ajax-dashboard-testpage.php"


def getHtmlSoup(url: str) -> BeautifulSoup:
    """Fetches html from the given url and returns the parsed HTML

    Makes a blocking HTTP request for HTML then returns it in a BeautifulSoup parser
    """

    transport = httpx.HTTPTransport(retries=3)
    client = httpx.Client(transport=transport)
    try:
        raw_html = client.get(url).text
    except Exception as e:
        print(
            f"Caught {type(e)}: {e}\n",
            "Unable to retrieve weather information at this time.",
        )

    return BeautifulSoup(raw_html, "html.parser")


def getTemperatureFromHTML(html_soup: BeautifulSoup) -> float:
    """Extracts temperature string from HTML

    Uses css selectors to find <span id="ajaxtemp"> containing current temperature
    then strips whitespace and extraneous characters

    Returns current temperature with original precision as a float
    """
    ajax_temperature = html_soup.css.select_one("span#ajaxtemp").text
    temperature = ajax_temperature.strip().rstrip("°C")
    return float(temperature)


def getRoundedTemperature(temperature: float) -> str:
    """Returns string with rounded temperature"""
    return f"{round(temperature)} degrees Celsius"


def main() -> None:
    weather_soup = getHtmlSoup(WEATHER_URL)
    current_temp = getTemperatureFromHTML(weather_soup)
    rounded_temp = getRoundedTemperature(current_temp)
    print(rounded_temp)


if __name__ == "__main__":
    main()
