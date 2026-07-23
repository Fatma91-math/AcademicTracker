from modules.scholar import ScholarScraper


def main():

    scholar = ScholarScraper()

    print("=" * 40)
    print("Academic Tracker")
    print("=" * 40)

    print("Researcher:", scholar.get_name())
    articles = scholar.get_articles()

    print("\nArticles:")

    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['title']}")


if __name__ == "__main__":
    main()
article = {
    "title": "My First Paper",
    "citations": 25,
    "year": 2024
}

print("\nDictionary Test")
print(article)

print(article["title"])
print(article["citations"])
print(article["year"])