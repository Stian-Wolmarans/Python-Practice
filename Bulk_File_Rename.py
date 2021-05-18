import os

def main():
    i = 0
    path = "Drive:/Filepath/etc/"
    for filename in os.listdir(path):
        destination = "name" + str(i) + ".something"
        source = path + filename
        destination = path + destination
        os.rename(source, destination)
        i += 1

if __name__ == '__main__':
    main()