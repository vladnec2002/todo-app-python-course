import glob
import csv
import shutil
import webbrowser

myfiles = glob.glob("../files/*.txt")
print(myfiles)

#------------------------

with open("../example_files/weather.csv", "r") as csvfile:
    data = list(csv.reader(csvfile))

print(data)

city = input("Enter city name: ")

for row in data:
    if row[0] == city:
        print(row[1])

#--------------------------

shutil.make_archive("output", "zip", "../files")

#--------------------------

user_term = input("Enter your search term: ").replace(" ", "+")
webbrowser.open_new_tab("https://www.google.com/search?q=" + user_term)