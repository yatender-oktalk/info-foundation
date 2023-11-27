file1 = open("MyFile.txt", "w") 
file1.write("Hello \n")
file1.close()
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file2 = open(r"D:\Text\MyFile2.txt", "w+") 