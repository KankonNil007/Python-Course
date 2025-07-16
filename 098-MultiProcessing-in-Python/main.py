# MultiProcessing in Pyhthon

import multiprocessing
import requests

def downFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"098-MultiProcessing-in-Python/images/Image{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/500/800"
    images = []

    for i in range(1, 6):
        # downFile(url, i) # Downloads files one by one
        p = multiprocessing.Process(target=downFile, args=[url, i])
        p.start()
        images.append(p)

    for i in images:
        i.join()