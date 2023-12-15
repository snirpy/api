import requests

res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

for move in res.json()["moves"]:
 
    print(move["move"]["name"],"==>", move["version_group_details"][0]["move_learn_method"]["name"])
   
        

        
    



































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
    