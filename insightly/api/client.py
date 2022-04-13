from contextlib import AbstractContextManager
import time
from django.conf import settings
import requests
from requests import exceptions
import base64
import json

class Session(AbstractContextManager):

    API_BASE_URL = 'https://api.na1.insightly.com/v3.1/'

    def __init__(self, insightly_api_key=settings.INSIGHTLY_API_KEY):
        self.session = requests.Session()
        self.session.auth = self.basic_auth(insightly_api_key)

    def basic_auth(self, api_key):
        # Login equals to API Key with an empty password as per
        # Insightly API documentation.
        login = api_key
        password = ''
        return requests.auth.HTTPBasicAuth(login, password)

    def url(self, uri):
        return f'{self.API_BASE_URL}{uri}'

    def __exit__(self, exc_type, exc, tb):
        self.session.close()

    def request(self, method, uri, **kwargs):
        repeat = kwargs.pop('repeat', 3)
        try:
            with self.session.request(method, self.url(uri), **kwargs) as resp:
                from json.decoder import JSONDecodeError
                try:
                    return resp.json()
                except JSONDecodeError as error:
                    i = 2
                    import pdb
                    pdb.set_trace()
                    i = 3
        except exceptions.HTTPError as error:
            if error.status == 429:  # "Too Many Requests" error
                if repeat > 0:
                    time.sleep(20)  # Wait a bit and repeat.
                    kwargs['repeat'] = repeat - 1
                    return self.request(method, uri, **kwargs)
            raise

    def get(self, uri, params=None):
        skip = 0
        top = 500
        result = []
        while True:
            items = self.request(
                'GET', f'{uri}?skip={skip}&top={top}', params=params)
            if items:
                skip += top
                result.extend(items)
            else:
                break
        return result

    def post(self, uri, json=None):
        return self.request('POST', uri, json=json)

    def put(self, uri, json=None):
        return self.request('PUT', uri, json=json)

    def delete(self, uri):
        return self.session.request('DELETE', self.url(uri))

    def get_projects(self):
        return self.get('/Projects')

    def get_pipelines(self):
        return self.get('/Pipelines')

    def get_pipeline_stages(self):
        return self.get('/PipelineStages')

    #def get_pipeline_stages(self):
    #    return self.get('/PipelineStages')

    def get_project_categories(self):
        return self.get('/ProjectCategories')
    
    def get_users(self):
        return self.get('/Users')

if __name__ == '__main__':
    with Session() as ses:
        ses.get_projects()
