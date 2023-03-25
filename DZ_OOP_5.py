import requests
from pprint import pprint
import yadisk


# Задача 1
def intelligence():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    # print(response)
    # pprint(response.json())
    data = response.json()
    mane_data = []
    for item in data:
        if item['name'] == 'Hulk' or item['name'] == 'Thanos' or item['name'] == 'Captain America':
            mane_data.append((item['name'], item['powerstats']['intelligence']))
    # print(mane_data)

    def sorting(i):
        return i[1]

    mane_data.sort(key=sorting, reverse=True)
    # print(mane_data)
    result = list(mane_data[0])
    print(f'{result[0]} has the highest intelligence - {result[1]}')


if __name__ == '__main__':
    intelligence()


# задача 2

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()
        # pprint(response.json())

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


token = ''
if __name__ == '__main__':
    ya = YandexDisk(token)
    ya.upload_file_to_disk('на Яндекс.диске', 'на компьютере')