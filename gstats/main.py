from .fetchers import get_repo_html_url_list
from .utils import get_all_blobs
from .parser import get_loc

def main():
    repo_list = get_repo_html_url_list("AayushK47")

    blobs = get_all_blobs(repo_list)

    get_loc(blobs)

    
            

main()