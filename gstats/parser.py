import requests


extMap = {
    'py': 'python',
    'ipynb': 'python',
    'js': 'javascript',
    'jsx': 'javascript',
    'tsx': 'typescript',
    'ts': 'typescript',
    'java': 'java',
    'c': 'c',
    'dart': 'dart',
}

def get_loc(blob_list):
    loc = {}
    print(len(blob_list))
    x = 0
    for link in blob_list:
        x += 1
        ext = link.split(".")[-1]
        req_url = link.split('/blob')
        req_url = ''.join(req_url)
        req_url = "https://raw.githubusercontent.com" + req_url
        response = requests.get(req_url)

        if ext == 'ipynb':
            pass
        elif ext in extMap:
            lines = len(response.text.split('\n'))
            if extMap[ext] in loc:
                loc[extMap[ext]] += lines
            else:
                loc[extMap[ext]] = lines
        print(x)
    
    print(loc)