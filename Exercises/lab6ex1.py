user_input = input("Enter a new member: ")

file = open("../example_files/members.txt", "r")
members = file.readlines()

file.close()

members.append(user_input + "\n")

file = open("../example_files/members.txt", "w")

members = file.writelines(members)
file.close()