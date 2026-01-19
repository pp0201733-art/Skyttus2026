# 1. Read a file and display its contents
f = open("demo.txt", "r")
print(f.read())
f.close()

# 2.Count number of lines in a file

f = open("demo.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
f.close()

# 3. Count word occurrences in a file

f = open("demo.txt", "r")
text = f.read().split()
count = {}

for word in text:
    count[word] = count.get(word, 0) + 1

print(count)
f.close()

# 4. Write 5 user sentences to a file

f = open("sentences.txt", "w")

for i in range(5):
    s = input("Enter sentence: ")
    f.write(s + "\n")

f.close()

# 5. Append strings to an existing file

data = ["Apple", "Banana", "Mango"]

f = open("fruits.txt", "a")
for item in data:
    f.write(item + "\n")
f.close()

# 6. Print lines with a specific word

f = open("demo.txt", "r")
word = "Python"

for line in f:
    if word in line:
        print(line)
f.close()

# 7. Replace a word in a file

f = open("demo.txt", "r")
data = f.read()
f.close()

data = data.replace("Python", "Java")

f = open("demo.txt", "w")
f.write(data)
f.close()

# 8. Merge two text files

f1 = open("demo.txt", "r")
f2 = open("demo2.txt", "r")
f3 = open("merge.txt", "w")

f3.write(f1.read())
f3.write(f2.read())

f1.close()
f2.close()
f3.close()

# 9. Read and display a CSV file

import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
# 10. Back up a file by copying content

f1 = open("demo.txt", "r")
f2 = open("backup.txt", "w")


f2.write(f1.read())
print("File backup Sucssefully")

f1.close()
f2.close()