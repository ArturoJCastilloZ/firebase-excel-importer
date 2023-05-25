from dotenv import load_dotenv
import os

# Carga las variables de entorno para las credenciales del archivo .env
load_dotenv()

PATH_FILE_DATA = os.getenv("PATH_FILE")
DESTINATION_FILE = os.getenv("DESTINATION")
BLOB_NAME = os.getenv("BLOB")
BUCKET_NAME = os.getenv("BUCKET")

CREDENTIAL_JSON = ({
    "TYPE": os.getenv("TYPE"),
    "PROJECT_ID": os.getenv("PROJECT_ID"),
    "PRIVATE_KEY_ID": os.getenv("PRIVATE_KEY_ID"),
    "PRIVATE_KEY": os.getenv("PRIVATE_KEY"),
    "CLIENT_EMAIL": os.getenv("CLIENT_EMAIL"),
    "CLIENT_ID": os.getenv("CLIENT_ID"),
    "AUTH_URI": os.getenv("AUTH_URI"),
    "TOKEN_URI": os.getenv("TOKEN_URI"),
    "AUTH_PROVIDER_X509_CERT_URL": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "CLIENT_X509_CERT_URL": os.getenv("CLIENT_X509_CERT_URL")
})