import os

location = r"D:\testing"
detect = "binod"

files = os.listdir(location)

words = []
newfile = []
for file in files:
    if file.endswith(".txt" or ".pdf"):
        newfile.append(file)
        with open(location+ '\\' +file) as f:
            words.extend(f.readlines())

for text in words:
    t = text.split(" ")
    for word in t:
        if word.lower() == detect.lower():
            x = words.index(text)
            print(f"Result : {word}, is in file :{newfile[x]}")