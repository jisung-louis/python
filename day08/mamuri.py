import os

def read_folder(path):
    output = os.listdir(path)
    print(output)
    for item in output:
        # print("아이템 : ", item)
        if os.path.isdir(item):
            print(path + "/" + item)
            read_folder(path + "/" + item)
        else:
            print("파일: ", item)

read_folder(".")