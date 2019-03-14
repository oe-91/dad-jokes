import requests


header = {"Accept": "text/plain"}

def get_me_a_joke():
    try:
        r = requests.get('https://icanhazdadjoke.com', headers=header)
        return(r.text)
    except ValueError as err:
        print("Could not connect to icanhazdadjoke.com: ", err)

