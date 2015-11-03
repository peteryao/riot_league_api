import requests
import json
import httplib

class RiotClient:
    root = "https://na.api.pvp.net"
    apikey = None

    def __init__(self,apikey):
        self.apikey=apikey

    def match(self, region, match_id):
        url = self.root+'/api/lol/{}/v2.2/match/{}'.format(region, match_id)
        response = self.api_get(url)

        return response

    def summoner_name(self, region, summoner_name):
        url = self.root+'/api/lol/{}/v1.4/summoner/by-name/{}'.format(region, summoner_name)
        response = self.api_get(url)

        return response

    def summoner_recent_match(self, region, summoner_id):
        url = self.root + '/api/lol/{}/v1.3/game/by-summoner/{}/recent'.format(region, summoner_id)
        response = self.api_get(url)

        return response

    def summoner_match_list(self, region, summoner_id):
        url = self.root + '/api/lol/{}/v2.2/matchlist/by-summoner/{}'.format(region, summoner_id)
        response = self.api_get(url)

        return response

    def champion(self, region):
        url = self.root+'/api/lol/{}/v1.2/champion'.format(region)
        response = self.api_get(url)

        return response

    def static_item(self, item_id):
        url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/{}'.format(item_id)
        response = self.api_get(url)

        return response

    def api_post(self, url, data={}):
        data['api_key'] = self.apikey
        response = requests.post(url, params=data)
        print response.url

        return response

    def api_get(self, url, data={}):
        data['api_key'] = self.apikey
        response = requests.get(url, params=data)
        print response.url

        return response