filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(f"../example_files/{filename}", "r")
    print(file.readlines())
    file.close()
