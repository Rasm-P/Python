import sys
import webget


def check_args(arguments):
    return True

def run(arguments):
    if check_args(arguments):
        for argument in arguments:
            webget.download(argument)
    else:
        print('No arguments!')

if __name__ == '__main__':
    run(sys.argv[1:])