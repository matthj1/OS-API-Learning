import requests

KEY = "8sxgVXPjDNz4gW6FtBaATGVgqdWBqAEQ"


def find(search_term, feature):
    base = "https://api.os.uk/search/names/v1/"
    find_uri = base + "find?query=" + search_term + "&key=" + KEY
    response = requests.get(find_uri)
    data = response.json()
    for results in data["results"]:
        print(results)
        if results["GAZETTEER_ENTRY"]["LOCAL_TYPE"] == feature:
            return search_term + " has a " + feature
    return search_term + " does not have a " + feature


def to_national_grid(lat_long):
    lat = lat_long[0]
    long = lat_long[1]
    URI = f"http://webapps.bgs.ac.uk/data/webservices/CoordConvert_LL_BNG.cfc?method=LatLongToBNG&lat={lat}&lon={long}"
    lat_long_response = requests.get(URI)
    data = lat_long_response.json()
    return round(data["EASTING"]), round(data["NORTHING"])


def nearest(coords, isBNG):
    if isBNG:
        BNG_coords = coords
    else:
        BNG_coords = to_national_grid(coords)
    URI = f"https://api.os.uk/search/names/v1/nearest?point={BNG_coords[0]},{BNG_coords[1]}&radius=1000&key=" + KEY
    response = requests.get(URI)
    print(response.json())


if __name__ == "__main__":
    #print(find("Portsmouth", "Harbour"))
    to_national_grid((52.342622, -0.074505))
    nearest((52.342622, -0.074505), False)
