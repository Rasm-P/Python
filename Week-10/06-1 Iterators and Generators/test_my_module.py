import get_names

name_file = 'Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.csv'

def take_a_number_return_names(num):
    name_list = get_names.read_linewise(name_file)
    names = list(next(name_list) for n in range(num))
    return names

if __name__ == '__main__':
    print(take_a_number_return_names(5))