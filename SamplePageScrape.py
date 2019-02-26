import requests
import bs4

def scrapeGameSheet(gameUrl):
	# res = requests.get(gameUrl)
	res = requests.get('https://dmyha.pucksystems2.com/game/game_sheet/22772996')
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text)
	
	# find stats here
	homeTeam = 'Home team'
	awayTeam = 'Away team'
	
	print('Game between ' + homeTeam + ' and ' + awayTeam)
