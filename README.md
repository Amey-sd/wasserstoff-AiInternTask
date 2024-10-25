# PDF Processing and Summarization Application

This project provides a straightforward yet powerful solution for processing PDFs. It includes functionality for downloading PDFs from a JSON list, extracting text, generating summaries, extracting keywords using TF-IDF, and storing this data in MongoDB. The application also utilizes threading to optimize PDF processing.

## Features

- **PDF Downloading**: Automatically download PDFs from URLs listed in a JSON file.
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
 ┣ 📜 main.py                 # Main application for PDF processing
 ┣ 📜 load_pdfs.py            # Script for downloading PDFs from URLs in JSON
 ┣ 📜 requirements.txt        # Lists dependencies for the project
 ┣ 📜 README.md               # Project documentation
 ┗ 📂 dataset/                # Directory where PDFs and Dataset.json are stored
```

## Usage

### Step 1: Download PDFs

The `load_pdfs.py` script fetches PDFs from URLs stored in `Dataset.json`:

1. Ensure `Dataset.json` (JSON format: `{ "pdf_name": "pdf_url" }`) is located in the `/dataset` directory.
2. Run `load_pdfs.py` to download the PDFs:

   ```bash
   python load_pdfs.py
   ```

### Step 2: Set up MongoDB

1. Start your MongoDB server (adjust connection string as needed).
2. Modify `main.py` if your MongoDB configuration differs.

### Step 3: Process PDFs

After downloading, process the PDFs with `main.py`:

```bash
python main.py
```

### Output

Processed data (summary and keywords) for each PDF is stored in MongoDB.

## Customization

- **Summary Length**: Adjust summary percentage in the `generate_summary` function in `main.py`.
- **Thread Count**: Change the number of concurrent threads by setting `max_workers` in `process_pdfs_in_directory` in `main.py`.

## License

This project is licensed under the MIT License.

---

### Example Output (in MongoDB)

Each document entry in MongoDB includes:
- `pdf_name`: Name of the PDF file
- `summary`: Generated summary of the PDF
- `keywords`: List of extracted keywords
- `processed_at`: Timestamp of processing
