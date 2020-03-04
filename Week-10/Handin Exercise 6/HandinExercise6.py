import webget
from concurrent.futures import ThreadPoolExecutor

#Ex 1
class NotFoundException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

class Moduel_class:
    #1
    def __init__(self, url_list):
        self.url_list = url_list

    #2
    def download(self, url, filename):
        try:
            webget.download(url, filename)
        except:
            raise NotFoundException('File not found!')
    
    #3
    def multi_download(self, url_list):
        def io_heavy_time_it(list_url):
            for url in list_url:
                print(url)
                try:
                    webget.download(url)
                except:
                    raise NotFoundException('File not found!')
            
        def multithreading(func, args, workers=4):
            with ThreadPoolExecutor(workers) as ex:
                ex.map(func(args))

        multithreading(io_heavy_time_it, url_list)

    #4
    def __iter__(self):
        self.num = 0
        return self

    #5
    def __next__(self):
        if(self.num >= len(self.url_list)):
            raise StopIteration
        self.num += 1
        return self.num

    #6
    def urllist_generator(self):
        num = 0
        while True:
            yield self.url_list[num]
            num += 1

    #7
    def avg_vowels(self, text):
        total_vowls = 0
        for char in text:
            if (char in 'aieouAIEOU'):
                total_vowls += 1
        return len(text) / total_vowls

    #8
    def hardest_read(self):
        dict_hardness = {}
        for file_txt in self.url_list:
            with open(file_txt) as file_object:
                contents = file_object.read()
                dict_hardness[file_txt] = self.avg_vowels(contents)
        return max(dict_hardness)