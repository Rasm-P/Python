import os
import glob
import Exercise1

#1
def takes_a_path_to_folder(folder_path, out_file):
    lines = [f for f in os.listdir(folder_path) if os.path.isfile(f)]
        
    with open(out_file, 'w') as file_object:
        for line in lines:
            file_object.write(line + '\n')

#2
def find_files_in_all_subfolders(folder_path, ext):
    #lines = glob.glob(folder_path + r'\**\*.py', recursive=True)
        
    subfolders, files = [], []
    for f in os.scandir(folder_path):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
                files.append(f.name)

    for dir in list(subfolders):
        sf, f = find_files_in_all_subfolders(dir, ext)
        subfolders.extend(sf)
        files.extend(f)

    return subfolders, files    

def files_in_subfolders(folder_path, out_file):
    sf, f = find_files_in_all_subfolders(folder_path, [])

    with open(out_file, 'w') as file_object:
        for line in f:
            file_object.write(line + '\n')

#3
def  list_of_filenames(list_filenames):
    for filename in list_filenames:
        if not (filename.endswith('.py')):
            with open(os.path.join(filename)) as f_obj:
                print(f_obj.read().splitlines())

#4
def contains_an_email(list_filenames):
    for filename in list_filenames:
        if not (filename.endswith('.py')):
            with open(os.path.join(filename)) as f_obj:
                for line in f_obj:
                    if '@' in line:
                        print(line)

#5
def takes_list_of_md_files(md_list, md_out_file):
    headers = []
    for md_file in md_list:
        if (md_file.endswith('.md')):
            with open(md_file) as f_obj:
                for line in f_obj:
                    if '#' in line:
                        headers.append(line)

    with open(md_out_file, 'w') as file_object:
        for header in headers:
            file_object.write(header + '\n')

if __name__ == "__main__" :
    folder_path = 'C:/Users/rasmu/Desktop/Python/Week-6/02-Exercise'
    out_file = 'out_file.txt'
    filenames = Exercise1.read_csv(folder_path+'/'+out_file)
    md_list = ['C:/Users/rasmu/Desktop/Python/README.md','C:/Users/rasmu/Documents/github/testPipeline/README.md','C:/Users/rasmu/Documents/github/TestExamExerciseType2/README.md']
    md_out_file = 'md_out_file.txt'

    files_in_subfolders(folder_path, out_file)
    takes_a_path_to_folder(folder_path, out_file)
    list_of_filenames(filenames)
    contains_an_email(filenames)
    takes_list_of_md_files(md_list, md_out_file)