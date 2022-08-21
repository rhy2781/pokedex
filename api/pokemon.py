import json

import requests


def request_and_process_pokemon_data(s):
    api_url = "https://pokeapi.co/api/v2/pokemon/" + s + "/"
    response = requests.get(api_url)
    res = response.json()

    # remove any unwanted data that is too complicated for us to process
    del res["is_default"]
    res["national_id"] = res["order"] # i believe this references the national dex number
    del res["order"]
    del res["game_indices"]
    del res["past_types"]
    return res


def load_data():
    with open("localDatabase.json") as json_file:
        return json.load(json_file)


def main():
    # this will store the entire list of pokemon that we query for
    pokedex = load_data()

    # this will contain the information that we will store about the pokemon
    s = "charmander"
    data = request_and_process_pokemon_data(s)
    pokedex[s] = data


    # file management
    f = open("localDatabase.json", "w")
    dump = json.dumps(pokedex)
    f.write(dump)
    f.close()


if __name__ == "__main__":
    main()
