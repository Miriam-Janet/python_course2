filenames = ["files/file1.txt", "files/file2.txt", "files/file3.txt"]

with open("files/new-file.txt", "w") as new_file:
    for name in filenames:
        with open(name) as f:
            for line in f:
                new_file.write(line)
            
            new_file.write("\n")