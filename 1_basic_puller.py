import sys
import bs4 as bs
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import re
import requests

# URL of the website containing the PDB files
url = 'https://alphafold.ebi.ac.uk/entry/'

# List of PDB file names (UniProt Id) to be downloaded
pdb_files = ['Q5VSL9', 'A0A6M0PRZ6']

###FIND DOWNLOADABLE LINKS####
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

def main(url):
    page = Page(url)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find_all('a', href=True)
    return str(js_test)

# Loop through the list of PDB files and download each one
for file in pdb_files:
    # Construct the URL for the current PDB file
    pdb_url = url + file

    js_test = main(pdb_url)

    # Define a regular expression pattern to match link-strings ending with ".pdb"
    pattern = r"https://alphafold.ebi.ac.uk/files/\S+\.pdb"

    # Find all link-strings in the text that match the pattern
    links = ''.join(re.findall(pattern, js_test))

    print(links)

    # Send a request to the server to download the PDB file
    response = requests.get(links)

    # Save the downloaded PDB file to disk
    with open(file, 'wb') as f:
        f.write(response.content)
