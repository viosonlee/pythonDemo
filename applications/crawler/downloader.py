import pathlib

import requests


def download_file(url, file_path):
    path = pathlib.Path(file_path)
    if path.exists() and path.is_file():
        print("%s已存在" % file_path)
    else:
        r = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(r.content)
        f.close()
