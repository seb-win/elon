import os
from google.cloud import storage

def get_storage_client():
    # Hardcode the path to the service account JSON for local testing
    credentials_path = "/Users/sebastianwinkler/Documents/Jobseite/AI/work for elon/service_account_key.json"
    
    if os.path.exists(credentials_path):
        print(f"Running locally, using service account credentials from {credentials_path}")
        return storage.Client.from_service_account_json(credentials_path)
    else:
        print("Running on GCE, using default service account.")
        return storage.Client()

# Create a sample file within the script
def create_sample_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Created sample file: {filename}")

# Example usage: Upload a file to Google Cloud Storage
def upload_to_gcs(bucket_name, folder_name, source_file_name, destination_blob_name):
    storage_client = get_storage_client()
    bucket = storage_client.bucket(bucket_name)
    
    # Create the full path in the bucket (e.g., folder_name/destination_blob_name)
    blob_path = f"{folder_name}/{destination_blob_name}"
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {blob_path}.")

# Example: Create a sample file and upload it to GCS
bucket_name = 'work_for_elon'
folder_name = 'spacex'  # Folder within the bucket
source_file_name = 'example_upload.txt'
destination_blob_name = 'example_upload.txt'

# Create a file with sample content
sample_content = "Hello from the script! This is a test file for Google Cloud Storage upload."
create_sample_file(source_file_name, sample_content)

# Upload the file to the Cloud Storage bucket
upload_to_gcs(bucket_name, folder_name, source_file_name, destination_blob_name)
