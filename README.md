# 🚀 Azure Blob Storage Uploader

This project demonstrates multiple ways to upload files to Azure Blob Storage using:

- ✅ Azure Portal (manual upload)
- ✅ Azure CLI (automated via terminal)
- ✅ Python SDK (`upload_blob.py`)
- ✅ Streamlit UI for browser-based uploads (`app.py`)

---

## 📁 Project Structure

| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `upload_blob.py`| Uploads a local file to Azure Blob using Python  |
| `app.py`        | Streamlit UI for uploading files via browser     |
| `README.md`     | Project overview and usage instructions          |

---

## 🔧 Prerequisites

- Azure Subscription
- A Storage Account and Blob Container
- Python 3.x installed
- `azure-storage-blob` and `streamlit` libraries

Install packages locally using:

```bash
pip install azure-storage-blob streamlit
