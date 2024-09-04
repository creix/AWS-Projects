import requests

url = "https://yodish.p.rapidapi.com/yoda.json"

def get_translation(text):
    querystring = {"text": "{}".format(text)}

    headers = {
        "X-RapidAPI-Key": "9e4b0bd666mshd40bed7ca654f99p1146eajsn3fcabc04eedc",
        "X-RapidAPI-Host": "yodish.p.rapidapi.com"
    }

    response = requests.post(url, headers=headers, params=querystring)

    if response.ok:
        data = response.json()
        if 'contents' in data and 'translated' in data['contents']:
            return data['contents']['translated']
    return None

def print_translated_text(text):
    print("Yoda would say: {}\n".format(text))

while True:
    user_text = input("Enter a phrase to translate: ")
    if not user_text == '0':
        response = get_translation(user_text)
        print_translated_text(response)
    else:
        break
