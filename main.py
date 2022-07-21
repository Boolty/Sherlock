import os
import webbrowser
from iptrack import iptracker
from encrypt import encrypt, decrypt


def main():
    while True:
        name = 'Sherlock'
        version = '1.1'
        print(f'Version: {version}')
        print(f'Hi, {name} what can i finde for you...')
        f_found = os.listdir()
        print('1=IPTracker \n')
        print('2=Encrypt File \n')
        print('3=De_Encrypt File \n')
        print('4=Open URL_Scan \n')
        print('5=List Files \n')
        print('6=Who.is Scan \n')
        case = input('Number: ')
        if int(case) == 1:
            iptracker()
            print('\n')
        elif int(case) == 2:
            print('Files found: ', f_found)
            filename = input('Filename: ')
            encrypt(filename)
            print('\n')
        elif int(case) == 3:
            print('Files found: ', f_found)
            filename = input('Filename: ')
            key = input('Decrypt_Key_name: ')
            decrypt(filename, key)
            print('\n')
        elif int(case) == 4:
            url = 'https://urlscan.io/'
            webbrowser.open(url, new=0, autoraise=True)
        elif int(case) == 5:
            print('Files found: ', f_found)
            print('\n')
        elif int(case) == 6:
            whois = input('Domain Scan: ')
            url = 'https://who.is/whois/' + whois
            webbrowser.open(url, new=0, autoraise=True)


if __name__ == '__main__':
    main()
