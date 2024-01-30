import os
import sys
import requests
import tarfile
from tqdm import tqdm
import gzip
import shutil
from collections import defaultdict
from operator import itemgetter

def download_architecture_contents_file(architecture):
    #Hardcoding the debian mirror url as provided, if the mirror url has to be changed, below variable has to be modified accordingly
    debian_mirror_url = "http://ftp.uk.debian.org/debian/dists/stable/main/"
    architecture_contents_url = f"{debian_mirror_url}/Contents-{architecture}.gz"
   
    try:
        # Raises an HTTPError for bad responses (e.g., 404, 500)
        response = requests.get(architecture_contents_url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        # Setting up tqdm to display the progress bar
        tqdm_download_bar = tqdm(total=total_size, unit='B', unit_scale=True)

        with open(f"Contents-{architecture}.gz", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    tqdm_download_bar.update(len(chunk))

        tqdm_download_bar.close()

        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading Contents file: {e}")
        return False

        
def extract_architecture_contents_file(architecture):
   
   
    try:
        if not os.path.exists(contents_file_path):
            print(f"Error: File not found: {contents_file_path}")
            return

        # Create a new file with the same name without the ".gz" extension
        contents_file_name = contents_file_path.replace(".gz", "")

        with gzip.open(contents_file_path, 'rb') as f_in, open(contents_file_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

        print(f"Successfully decompressed {contents_file_path} to {contents_file_name}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def parse_architecture_contents_file(file_path):
    package_files_count = defaultdict(int)

    try:
        with gzip.open(file_path, "rt", encoding="utf-8", errors="ignore") as f:
            for line in f:
                parts = line.strip().split(" ")
                if len(parts) > 1:
                    package = parts[1]
                    if package:
                        package_files_count[package] += 1
    except Exception as e:
        print(f"Error parsing Contents file: {e}")

    return package_files_count

def display_architecture_top_packages(package_files_count):
    sorted_packages = sorted(package_files_count.items(), key=itemgetter(1), reverse=True)

    print("\nTop 10 Packages:")
    for i, (package, count) in enumerate(sorted_packages[:10], start=1):
        print(f"{i}. {package.ljust(25)} {count}")

if __name__ == "__main__":

    #assigning the passed argument to architecture variable
    architecture = sys.argv[1]
    print("=====================================")
    print(f"Downloading the Contents-{architecture}.gz\n")
    print("=====================================")
    if download_architecture_contents_file(architecture):
        #if the content file has been downloaded, function will return True and this block will be executed
        print(f"\n Extracting the contents of Contents-{architecture}.gz")
        
        contents_file_path = f"Contents-{architecture}.gz"
        extract_architecture_contents_file(architecture)
        print("=====================================")
        
        print("\nCounting the files and resp packages")        
        package_files_count = parse_architecture_contents_file(contents_file_path)
        print("\n")
        print("=====================================")
        display_architecture_top_packages(package_files_count)
        print("=====================================")
