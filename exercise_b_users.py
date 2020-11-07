users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# # 3. Get the array of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers

eriks_nums = users["Erik"]["lottery_numbers"]
print(min(eriks_nums))

# 6. Return an array of Avril's lottery numbers that are even

avrils_nums = users["Avril"]["lottery_numbers"]
even_nums = []
for num in avrils_nums:
  if num % 2 == 0:
    even_nums.append(num)

print(even_nums)

"lottery_numbers": [12, 14, 33, 38, 9, 25],

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

eriks_nums.append(7)
print(eriks_nums)

# 8. Change Erik's hometown to Edinburgh

erik_hometown = users["Erik"]["homehome_town"] = "Edinburgh"
print(erik_hometown)

# 9. Add a pet dog to Erik called "Fluffy"

new_dog = {
  "name": "Fluffy",
  "species": "dog"
}

users["Erik"]["pets"].append(new_dog)
print(users["Erik"]["pets"])


# 10. Add another person to the users dictionary

users["ian"] = {
    "twitter": "twitter name",
    "lottery_numbers": [4,5,6,7,8],
    "home_town": "Edinburgh",
    "pets": [
      {
        "name": "Dave",
        "species": "dog"
      }
    ]
}