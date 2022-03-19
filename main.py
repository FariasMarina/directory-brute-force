import urllib.request


def main():
    website = input('[+] Website URL: ')
    print(urllib.request.urlopen(website).getcode())


if __name__ == '__main__':
    main()