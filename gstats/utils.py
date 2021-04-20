import requests
from bs4 import BeautifulSoup

def scan_tree(repo_html_url):
    soup = BeautifulSoup(requests.get(repo_html_url).text, 'lxml')
    tree_list = list(map(lambda x: x['href'], soup.find_all(class_="js-navigation-open Link--primary")))
    return tree_list

def separate_tree_and_blob(links):
    trees = []
    blobs = []
    for link in links:
        if 'tree' in link.split("/"):
            trees.append("https://github.com/" + link)
        else:
            blobs.append(link)
    return trees, blobs

def get_all_blobs(repo_list):
    trees, blobs = [], []

    for repo in repo_list:
        t, b = separate_tree_and_blob(scan_tree(repo))
        trees.extend(t)
        blobs.extend(b)
    
    while trees != []:
        t, b = separate_tree_and_blob(scan_tree(trees[0]))
        trees.extend(t)
        blobs.extend(b)
        trees.pop(0)
    
    return blobs
