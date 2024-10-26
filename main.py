from load_pdfs import json_loader
from summarizer import summarizer
import os

user_input = input("Do you want to extract PDFs from a JSON file? (yes/no): ").strip().lower()
if user_input == 'yes':
    json_loader.load()
script_dir = os.path.dirname(__file__)
pdf_folder_path = os.path.join(script_dir, 'dataset')
summarizer.process_pdfs_in_directory(pdf_folder_path)