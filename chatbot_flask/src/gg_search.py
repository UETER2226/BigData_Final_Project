import re
import requests
import pandas as pd

def build_payload(query, start =1, num=10, data_restrict='m1',**params):
    payload = {
        'key':"AIzaSyD5ZuvFYdZxvioaP6OKFNtdAlEgnNehOCs",
        'q':query,
        'cx':"024969196858e485f",
        'start':start,
        'num':num,
        'dateRestrict':data_restrict
    }
    payload.update(params)
    return payload

def make_request(payload):
    response = requests.get('https://www.googleapis.com/customsearch/v1',params=payload)
    if response.status_code != 200:
        raise Exception('Request failed')
    return response.json()
def get_google_search_results(query):
    payload = build_payload(query, num=5)  # Get top 5 results
    response = make_request(payload)
    search_results = []
    
    for item in response.get('items', []):
        search_results.append({
            'title': item.get('title'),
            'link': item.get('link'),
            'snippet': item.get('snippet')
        })
    
    return search_results


