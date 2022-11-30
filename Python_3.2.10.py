counties = ["Araphoe", "Denver", "Jefferson"]


#for i in counties:
#    print(i)


# in the code below, if you leave out the index[i] in line 11; ex: counties[i], then it will print out the entire list of counties

#for i in range(len(counties)):
#   print(counties)

# but if you specify counties[i], then it will print each county in the list one time.

#for i in range(len(counties)):
#    print(counties[i])

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.keys():
#    print(county)

#for county in counties_dict.values():
#    print(county)

#for county in counties_dict:
#    print(counties_dict.get(county))

#for key, value in counties_dict.items():
#    print(key, value)

#for county, voters in counties_dict.items():
#    print(county, voters)

#for county, voters in counties_dict.items():
#   print(f"{county} county has {voters:,} registered voters.")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}
               ]

#for county_dict in voting_data:
#    print(county_dict)

#for county_dict in range(len(voting_data)):
#    print(voting_data[county_dict])

# the code below will print all of the values from the list of dictionaries. Notice that it did not print the keys, since we did not specify.

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

# now since we specific keys in the code below in line 58, it will print the keys (but its printing them in a diff line of code from the values)

#for county_dict in voting_data:
#    for value in county_dict.keys():
#        print(value)

#for county_dict in voting_data:
#    print(county_dict['county'])


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}
               ]


# Below is a hard piece of code to write! Remember this when you are in a pinch.

# Remember, you will use dictionary_name["key_name"] to get the value of the key. USe that in {   } to have it in an f-string.

for counties_dict in voting_data:
    print(f'{counties_dict["county"]} county has {counties_dict["registered_voters"]} registered voters.')

    