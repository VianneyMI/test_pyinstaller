# Data Processor Application

A Python application for processing and merging CSV and Excel files with data validation.

## Features

- Read and validate CSV and Excel files
- Merge multiple files of the same type (CSV or Excel)
- Data validation using Pydantic models
- User-friendly GUI interface
- Automatic Excel formatting

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. In the application:
   - Click "Add Files" to select CSV or Excel files to process
   - Select an output directory
   - Enter an output filename
   - Click "Process Files" to validate and merge the files

## Data Format

The application expects files with the following columns:
- employee_id (integer)
- name (string)
- email (string)
- department (string)
- salary (float)
- hire_date (date)
- is_active (boolean)
- skills (list of strings)

## Building with PyInstaller

The application uses a custom spec file (`main.spec`) to handle all dependencies correctly, particularly for Pydantic v2 and other packages.

To create a standalone executable:
```bash
pyinstaller main.spec
```

The executable (`DataProcessor.exe`) will be created in the `dist` directory. The spec file includes:
- All necessary hidden imports for Pydantic v2
- Required packages (pandas, openpyxl, tkinter)
- GUI configuration (windowed mode)
- Custom application name

Note: The spec file is already configured with all necessary settings, so there's no need to use additional command-line arguments.

