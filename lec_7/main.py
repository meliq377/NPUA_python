def open_user_file():
    filename = input("please enter correct filename: ")
    try:
        file_obj = open(filename, mode='r')
        print(file_obj.read())
    except:
        print("FileNotFoundError")
    

open_user_file()