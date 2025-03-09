import requests

url = 'https://meowfacts.herokuapp.com/'

def get_meow_facts():

    try:

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

        else:
            print(f'Erro no retorno da api: {response.status_code}')

    except Exception as e:
        print(f'Aconteceu algum erro: {e}')

print(get_meow_facts())