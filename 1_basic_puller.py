import requests
from bs4 import BeautifulSoup

import sys
import bs4 as bs
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import re

# URL of the website containing the PDB files
url = 'https://alphafold.ebi.ac.uk/entry/'

# List of PDB file names (UniProt Id) to be downloaded
pdb_files = ['Q5VSL9', 'A0A6M0PRZ6']

# Loop through the list of PDB files and download each one
for file in pdb_files:
    # Construct the URL for the current PDB file
    pdb_url = url + file

    ###FIND DOWNLOADABLE LINKS####
    # Send a request to the server to get the webpage content
    test_url = 'https://alphafold.ebi.ac.uk/entry/A0A6M0PRZ6'
    response = requests.get(test_url)

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags that contain the download links
    download_links = soup.find_all('a', href=True)

    # Loop through the download links and print their URLs
    for link in download_links:
        print(link['href'])
    
    # Send a request to the server to download the PDB file
    #response = requests.get(pdb_url)
    
    # Save the downloaded PDB file to disk
    # with open(file, 'wb') as f:
    #     f.write(response.content)

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def main():
    page = Page(test_url)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find_all('a', href=True)
    return str(js_test)
#if __name__ == '__main__': main()
js_test = main()

# Define a regular expression pattern to match link-strings ending with ".pdb"
pattern = r"https://alphafold.ebi.ac.uk/files/\S+\.pdb"

# Find all link-strings in the text that match the pattern
links = re.findall(pattern, js_test)



print(links)