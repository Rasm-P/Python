import os
from memory_profiler import profile

@profile
def read_complete(path):
    with open(path) as fp:
        return fp.readlines()

#if not os.path.isfile('unisex_navne.xls'):
#        os.system('curl -O unisex_navne.xls https://ast.dk/_namesdb/export/names?format=xls&gendermask=4')
#read_complete('unisex_navne.xls')

read_complete('Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.csv')