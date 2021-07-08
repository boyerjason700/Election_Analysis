counties = ["Arapahoe","Denver","Jefferson"]

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# count = 7

# while count < 1:

#     print("Hello World")

# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num) 

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)

# for county, voters in counties_dict.items():
#     print((counties_dict[county]) + ' county has ' + [counties_dict(voters0] + ' registered voters')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)