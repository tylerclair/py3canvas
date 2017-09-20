import requests
base_url = 'https://canvas.instructure.com/doc/api'
url = 'https://canvas.instructure.com/doc/api/api-docs.json'
apis = requests.get(url)
processed_apis = apis.json()
for endpoint in processed_apis['apis']:
    endpoint_url = '{}{}'.format(base_url, endpoint['path'])
    endpoint_filename = endpoint['path'][1:]
    endpoint_file = requests.get(endpoint_url)
    endpoint_json = endpoint_file.text
    with open(endpoint_filename, 'w') as file:
        file.write(endpoint_json)
