#Basic File Operations
#Create a text file notes.txt and write 5 lines into it.
"""
with open("notes1.txt","w",) as f:
    f.write("Line1: Python file operations.\n")
    f.write("Line2: Python file operations.\n")
    f.write("Line3: Python file operations.\n")
    f.write("Line4: Python file operations.\n")
    f.write("Line5: Python file operations.\n")

#Read the file and print all lines.
with open("notes.txt","r") as f:
    print(f.read())

#Read only the first 2 lines from the file.
with open("notes.txt","r") as f:
    notdt=f.readlines()
    print(notdt[:2])

#Count the number of lines in the file.
with open("notes.txt","r") as f:
    notdt=f.readlines()
    print(len(notdt))
#Append a new line "End of Notes" at the end of the file.
with open("notes.txt","a") as f:
    f.write("End of Notes")
"""
"""
#Intermediate Tasks
#Read a file and remove all blank lines before printing.
with open("notes.txt","r") as f:
    notdt=f.readlines()
    notdts=[i.strip() for i in notdt]
    print(notdts)

#Read a file and print each line with line numbers.
#(e.g., 1: This is first line)
with open("notes.txt","r") as f:
    notdt=f.readlines()
    b=0
    for i in notdt:
        b+=1
        print(f"{b}:{i}")
#Copy the contents of one file into another (copy.txt).
with open("notes.txt","r") as f,open("notes2.txt","w") as w:
    notdt=f.read()
    w.write(notdt)
#Write a program to count how many times each word occurs in a file
with open("notes.txt","r") as f:
    notdt=f.read()
    notdts=notdt.split() 
    print(notdts)
    d={}
    for j in notdts:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    print(d)
#Merge the contents of two files (file1.txt, file2.txt) into a new file

# Merge file1.txt and file2.txt into merged.txt
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

# Write into new file
with open("merged.txt", "w") as f3:
    f3.write(data1 + "\n" + data2)

print("Files merged successfully into merged.txt")
"""
#Advanced Tasks
#Write a program to read a CSV file and print only selected columns.
import csv
with open("marks.csv","r") as f,open("marks_output.csv","w") as w:
    reader_markdt=csv.DictReader(f)
    fieldnames = ["Name", "English"]
    writer_markdt=csv.DictWriter(w,fieldnames)
    writer_markdt.writeheader()

    for row in reader_markdt:
        writer_markdt.writerow({col:row[col] for col in fieldnames})

#Read a file and replace a given word with another word. Save result to a new file.
with open("marks.csv","r") as f:
    markdt=f.readlines()
    markdtlst= [i.replace("Alice","Vignesh") for i in markdt]
    print(markdtlst)
#Read a log file and extract only lines that contain the word "ERROR".
with open("log.txt","r") as f:
    markdt=f.readlines()
    for i in markdt:
        if "ERROR" in i:
            print(i)










