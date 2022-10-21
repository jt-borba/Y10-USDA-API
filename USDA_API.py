import requests
import json
food = input("Please input the food you want to search: ")
nutrientNameInput = input("Please input the nutrient you would like to search for. (Capitalize first letter, vitamins are included)")
apiRequest = ("https://api.nal.usda.gov/fdc/v1/foods/search?api_key=RhKK6sLU006eA3yKQVVt5eDGb37mNafpw6Xws0C5&query=" + food)
print (apiRequest)

r = requests.get(
    apiRequest,
)

print("Status Code:", r.status_code)
#https://api.nal.usda.gov/fdc/v1/foods/search?query=bananna&pageSize=2&api_key=RhKK6sLU006eA3yKQVVt5eDGb37mNafpw6Xws0C5
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=1)
    print(text)
foodJSON = r.json()


listOfFoods = foodJSON["foods"]
for food in listOfFoods:
    print(food["description"])
    for nutrient in food["foodNutrients"]:
        if(nutrient["nutrientName"] == nutrientNameInput):
            print(nutrientNameInput + ': ' + str(nutrient["value"]) + str(nutrient["unitName"]))



#print(r.json())
