import firebase_admin
from firebase_admin import firestore, credentials, storage
import pandas as pd
from loguru import logger
import os


def init_firebase(credentials_) -> firestore.client:
    """Inicializa una instancia de la base de datos de Firestore de Firebase.

    Args:
        credentials_: Credenciales necesarias para la conexión
    
    Return:
        firestore.client.Client = Objeto de cliente que se puede usar para 
        realizar operaciones en la base de datos
    """
    try:
        logger.info("Inicializando firebase")
        cred = credentials.Certificate(credentials_)
        firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception as err:
        logger.exception(f"Ocurrió un error al inicializar firebase: \n {err}")


def download_file(bucket_name, blob_name, destination_file) -> None:
    """
    Descarga un archivo de Firebase Storage y lo guarda en una ubicación local.

    Args:
        bucket_name (str): El nombre del bucket de Firebase Storage donde se encuentra el archivo.
        blob_name (str): El nombre del objeto blob dentro del bucket que se desea descargar.
        destination_file (str): La ruta y el nombre de archivo donde se guardará el archivo descargado.

    Returns:
        None
    """
    try:
        logger.info("Descargando archivo de Firebase Storage")
        bucket = storage.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(destination_file)
    except Exception as err:
        logger.exception(f"Ocurrió un error al descargar el archivo de Firebaset Storage: \n {err}")


def get_data(data_file) -> dict:
    """Lee los datos de un archivo de Excel, 
    los convierte en un diccionario de Python y devuelve el diccionario.
    Cada hoja de cálculo en el archivo de Excel se convierte en una clave 
    en el diccionario y sus filas se convierten en valores asociados a esa clave.

    Args:
        data_file: Archivo excel que se leera
    
    Return:
        data: Diccionario de datos. 
    """
    try:
        logger.info("Extrayendo la información")
        excel_file = pd.ExcelFile(data_file)
        data = {}
        for sheet in excel_file.sheet_names:
            sheet_data = excel_file.parse(sheet)
            sheet_name = sheet.replace(" ", "-").lower()
            data[sheet_name] = sheet_data.to_dict('records')
        excel_file.close()
        return data
    except Exception as err:
        logger.exception(f"Ocurrió un error al extraer la información del archivo: \n {err}")


def clean_firestore(db) -> None:
    """Elimina todos los documentos y colecciones existentes en la base de datos. 
    Se utiliza para asegurarse de que la base de datos esté limpia antes de guardar nuevos datos.

    Args:
        db: Objeto de cliente de la base de datos Firestore de Firebase para
        realizar operaciones en la base de datos.
    """
    try:
        logger.info("Limpiando firestore collections")
        collections = db.collections()
        for collection in collections:
            docs = collection.stream()
            for doc in docs:
                doc.reference.delete()
        for collection in collections:
            collection.reference.delete()
    except Exception as err:
        logger.exception(f"Ocurrió un error al limpiar las colecciones existentes: \n {err}")


def save_data(db, data) -> None:
    """Guarda los datos en la base de datos de Firestore.
    Itera sobre el diccionario de datos y crea documentos en las colecciones correspondientes en la base de datos.

    Args:
        db: Objeto de cliente de la base de datos Firestore de Firebase para
        realizar operaciones en la base de datos.

        data: Datos a guardar.
    """
    try:
        logger.info("Guardando información")
        for collection_name, collection_data in data.items():
            collection_ref = db.collection(collection_name)
            for row_data in collection_data:
                doc_ref = collection_ref.document()
                doc_ref.set(row_data)
    except Exception as err:
        logger.exception(f"Ocurrió un error al guardar la información de Firestore: \n {err}")


def run_process(credentials, data_file, bucket_name, blob_name, destination_file):
    """Ejecuta todo el proceso"""
    db = init_firebase(credentials)
    download_file(bucket_name, blob_name, destination_file)
    data = get_data(data_file)
    clean_firestore(db)
    save_data(db, data)
    os.remove(f"./{data_file}")
    logger.success("Proceso completo")