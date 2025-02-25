# PDFCombinerPY from dflopez

Takes PDFs and combines them

## Installation on Windows

### Required Installations

```sh
pip install PyPDF2 reportlab pdf2image Pillow colorama
```
or
```sh
pip install -r requirements.txt
```

#### Download and install Poppler:

1. Go to [Poppler releases](https://github.com/oschwartz10612/poppler-windows/releases).
2. Download the latest version of Poppler for Windows (e.g., `poppler-23.11.0.zip`).
3. Extract the ZIP file into a folder, e.g., `C:\poppler`.
4. Add the Poppler `bin` folder to your environment variable `PATH`:
   - Right-click on "This PC" or "My Computer" and select "Properties".
   - Click on "Advanced system settings".
   - In the "Advanced" tab, click on "Environment Variables".
   - Under "System variables", find the `PATH` variable and click "Edit".
   - Add the path to the Poppler `bin` folder, e.g., `C:\poppler\bin`.
   - Click "OK" to save the changes.

## Installation on macOS

### Required Installations

#### In the script path, run the following commands:
- **Creates a virtual environment for Python**
    ```sh
    python3 -m venv venv 
    ```
- **Activates the virtual environment**
    ```sh
    source venv/bin/activate
    ```
- **Installs the necessary libraries**
    ```sh
    pip install PyPDF2 reportlab pdf2image Pillow colorama
    ```
- **or**
    ```sh
    pip install -r requirements.txt
    ```

To deactivate the virtual environment:
```sh
deactivate
```

## Steps to Use

### Create the following folders in the same path as the script:
- `input`: This folder should contain the PDFs to be combined.
- `output`: The combined PDF will be generated here.

### Run the script:
- **On Windows**:
  ```sh
  python combine_pdfs.py
  ```
- **On macOS** (with the virtual environment activated):
  ```sh
  python3 combine_pdfs.py
  ```

### Notes
- The DPI can be adjusted for the required quality, depending on the machine's resources.
- In the initial version, it works with the input PDFs grouped into a single file.


![alt text](https://www.python.org/static/img/python-logo.png)