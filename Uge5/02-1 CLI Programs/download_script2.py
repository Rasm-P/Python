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
    input_lines = sys.stdin.read().split()
    run(input_lines[1:])