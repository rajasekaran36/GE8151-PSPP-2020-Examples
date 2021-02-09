import os
units = [file for file in os.listdir(os.curdir) if os.path.isdir(file)]
units.remove('.git')
units.remove('.upm')
units.sort()
print("\nU.No\t:","\tUnit")
print("-----------------------")
for i in range(len(units)):
    print(i+1,"\t\t:\t",units[i])
print("-----------------------")
unitnumber = int(input("Enter unit number:"))
os.chdir(units[unitnumber-1])
files = os.listdir(os.curdir)

files.sort()
print("\nE.No\t:","\tExample")
print("-------------------------------------------")
for i in range(len(files)):
    print(i+1,"\t\t:\t",files[i])
print("-------------------------------------------")
fileno = int(input("Enter Example number to run:"))
print("\n"+files[fileno-1])
print("-------------------------------------------\n")
print(">>>>>>>\n")
os.system("python "+files[fileno-1])
print("\n<<<<<<<")
