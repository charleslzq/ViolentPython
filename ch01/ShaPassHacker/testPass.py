# import crypt
import hashlib


def test_pass(crypt_pass) :
    # salt = crypt_pass[0:2]
    dic_file = open('dictionary.txt', 'r')
    for word in dic_file.readlines():
        word = word.strip('\n')
        # crypt_word = crypt.crypt(word, salt)
        crypt_word_sha = hashlib.sha512(word.encode('utf-8'))
        if crypt_word_sha.hexdigest() == crypt_pass:
            print("[+] Found Password: " + word + "\n")
            return
    print("[-] Password Not Found.\n")
    return


def main():
    pass_file = open('passwords.txt')
    for line in pass_file.readlines():
        if ":" in line:
                user = line.split(':')[0]
                crypt_pass = line.split(':')[1].strip(' ')
                print(crypt_pass)
                test_pass(crypt_pass)


if __name__ == "__main__":
    main()
