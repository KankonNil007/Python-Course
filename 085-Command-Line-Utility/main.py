# Command Line Utility in Python

import argparse
import requests

def download_file(url, output):
    if output is None:
        local_filename = url.split('/')[-1]
    else:
        local_filename = output
    # the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Enter the url of the file")
parser.add_argument("-o", "--output", help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
download_file(args.url, args.output)


# To use this: Run this on the powershell
# python "python file name with directory" "image link" -o "File name you wanna save as with directory"