from api.config.firebase_config import CREDENTIAL_JSON, PATH_FILE_DATA, BUCKET_NAME, BLOB_NAME, DESTINATION_FILE
from api.services.services import run_process

run_process(CREDENTIAL_JSON, PATH_FILE_DATA, BUCKET_NAME, BLOB_NAME, DESTINATION_FILE)