import json
import requests
import os

class json_loader:
    def load_json_file(json_path):
        with open(json_path, 'r') as file:
            return json.load(file)
        
    def load():
        script_dir = os.path.dirname(__file__)
        json_file_path = os.path.join(script_dir, 'dataset', 'Dataset.json')
        with open(json_file_path, 'r') as file:
            pdf_links = json.load(file)

        # Function to download a PDF
        def download_pdf(url, filename):
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f'Downloaded: {filename}')
            else:
                print(f'Failed to download: {url}')

        # Iterate through the JSON data and download each PDF
        for pdf_name, pdf_url in pdf_links.items():
            # Construct a valid filename (you may want to adjust this)
            filename = os.path.join('dataset', f'{pdf_name}.pdf')
            download_pdf(pdf_url, filename)
