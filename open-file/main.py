with open("textfile.txt", "r") as textfile:
    file_data = textfile.read()
    print(len(file_data.split(" ")))