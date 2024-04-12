# SCRAPING NBA DATA

"""
Important thing to note: you'll need to create three directories within this project:
 'nba_awards', 'player_stats', 'team_standings'
"""

# import libraries
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup
import time

# creating global variables
seasons = list(range(1997, 2024))


# created function that gets the html
def get_html(url, selector, sleep=5, retries=3):
    """
    :param url: the url for the data we are trying to scrape
    :param selector: the thing we are looking for within the whole html file
    :param sleep: initial amount of pause between scrapes
    :param retries: amount of retries to scrape before we pass error
    :return: the html file scraped from the internet
    """

    # initialize the html
    html_file = None

    # essentially attempt to web scrape with multiple tries
    for i in range(1, retries + 1):
        time.sleep(sleep * i)

        # using playwright to attempt to scrape, but if error is thrown, keep going
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(url)
                print(page.title())
                html_file = page.inner_html(selector)
        except PlaywrightTimeout:
            print(f"Timeout error on {url}")
            continue
        else:
            break
    return html_file


# function which scrapes standings from a given season
def scrape_standings(temp_season):
    """
    :param temp_season: the current indexical season
    :return: writes the standing html file to the team_standing directory for the given season
    """

    # get the url
    nba_url = f"https://www.basketball-reference.com/leagues/NBA_{temp_season}_standings.html"

    # call the get_html function to get the html
    html = get_html(nba_url, "#all_standings")

    # give the html text a name
    html_name = f"NBA_Season_{temp_season}_Standings.html"

    # save file path to the directory
    with open(f"team_standings/{html_name}", "w+") as f:
        f.write(html)


# function which scrapes the player stats from a given season
def scrape_stats(temp_season):
    """
    :param temp_season: the current indexical season
    :return: writes all the stats html files to the player_stats directory for the given season
    """

    nba_url = f"https://www.basketball-reference.com/leagues/NBA_{temp_season}_per_game.html"

    # call the get_html function to get the html
    html = get_html(nba_url, "#content .filter")

    # using BeautifulSoup library
    soup = BeautifulSoup(html)

    # find all the a-tags for the stats pages
    links = soup.find_all('a')
    href = [link['href'] for link in links]
    stats_pages = [f"https://basketball-reference.com{link}" for link in href]

    # save file path to the directory
    for url in stats_pages:

        # get specific type of stat by splitting up the url
        stat_type = (url.split(f"{temp_season}")[-1].split(".")[0])[1:]

        # give the html text a name
        html_name = f"NBA_Season_{temp_season}_{stat_type}.html"

        # get the html files based upon certain restrictions
        if stat_type == "play-by-play":
            stat_selector = "#all_pbp_stats"
        elif stat_type == "adj_shooting":
            stat_selector = "#all_adj-shooting"
        else:
            stat_selector = f"#all_{stat_type}_stats"

        # save html files
        html = get_html(url, stat_selector)
        with open(f"player_stats/{html_name}", "w+") as f:
            f.write(html)


# function which scrapes the nba awards from a given season
def scrape_awards(temp_season):
    """
    :param temp_season: the current indexical season
    :return: writes all the awards html files to the nba_awards directory for the given season
    """

    nba_url = f"https://www.basketball-reference.com/awards/awards_{temp_season}.html"

    # create list of award selectors that I actually want
    award_list = ["all_mvp", "all_roy", "all_dpoy", "all_smoy", "all_mip",
                  "all_leading_all_nba", "all_leading_all_defense"]

    for award_selector in award_list:

        # call the get_html function to get the html
        html = get_html(nba_url, f"#{award_selector}")

        # give the html text a name
        html_name = f"NBA_Awards_{temp_season}_{award_selector}_voting.html"

        # save file path to the directory
        with open(f"nba_awards/{html_name}", "w+") as f:
            f.write(html)


# function which scrapes the rookie list from the latest nba season
def scrape_rookies(temp_season):
    """
    :param temp_season: the current indexical season
    :return: writes the rookie list html file to the project directory
    """

    # create the url
    nba_url = f"https://www.basketball-reference.com/leagues/NBA_{temp_season}_rookies.html"

    # call the get_html function to get the html
    html = get_html(nba_url, "#all_rookies")

    # give the html text a name
    html_name = f"NBA_Season_{temp_season}_Rookies.html"

    # save file path to the directory
    with open(f"{html_name}", "w+") as f:
        f.write(html)


if __name__ == "__main__":

    # loop through each season, scraping the stats, standings, and award voting rankings

    for season in seasons:
        scrape_standings(season)
        scrape_stats(season)
        scrape_awards(season)
    
    # get the updated stats for the 2024 season
    scrape_standings(2024)
    scrape_stats(2024)

    # scrape the rookies list for the 2024 season
    scrape_rookies(2024)
