#!/usr/bin/env python3
"""Alta3 Research | Farm loops"""


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
farms = [
  {
    "name": "NE Farm",
    "agriculture": [
      "sheep",
      "cows",
      "pigs",
      "chickens",
      "llamas",
      "cats"
    ]
  },
  {
    "name": "W Farm",
    "agriculture": [
      "pigs",
      "chickens",
      "llamas"
    ]
  },
  {
    "name": "SE Farm",
    "agriculture": [
      "chickens",
      "carrots",
      "celery"
    ]
  }
]
NE_animals= farms[0]["agriculture"]
for x in NE_animals:
    print(x)

for a_farm in farms:
    print("-",a_farm["name"])
choice= input("Pick a farm!\n")

"""for a_farm in farms:
    if a_farm["name"].lower() == choice.lower():
        for animals in a_farm["agriculture"]:
            print(animals)"""
vegis =["carrots", "celery"]
for a_farm in farms:
    if a_farm["name"].lower() == choice.lower():
        for ag_item in a_farm["agriculture"]:
            if ag_item not in vegis:
                print(ag_item)
