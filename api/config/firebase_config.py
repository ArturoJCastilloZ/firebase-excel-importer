from dotenv import load_dotenv
import os

# Carga las variables de entorno para las credenciales del archivo .env
load_dotenv()

PATH_FILE_DATA = os.environ.get("PATH_FILE")
DESTINATION_FILE = os.environ.get("DESTINATION")
BLOB_NAME = os.environ.get("BLOB")
BUCKET_NAME = os.environ.get("BUCKET")

CREDENTIAL_JSON = ({
    "type": os.environ.get("TYPE"),
    "project_id": os.environ.get("PROJECT_ID"),
    "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
    "private_key": os.environ.get("PRIVATE_KEY").replace(r'\n', '\n'),
    "client_email": os.environ.get("CLIENT_EMAIL"),
    "client_id": os.environ.get("CLIENT_ID"),
    "auth_uri": os.environ.get("AUTH_URI"),
    "token_uri": os.environ.get("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.environ.get("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.environ.get("CLIENT_X509_CERT_URL")
})