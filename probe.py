import sys
import requests

def urls(out_files):
    url2 = sys.stdin.read().strip().split()

    good_urls = []
    bad_urls = []

    for url in url2:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                good_urls.append(url)
        except requests.exceptions.MissingSchema:
            bad_urls.append(url)
            continue
        except requests.exceptions.ConnectionError:
            bad_urls.append(url)
            continue

    with open(out_file, 'w') as file:
        file.write('\n'.join(good_urls))
    print(f"Saved url {out_file}")



out_file = 'filtered_urls.txt'

urls(out_file)