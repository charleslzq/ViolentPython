import zipfile
from threading import Thread


def extract_file(z_file, password):
    try:
        z_file.extractall(pwd=password.encode('utf-8'))
        print('[+] Password=' + password + '\n')
    except:
        pass


def main():
    z_file = zipfile.ZipFile('evil.zip')
    pass_file = open('dictionary.txt')
    for line in pass_file.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_file, args=(z_file, password))
        t.start()


if __name__ == '__main__':
    main()

