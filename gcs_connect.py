from google.cloud import storage

# Path to your service account key file
service_account_file = 'service_account_key.json'

# Name of the bucket and the file you want to upload
bucket_name = 'work_for_elon'
destination_blob_name = 'hello_world.txt'

# Create a text file with "Hello World!" content
source_file_name = 'hello_world.txt'
with open(source_file_name, 'w') as f:
    f.write('Hello World!')

# Initialize a client using the service account
storage_client = storage.Client.from_service_account_json(service_account_file)

# Get the bucket
bucket = storage_client.bucket(bucket_name)

# Upload the file to Google Cloud Storage
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

print(f"File {source_file_name} uploaded to {destination_blob_name}.")
