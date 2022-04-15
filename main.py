import urllib.request

def main():
    words = ['admin', 'contact', 'index']
    website = input('[+] Website URL: ')

    for word in words:
        directories = website + word
        try:
            print(urllib.request.urlopen(directories).getcode())
        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()