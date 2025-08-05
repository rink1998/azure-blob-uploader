import streamlit as st
from azure.storage.blob import BlobServiceClient

st.set_page_config(page_title="Azure Blob Uploader", page_icon="📤")
st.title("📤 Upload File to Azure Blob Storage")

# Input: Connection string and container name
connection_string = st.text_input("Enter your Azure Storage connection string", type="password")
container_name = st.text_input("Enter container name", value="uploads")

# File upload
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file and connection_string and container_name:
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=uploaded_file.name)
        
        blob_client.upload_blob(uploaded_file, overwrite=True)

        st.success(f"File '{uploaded_file.name}' uploaded successfully to container '{container_name}'!")

    except Exception as e:
        st.error(f"Upload failed: {e}")
