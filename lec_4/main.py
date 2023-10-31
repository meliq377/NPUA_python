def classify_numbers():
    n = int(input("Enter list size:"))
    first_list = []
    odd_list = []
    evan_list = []
    for i in range(n):
        item = int(input(f'Enter {i} element:'))
        first_list.append(item)
        if item % 2 == 0:
            evan_list.append(item)
        else:
            odd_list.append(item)
    print("Evan Numbers", evan_list)
    print("Odd Numbers", odd_list)
