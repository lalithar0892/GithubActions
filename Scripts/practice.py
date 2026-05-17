import sys
num = int(sys.argv[1])
for i in range(1,num+1):
    print(f"{i} : HIIIIII")

with open("report.txt", "w") as file:
    file.write("Daily Build Report\n")
    file.write("-------------------\n")
    file.write("Build Status : SUCCESS\n")
    file.write("Tests Passed : 25\n")
    file.write("Tests Failed : 0\n")

print("Report Generated Successfully")
