import requests
import json

game_title = input("Enter the game title to search: ")

# p = dict(q=game_title)
p = {
    "q": game_title
}
url = "https://game.51.com/search/action/game/"
response = requests.get(url, params=p)
response.encoding = "utf-8"

page_html = response.text
print(f"Page HTML Type: {type(page_html)}")
print(f"Page HTML Content (first 500 chars): {page_html[:500]}")
print("Search completed.")

with open("demo/htm/51搜索结果.html", "w", encoding="utf-8") as file:
    file.write(page_html)
    print("Search results written to demo/htm/51搜索结果.html")
