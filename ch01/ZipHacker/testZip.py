import zipfile


z_file = zipfile.ZipFile('evil.zip')
pass_file = open('dictionary.txt')
for line in pass_file.readlines():
    password = line.strip('\n')
    try:
        z_file.extractall(pwd=password.encode('utf-8'))
        print('[+] Password=' + password + '\n')
        exit(0)
    except Exception as e:
        pass
