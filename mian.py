import requests
import json
import pprint

api_key        = 'RGAPI-a7729f27-ee03-4d3d-80d3-417c66c8013c'
user_id        = 'vB46JXdkUPRe5WVipCebot2hDAF8NWJdTFKaWMQw8BYlcis-bHj9NA1kAg'                     # id        
user_accountId = 'dmVkPdwB2Uy-hrc4diezWkT6KCrOUIwQ4HRXSyO-4riFs2kOxJUMUvDP'                       # accountId 
user_puuid     = 'P8rkPEwgy3n4wyMLW8rOTBdrVSTVODePUGxWj1uKWrOYEvdmymzBHnL3H6TVI7SPPhJ-ZdFbg0f5dQ' # puuid     
base_url       = 'https://kr.api.riotgames.com'

def requestAPI(url):
    headers = {
        'X-Riot-Token': 'RGAPI-a7729f27-ee03-4d3d-80d3-417c66c8013c'
    }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)

def main():
    url = base_url + '/lol/league/v4/entries/by-summoner/' + user_id

    result = requestAPI(url)
    pprint.pprint(result, indent=2)

    url = base_url + '/lol/match/v4/matchlists/by-account/' + user_accountId

    result = requestAPI(url)
    pprint.pprint(result, indent=2)

main()

