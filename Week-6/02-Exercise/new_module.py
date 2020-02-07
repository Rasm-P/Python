import utils
import Exercise1

folder_path = 'C:/Users/rasmu/Desktop/Python/Week-6/02-Exercise'
out_file = 'out_file.txt'
filenames = Exercise1.read_csv(folder_path+'/'+out_file)
md_list = ['C:/Users/rasmu/Desktop/Python/README.md','C:/Users/rasmu/Documents/github/testPipeline/README.md','C:/Users/rasmu/Documents/github/TestExamExerciseType2/README.md']
md_out_file = 'md_out_file.txt'

if __name__ == "__main__" :
    utils.files_in_subfolders(folder_path, out_file)
    utils.takes_a_path_to_folder(folder_path, out_file)
    utils.list_of_filenames(filenames)
    utils.contains_an_email(filenames)
    utils.takes_list_of_md_files(md_list, md_out_file)