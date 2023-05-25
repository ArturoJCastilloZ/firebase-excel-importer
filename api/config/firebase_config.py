from dotenv import load_dotenv
import os

# Carga las variables de entorno para las credenciales del archivo .env
# load_dotenv()

PATH_FILE_DATA = os.getenv("PATH_FILE")
DESTINATION_FILE = os.getenv("DESTINATION")
BLOB_NAME = os.getenv("BLOB")
BUCKET_NAME = os.getenv("BUCKET")

CREDENTIAL_JSON = ({
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
})