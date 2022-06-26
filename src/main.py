import urllib.request
from os import path
import datetime

"""
TODO: 
- Recognize Wordpress URL and use wordpress wordlists;
- Use default wordlist if none is inserted;
- Insert https or http if URL doesn't have it;
- Customize output colors;
- Brute-force with more threads; 
"""

def main():
    website = input('[+] Website URL: ')
    words_dir = input('[+] Wordlist path: ')

    print_program_info()

    words = path.realpath(words_dir)

    with open(words) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    for word in lines:
        directory = website + word
        try:
            print(f'[{urllib.request.urlopen(directory).getcode()}]  /{word} ')
        except Exception as error:
            pass

    print(40*"═")
    now = datetime.datetime.now()
    print(f'Successfully concluded at {now.hour}:{now.minute}:{now.second}')
    print(40*"═")
    

def print_program_info():
    print(40*"═")
    print('DBT - v1.1.0')
    print('by Marina Farias (@dilunno)')
    print(40*"═")
    now = datetime.datetime.now()
    print(f'Started at {now.hour}:{now.minute}:{now.second}')
    print(40*"═")
 

if __name__ == '__main__':
    main()