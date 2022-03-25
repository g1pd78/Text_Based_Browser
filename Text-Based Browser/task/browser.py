import sys
import requests
import os
from bs4 import BeautifulSoup
from colorama import Fore

headers = {'User-Agent': 'Mozilla/5.0'}
if __name__ == '__main__':
    directory = sys.argv[1]
    if os.access(directory, os.F_OK):
        pass
    else:
        os.makedirs(directory)

    history = []
    while True:
        address = input()
        if address == 'exit':
            break
        elif address == 'back':
            try:
                history.pop()
                address = history.pop()
            except Exception:
                pass
        if 'https://' not in address:
            address = 'https://' + address
        try:
            response = requests.get(address, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            response = soup.find_all('a')
            for x in response:
                x.string = "".join([Fore.BLUE, x.get_text(), Fore.RESET])
            response = soup.get_text()

            history.append(address)
            address = address[8:address.find('.')]
            f = open(directory + '/' + address, 'w', encoding='UTF-8')
            f.write(response)
            f.close()
            print(response)
        except Exception as error:
            print(error)
            print('Error: Incorrect URL')
