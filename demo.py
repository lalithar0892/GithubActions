with open('profit.txt', 'r') as file:
    # read first 3 lines
    for i in range(3):
        print(file.readline().strip())