import requests
import toml

def get_word() -> tuple:
    parsed_toml = toml.load('api.toml')

    response = requests.get(parsed_toml['url']['api'])
    print(parsed_toml)

    if response.status_code == 200:
        return (response.json()[0], (parsed_toml['json']['keys']))