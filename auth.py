import requests
from urllib.parse import urlparse, parse_qs
import os


s = requests.Session()

url = "https://web-stage.learnin2432.com/auth/Account/Login?ReturnUrl=%2Fauth%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dtoken%2520id_token%26nonce%3D98765%26state%26client_id%3Dstackhawk%26scope%3Dopenid%26redirect_uri%3Dhttps%253A%252F%252Fjwt.ms"
payload = {
    "Email": os.environ.get('EMAIL'),
    "Password": os.environ.get('PASSWORD'),
}

r = s.post(url, data=payload, allow_redirects=True)

tokenUrl = r.url
query = parse_qs(tokenUrl)
token = query['https://jwt.ms#id_token'][0]
os.environ['ID_TOKEN'] = token
