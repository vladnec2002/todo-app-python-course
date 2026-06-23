contents = ["content 1",
            "content 2",
            "content 3"]

filenames = ["file1.txt", "file2.txt", "file3.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../example_files/{filename}", "w")
    file.write(content)
