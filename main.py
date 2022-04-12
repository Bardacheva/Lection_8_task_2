import requests
from pprint import pprint

files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
token = ''

class YaUploader:
    '''
    Класс для загрузки файлов на яндекс диск
    '''
    files_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    @property
    def header(self):
        return self.get_headers()

    def get_upload_link(self, file_path: str):
        '''
        Метод получает ссылку для загрузки файла на яндекс диск
        '''
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params, headers=self.header)
        return response.json()

    def upload(self, file_path: str, file_name: str):
        '''
        Метод загружает файлы на яндекс диск
        '''
        href = self.get_upload_link(file_path).get('href')
        if not href:
            return False

        with open(file_name, 'rb') as data:
            response = requests.put(href, data)
            if response.status_code == 201:
                print('Файл загружен')
                return True


ya = YaUploader(token)
ya.upload('file.txt', 'file.txt')


