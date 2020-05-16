# import extract_module as em
# import download_module as dm


import requests

def download_tar(url,name):
    print("Downloading Started")
    r = requests.get(url, allow_redirects=True)
    print("Successfully Downloaded")
    open(name, 'wb').write(r.content)

# print("Downloaded_module successfully called")

#Program for extracting all items of a file and putting in a folder called output.
import tarfile as tf
import os

def extract_tar(name):
    print("Extracting Started of {}".format(name))
    a = tf.open(name)
    output_name = "./Output-check/extracted" + os.path.splitext(name)[0]
    a.extractall(output_name)
    a.close()
    print("Extracting Finished")

# print("imported extract_modules_successfully")



def main():

    download_tar("http://www.shallalist.de/Downloads/shallalist.tar.gz","x.tar")
    download_tar("http://dsi.ut-capitole.fr/blacklists/download/blacklists.tar.gz","y.tar")
    download_tar("http://squidguard.mesd.k12.or.us/blacklists.tgz","z.tar")
    extract_tar("x.tar")
    extract_tar("y.tar")
    extract_tar("z.tar")

    

if __name__ == '__main__':
    main()



