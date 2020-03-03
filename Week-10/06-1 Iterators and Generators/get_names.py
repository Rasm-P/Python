from memory_profiler import profile

@profile
def read_linewise(file_name):
    with open(file_name) as fp:
        for line in fp:
            yield line

@profile
def return_all_names(file_name):
    lines = (line for line in open(file_name))
    return lines

if __name__ == '__main__':
    print(read_linewise('Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.csv'))
    print(next(read_linewise('Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.csv')))
    #return_all_names('Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.csv')