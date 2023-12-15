import requests

res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

for objet in res.json()["moves"]:
  
    print(objet["move"]["name"], end="==> ")   
    comp =0
    for methode in objet["version_group_details"]:

        if comp < 1:
            print(methode["move_learn_method"]["name"])
            comp += 1
      


































# print(res.json()["game_indices"])

# for element in res.json()["game_indices"]:
#     print(element["version"]["name"])

# for stat in res.json()["stats"]:
#     print(stat["stat"]["name"])

# for element in res.json()["types"]:
#     print(element["type"]["name"])


# for element in res.json()["moves"]:
#     for methode in element["version_group_details"]:
#         print(methode["move_learn_method"]["name"])
    