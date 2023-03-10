import requests

# URL of the website containing the PDB files
url = 'https://alphafold.ebi.ac.uk/entry/'

# List of PDB file names (UniProt Id) to be downloaded
pdb_files = ['Q5VSL9', 'A0A6M0PRZ6']

# Loop through the list of PDB files and download each one
for file in pdb_files:
    # Construct the URL for the current PDB file
    pdb_url = url + file
    
    # Send a request to the server to download the PDB file
    response = requests.get(pdb_url)
    
    # Save the downloaded PDB file to disk
    with open(file, 'wb') as f:
        f.write(response.content)
