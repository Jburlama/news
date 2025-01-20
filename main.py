import requests
import sqlite3
from datetime import date
import sys

def main():
	conn = sqlite3.connect("news.db")
	cursor = conn.cursor()
	limit = 100

	try:
		if (len(sys.argv) == 1):
			articles = news()
		elif (len(sys.argv) == 2 or len(sys.argv) == 3 or len(sys.argv) == 4):
			q = "technology"
			day = date.isoformat(date.today())
			for i in range(len(sys.argv))[1:]:
				arg, param = sys.argv[i].split("=")
				if (arg == "q"):
					q = param
				elif (arg == "day"):
					day = param
				elif (arg == "limit"):
					limit = int(param)
			articles = news(q, day)
	except ValueError:
		print("USAGE: python3 main.py \n       python3 main.py q=topic day=yyyy-mm-dd")
		return (0)

	data = []
	i = 0
	for article in articles:
		if (i == limit):
			break
		data = [(
			article['source']['name'],
			article['author'],
			article['title'],
			article['description'],
			article['url'],
			article['content'],
			article['publishedAt'].split('T')[0])]

		i += 1
		try:
			print(article["title"])
			cursor.executemany("INSERT INTO 'news' VALUES(?,?,?,?,?,?,?)", data)
		except sqlite3.IntegrityError:
			pass

	conn.commit()
	conn.close()



def news(q="technology", day=date.isoformat(date.today())):
	url = ('https://newsapi.org/v2/everything?'
	       f'q={q}&'
	       f'from={day}&'
	       'sortBy=popularity&'
	       'apiKey=60d8660832a64ac1b204ee671865ed31')
	
	response = requests.get(url)
	json = response.json()
	return json["articles"]


if __name__ == "__main__":
	main()
