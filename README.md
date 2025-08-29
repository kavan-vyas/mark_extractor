# Mark Extractor

A Python tool that extracts pages containing 2-3 mark questions from biology exam papers (PDFs) and combines them into a single output PDF.

## Overview

This tool is designed to help students and educators quickly identify and extract pages from biology exam papers that contain questions worth 2 or 3 marks. It processes multiple PDF files and creates a consolidated PDF with only the relevant pages.

## Features

- Processes multiple PDF files from a designated folder
- Uses regex pattern matching to identify pages with "2 marks" or "3 marks" text
- Combines matching pages into a single output PDF
- Case-insensitive matching for flexible text recognition
- Provides clear feedback on processing results

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip3 install -r requirements.txt
      ```

## Usage

1. Place your PDF files in the `pdfs/` directory
2. Run the extractor:
   ```bash
   python3 extractor.py
   ```
3. The output file `2-3_mark_pages.pdf` will be created in the project root directory

## Example Project Structure

```
mark_extractor/
├── extractor.py          # Main extraction script
├── pdfs/                 # Input PDF files directory
│   ├── AQA GCSE Biology Higher Paper 2 June 2018.pdf
│   ├── AQA GCSE Biology Higher Paper 2 June 2019.pdf
│   └── ... (other PDF files)
├── 2-3_mark_pages.pdf   # Output file (generated after running for the GCSE Biology papers)
└── README.md            # This file
```

## How It Works

1. The script scans all PDF files in the `pdfs/` directory
2. For each PDF, it extracts text from every page
3. Pages containing text matching the pattern "2 marks" or "3 marks" are identified
4. Matching pages are added to a new PDF document
5. The final consolidated PDF is saved as `2-3_mark_pages.pdf`

## Example Output

```
✅ PDF created: /path/to/mark_extractor/2-3_mark_pages.pdf
```

If no matching pages are found:
```
❌ No pages with 2 or 3 markers found.
```

## Notes

- The tool uses case-insensitive matching
- It looks for variations like "2 marks", "3 marks", "2 mark", "3 mark"
- Only pages with exact matches are included in the output
- The original PDF files remain unchanged

## Good Luck revising and remember:
- "When you eliminate the impossible, whatever remains, however improbable, must be the truth" - Sherlock Holmes σ


## License

This project is open source and available under the MIT License.