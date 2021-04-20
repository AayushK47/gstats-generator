import requests

def get_repo_html_url_list(github_username):
    response = requests.get(f"https://api.github.com/users/{github_username}").json()
    response = requests.get(response["repos_url"]).json()
    response = list(map(lambda x: x["html_url"], response))
    return response
