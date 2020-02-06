import sys
import getopt

#1
def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line)

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as f_obj:
        for line in lst:
            f_obj.write(line)

def read_csv(input_file):
    each_row = []
    with open(input_file) as f_obj:
        content = f_obj.read().splitlines()

    for line in content:
        each_row.append(line)
    
    return each_row

#2&3
def usage():
    return 'Usage : an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.'

def run(path_to_csv, argument):
    if argument == []:
        print_file_content(path_to_csv)
    else:    
        try:
            opts, args = getopt.getopt(argument, "hf", ["help", "file="])
        except getopt.GetoptError as err:
            sys.exit(2)
        for option, argu in opts:
            if option in ("-h","--help"):
                print(usage())
                sys.exit()
            elif option in ("-f","--file"):
                content_list = read_csv(path_to_csv)
                write_list_to_file(argu, content_list)
            else:
                assert False, "unhandled option"
    
if __name__ == "__main__" :
    run(sys.argv[1],sys.argv[2:])