from urllib.request import urlopen
import time,json,os, sys

gr = "\033[1;32m"
rd = "\033[1;31m"
r  = "\033[0m"

def Load(text):
    spin = "|/-\\"
    for i in range(5):
        for i in spin:
            print(text,gr,i,r, end='\r')
            time.sleep(0.1)
            pass
        pass
    print()
    pass

def printd(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
        pass
    pass

def attack():
    ip = input(f"{gr}IP -> {r}")
    url = f'http://ip-api.com/json/{ip}'
    request = urlopen(url)
    data = request.read().decode()
    data = eval(data)
    Load(f"Loading [ {gr}{data['query']}{r} ] :")
    for i in data:
        load = f" {gr}{i:<15}{r} [ {data[i]} ]\n"
        printd(load, 0.001)
        with open('.database.json', 'w') as info:
            json.dump(data, info)
            pass
        pass
    pass

def main():
    attack()
    pass

if __name__ == '__main__':
    main()
    pass
