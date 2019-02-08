import json
import random
import requests

def main():
    url = "https://goodquotesapi.herokuapp.com/author/george+orwell"

    # a lot could go wrong here, and i'm pretty lazy, so...
    try:
        r = requests.get(url)
        total_pages = json.loads(r.text)["total_pages"]

        params = {'page': random.randint(1, total_pages)}
        r = requests.get(url, params=params)

        quotes = json.loads(r.text)["quotes"]
        random_quote = quotes[random.randint(1, len(quotes))]
        return random_quote["quote"]
    except:
        return "Reality exists in the human mind, and nowhere else."

if __name__ == "__main__":
    print (main())
