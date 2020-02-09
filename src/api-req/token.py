#!
import requests
from config import client_id, client_secret, token_url


def generate_token():
    """Retreive OAuth2 Bearer token."""
    auth = (client_id, client_secret)
    body = {"grant_type": "client_credentials"}
    r = requests.post(token_url, auth=auth, json=body)
    return r.json().get("access_token")
