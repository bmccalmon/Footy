#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def download_page(file_name, url):
    print(f"Downloading {url} to {file_name}...")
    response = requests.get(url)
    with open(file_name, "w") as file:
        file.write(response.text)

def download_standings():
    download_page("standings.html", "https://www.skysports.com/premier-league-table")

def parse_standings():
	with open("standings.html") as fp:
		soup = BeautifulSoup(fp, "html.parser")

	teams = soup.find_all(class_="standing-table__cell--name-link")

	standings = list()
	pos = 1
	for team in teams:
		points = soup.find('td', class_='standing-table__cell', attrs={'data-sort-value': f'{pos}'})
		promotion = " "
		if pos <= 4:
			promotion = "C"
		if pos == 5:
			promotion = "E"
		if pos >= 18:
			promotion = "R"
		print(f"{promotion} {pos: <5} {team.text: <25} {points.text}")
		standings.append({"name": team.text, "pos": pos, "promotion": promotion, "points": points.text})
		pos += 1
	
	return standings

def main():
	download_standings()
	standings = parse_standings()

if __name__ == "__main__":
	main()
