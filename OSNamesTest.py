import requests

BASE = "https://api.os.uk/search/names/v1/"
KEY = "8sxgVXPjDNz4gW6FtBaATGVgqdWBqAEQ"


def find(search_term, feature):
    find_uri = BASE + "find?query=" + search_term + "&key=" + KEY
    response = requests.get(find_uri)
    data = response.json()
    for results in data["results"]:
        print(results)
        if results["GAZETTEER_ENTRY"]["LOCAL_TYPE"] == feature:
            return search_term + " has a " + feature
    return search_term + " does not have a " + feature


if __name__ == "__main__":
    print(find("Portsmouth", "Harbour"))
