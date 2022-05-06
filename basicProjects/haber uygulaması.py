from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(period="7d")
googlenews.search("TR")
results = googlenews.results()

for x in results:
    print("-"*50)
    print("Title -->", x["title"])
    print("time -->",x["date"])
    print("açıklama -->",x["desc"])
    print("link -->", x["link"])