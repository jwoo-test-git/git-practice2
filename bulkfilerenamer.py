import os

def main():
    i = 0 
    path= input("enter a directory path")
    path1 = path.replace("\"", "/")
    for filename in os.listdir(path1):
        dest = "img" + str(i) + ".jpg"
        source = path + filename
        dest = path + dest
        os.rename(source, dest)
        i += 1

rename = main()

