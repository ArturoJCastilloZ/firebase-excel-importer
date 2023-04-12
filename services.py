import firebase_admin
from firebase_admin import firestore, credentials
import pandas as pd
from loguru import logger


def init_firebase(credentials_) -> firestore.client:
    """Inicializa una instancia de la base de datos de Firestore de Firebase.

    Args:
        credentials_: Credenciales necesarias para la conexión
    
    Return:
        firestore.client.Client = Objeto de cliente que se puede usar para 
        realizar operaciones en la base de datos

    """
    logger.info("Inicializando firebase")
    cred = credentials.Certificate(credentials_)
    firebase_admin.initialize_app(cred)
    return firestore.client()


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
    logger.info("Extrayendo la información")
    excel_file = pd.ExcelFile(data_file)
    data = {}
    for sheet in excel_file.sheet_names:
        sheet_data = excel_file.parse(sheet)
        sheet_name = sheet.replace(" ", "-").lower()
        data[sheet_name] = sheet_data.to_dict('records')
    return data


def clean_firestore(db) -> None:
    """Elimina todos los documentos y colecciones existentes en la base de datos. 
    Se utiliza para asegurarse de que la base de datos esté limpia antes de guardar nuevos datos.

    Args:
        db: Objeto de cliente de la base de datos Firestore de Firebase para
        realizar operaciones en la base de datos.
    """
    logger.info("Limpiando firestore collections")
    collections = db.collections()
    for collection in collections:
        docs = collection.stream()
        for doc in docs:
            doc.reference.delete()
    for collection in collections:
        collection.reference.delete()


def save_data(db, data) -> None:
    """Guarda los datos en la base de datos de Firestore.
    Itera sobre el diccionario de datos y crea documentos en las colecciones correspondientes en la base de datos.

    Args:
        db: Objeto de cliente de la base de datos Firestore de Firebase para
        realizar operaciones en la base de datos.

        data: Datos a guardar.
    """
    logger.info("Guardando información")
    for collection_name, collection_data in data.items():
        collection_ref = db.collection(collection_name)
        for row_data in collection_data:
            doc_ref = collection_ref.document()
            doc_ref.set(row_data)


def run_process(credentials, data_file):
    """Ejecuta todo el proceso"""
    db = init_firebase(credentials)
    data = get_data(data_file)
    clean_firestore(db)
    save_data(db, data)
    logger.success("Proceso completo")