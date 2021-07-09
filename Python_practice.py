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

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# # for county in counties_dict:
# #     print(counties_dict[county])

# # for county in counties_dict:
# #     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)

# for county, voters in counties_dict.items():
#     # print(county + ' county has ' + str(voters) + ' registered voters')
#     print(f"{county} county has {voters} registered voters")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for 
    print(f"{key} county has {value} registered voters")
