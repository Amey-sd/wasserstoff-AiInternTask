# PDF Processing and Summarization Application

This project provides a straightforward yet powerful solution for processing PDFs. It includes functionality for downloading PDFs from a JSON list, extracting text, generating summaries, extracting keywords using TF-IDF, and storing this data in MongoDB. The application also utilizes threading to optimize PDF processing.

## Features

- **PDF Downloading**: Automatically download PDFs from URLs listed in a JSON file (only if required).
- **Text Extraction**: Extracts text from PDFs using `pdfminer`.
- **Summary Generation**: Summarizes documents to 20% of their length with Latent Semantic Analysis (LSA).
- **Keyword Extraction**: Uses TF-IDF vectorization to find keywords.
- **MongoDB Storage**: Stores summary and keywords data in MongoDB.
- **Thread Pool Management**: Limits concurrent threads to 5 for resource efficiency.

## Requirements

Make sure you have the following installed:

- Python 3.7+
- MongoDB
- Required Python packages (install with `requirements.txt`)

### Python Package Installation
To install the necessary packages, run:

```bash
pip install -r requirements.txt
```

## Project Structure

```plaintext
📂 pdf_processing_app/
 ┣ 📜 main.py                 # Main application for pipeline
 ┣ 📜 summarizer.py           # Script for summarizing and storing in MongoDB
 ┣ 📜 load_pdfs.py            # Script for downloading PDFs from URLs in JSON
 ┣ 📜 requirements.txt        # Lists dependencies for the project
 ┣ 📜 README.md               # Project documentation
 ┗ 📂 dataset/                # Directory where PDFs and Dataset.json must be stored
```

## Usage

### Step 1: Set up MongoDB

1. Start your MongoDB server (adjust connection string as needed).
2. Modify `main.py` if your MongoDB configuration differs.

### Step 2: Run file

Run main.py

```bash
python main.py
```
It will ask user if you want to first load pdfs from a json file

### Output

Processed data (summary and keywords) for each PDF is stored in MongoDB, under a new Database.

## Customization

- **Summary Length**: Adjust summary percentage in the `generate_summary` function in `summairzer.py`.
- **Thread Count**: Change the number of concurrent threads by setting `max_workers` in `process_pdfs_in_directory` in `summarizer.py`.

## License

This project is licensed under the MIT License.

---

### Example Output (in MongoDB)

Each document entry in MongoDB includes:
- `pdf_name`: Name of the PDF file
- `summary`: Generated summary of the PDF
- `keywords`: List of extracted keywords
- `processed_at`: Timestamp of processing
