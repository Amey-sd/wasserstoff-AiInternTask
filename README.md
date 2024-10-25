# PDF Processing and Summarization Application

A simple and efficient PDF processing tool that extracts text, generates summaries, extracts keywords using TF-IDF, and stores the data in MongoDB. This project uses multi-threading for concurrent PDF processing and limits the number of threads to improve performance.

## Features

- **Text Extraction**: Uses `pdfminer` to extract text from PDFs.
- **Summary Generation**: Summarizes documents to 20% of their original length using Latent Semantic Analysis (LSA).
- **Keyword Extraction**: Utilizes TF-IDF vectorization to identify relevant keywords.
- **MongoDB Storage**: Stores processed data (summary and keywords) for future reference.
- **Thread Pool Management**: Limits concurrent threads to 5 for efficient resource handling.

## Requirements

Make sure you have the following installed:

- Python 3.7+
- MongoDB
- Required Python packages (install with `requirements.txt`)

### Python Package Installation
To install the necessary packages, use:

```bash
pip install -r requirements.txt
```

## Project Structure

```plaintext
📂 pdf_processing_app/
 ┣ 📜 main.py                 # Main application file for PDF processing
 ┣ 📜 requirements.txt         # Lists all dependencies for the project
 ┣ 📜 README.md               # Project documentation
 ┗ 📂 dataset/                # Directory containing PDF files to be processed
```

## Usage

### Step 1: Set up MongoDB
1. Start your MongoDB server (adjust connection string as needed).
2. Modify `main.py` to match your MongoDB configuration if necessary.

### Step 2: Add PDFs
Place the PDFs you want to process in the `/dataset` directory.

### Step 3: Run the Application
Run the following command to start the processing:

```bash
python main.py
```

### Output
The processed data (summary and keywords) for each PDF will be stored in your MongoDB database in the specified collection.

## Customization

- **Summary Length**: Adjust the percentage of summary by modifying `generate_summary` function in `main.py`.
- **Thread Count**: Change the number of concurrent threads by adjusting `max_workers` in `process_pdfs_in_directory` function.

## License

This project is licensed under the MIT License.

---

### Example Output (in MongoDB)

Each document entry in MongoDB includes:
- `pdf_name`: Name of the PDF file
- `summary`: Generated summary of the PDF
- `keywords`: List of keywords extracted from the PDF
- `processed_at`: Timestamp of processing
