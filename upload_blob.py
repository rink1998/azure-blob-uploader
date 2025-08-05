from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace this with your Azure Blob Storage connection string
connection_string = "your_connection_string_here"

# Configuration
container_name = "uploads"  # Replace with your container name
file_path = "testfile.txt"  # Replace with your file name
blob_name = "testfile.txt"  # Name for the file in blob

try:
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get the container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create a blob client using the file name
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the file
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"✅ '{fil
