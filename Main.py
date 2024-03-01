import os
import requests
import random
import hashlib
from pathlib import Path

def cut_by_filter(line_processed: str="", filter: str="", splitter: str='"'):
    returning = []
    for line in line_processed.split(splitter):
        if filter not in line: continue
        returning.append(line)
    return returning

def add_two_arrays(array1: list=[], array2:  list=[]) -> list:
    for item  in array2:
        if item == "" or item == []: continue
        array1.append(item)
    return array1

def remove_chars(main_string: str="", substitute: str=".", substitute_with: str="[x]"):
    while substitute in main_string: 
        main_string = main_string.replace(substitute,substitute_with)
    return substitute

def rip_http(html_page_filepath: str=""):
    with open("index.html") as file:
        output = file.read().split("\n")

    filters = ['./', "http://", "https://"]

    array_return =  []

    for line in output:
        for one_filter in filters:
            if one_filter in line: 
                array_return = add_two_arrays(cut_by_filter(line, one_filter),array_return)

    for arr in set(array_return): print(arr)


def list_all_file_paths(directory):
    base_path = Path(directory)
    file_paths = [str(file) for file in base_path.rglob('*') if file.is_file()]
    return file_paths


class Integrity:
    def __init__(self,path_passed):
        self.filepath = path_passed

    def md5(self):
        hash_md5 = hashlib.md5()
        with open(self.filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def sha256(self):
        hash_sha256  = hashlib.sha256()
        bytearr  = bytearray(128*1024)
        memview = memoryview(bytearr)
        with open(self.filepath, 'rb', buffering=0) as file:
            for n in iter(lambda : file.readinto(memview), 0):
                hash_sha256.update(memview[:n])
        return hash_sha256.hexdigest()

    def filesize(self):
        st = os.stat(self.filepath)
        return st.st_size

    def all(self) -> list:
        return [ self.md5(), self.sha256(), self.filesize(), self.filepath]



for path in list_all_file_paths('/home/smartwatch/Documents/'):
    integ1 = Integrity(path)
    print(integ1.all())


class Test:
    def __init__(self):
        print("\n\nTesting Started:")
    def error_print(self, exception_passed):
        print( f"\n[[ERROR]]: {exception_passed}\n")
    def verify_results(self,  result):
        if result ==  False: return "Failed"
        elif result == True: return "Passed"
        else:  return "Undefined"

    def integrity_check(self):
        test = '<img class="mobileMode" role="presentation" pngsrc="https://secure.234234.fasdfafdadsfadfadf-p.local/ests/2.1.1.16/content/images/53.png?x=sdfgsd5dt" svgsrc="https://s.aadcdn.microsoftonline-p.local/ests/2.1.8.16/content/images/323.svg?x=12" data-bind="imgSrc" src="./Sign 23 to your account_files/zz.svg">'
        known_hash = ['3d878281884ed4631a32245ba168519c', '97e44e32de4fa0bf47ccb5cd70634c660f843a6a6ad3614362bbcf43032667a3', 307, 'testing_hash.txt']
        try:
            random_integer = random.randint(0,999_999_999_999)
            os.system("echo '"+test+ f"' > testing_hash{random_integer}.txt")
            test_hash = Integrity("testing_hash.txt").all()
            os.system(f"rm testing_hash{random_integer}.txt")
        except Exception as ex:
            test_hash = ""
            print(ex)


        result = self.verify_results(known_hash ==test_hash)
        print(f"[ {result} ]\tIntegrity check")

#Test().integrity_check() 

class Downloader:
    def __init__(self, url:str="", agent:str=""):
        self.url_passed = url
        if agent == "": agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4"
        self.user_agent  = agent

    def wget_r(self, output_folder:str="") -> bool:
        self.url_passed= remove_chars(self.url_passed, '"', "%22")
        try:
            command_part = ""
            if output_folder != "": 
                os.system(f'mkdir {output_folder}')
                command_part = f'cd "{output_folder}";'
            os.system(f'wget -r "{self.url_passed}" ')#-U "{self.user_agent}"

            return True
        except Exception as ex:
            print(ex)
            return False
    def download_page(self, page_download_location) -> bool:
        try:
            headers={self.user_agent}
            response= requests.get(url_passed.strip(), headers=headers, timeout=10)
            open(page_download_location, 'wb').write(response.content)
            return True
        except Exception as ex:
            print(ex)
            return False

Downloader("http://example.com/").wget_r()

# Unfinished project lol
