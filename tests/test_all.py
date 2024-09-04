import pytest
from bs4 import BeautifulSoup
from HoeWarmIsHetInDelft import (
    getHtmlSoup,
    getTemperatureFromHTML,
    getRoundedTemperature,
    main,
)

WEATHER_URL = "https://weerindelft.nl/WU/55ajax-dashboard-testpage.php"
BAD_URL = "https://99fakedelft.com"
HTML_SNIPPET = """
<table width="180" border="0" cellpadding="2" cellspacing="0">
    <tr>
    <td align="center" valign="top" class="data1" style="text-align: center;border: none">
    <span class="ajax" id="ajaxconditionicon2">
        <img src="./ajax-images/ovc.jpg"  
            </td>
    </tr>
    <tr align="center">
    <td align="center" valign="top" class="data1" style="text-align: center;border: none">
        <span class="ajax" id="ajaxthermometer">
                        <img src="thermometer.php?t=2.4°C" alt="Currently 2.4°C, Max: 3.1°C, Min: 2.0°C"
        title="Currently 2.4°C, Max: 3.1°C, Min: 2.0°C" height="170" width="54" /> </span>				</td>
    <td class="data1" style="text-align: center;border: none" valign="middle">
        <span class="ajax" id="ajaxtemp" style="font-size:20px">
        2.4&deg;C				  </span>
        <br/>
        <span class="ajax" id="ajaxtemparrow">&nbsp;</span>
        <br/><br/>
                            <br/><br/>
        Gevoelstemp: <span class="ajax" id="ajaxfeelslike">
            2&deg;C 
        </span>
        <br/><br/>
            </td>
    </tr>
    </table>
"""


def test_getHtmlSoup_returns_html() -> None:
    weather_soup = getHtmlSoup(WEATHER_URL)
    assert type(weather_soup) is BeautifulSoup


def test_getHTMLSoup_timeout() -> None:
    with pytest.raises(Exception):
        getHtmlSoup(BAD_URL)


def test_html_extraction() -> None:
    html = BeautifulSoup(HTML_SNIPPET, "html.parser")
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
