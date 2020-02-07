import os

if __name__ == '__main__':
    full__path = 'C:/Users/rasmu/Documents/Python'
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(full__path):
        for f in filenames:
            if (f.lower().endswith('.png')):
                listOfFiles += [os.path.join(dirpath, f)]
    print(listOfFiles)