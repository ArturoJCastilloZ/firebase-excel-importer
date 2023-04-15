# **Firebase Excel Data Importer**

Este proyecto es una aplicación que lee datos desde un archivo de Excel y los guarda en una base de datos de Firebase Firestore. El proyecto consta de cuatro funciones principales, que son:

- `init_firebase`: Inicializa una instancia de la base de datos de Firestore de Firebase.

- `get_data`: Lee los datos de un archivo de Excel y los convierte en un diccionario de Python.

- `clean_firestore`: Elimina todos los documentos y colecciones existentes en la base de datos de Firestore.

- `save_data`: Guarda los datos en la base de datos de Firestore.

La función run_process ejecuta todas las funciones anteriores para importar los datos desde un archivo de Excel a la base de datos de Firestore.

----

## **REQUERIMIENTOS**

Este proyecto requiere los siguientes paquetes de Python:

- Cuenta de Firebase y proyecto activo
- firebase_admin
- pandas
- loguru
- dotenv

Además, también se necesitan las credenciales de Firebase para poder conectarse a la base de datos de Firestore.

----

## **INSTALACIÓN**

1. Clonar el repositorio y navegar hasta la carpeta raíz del proyecto.
2. Crear un ambiente virtual de Python con `virtualenv venv` y activarlo con `source venv/bin/activate` o `venv/Scripts/activate` en windows.
3. Instalar las librerías requeridas con `pip install -r requirements.txt`.
4. Descargar las credenciales de servicio de Firebase en formato JSON y agrega los valores en el archivo `.env.example` y después elimina la extensión `.example` del mismo.
5. Agrega la ruta del archivo excel en el archivo `firebase_config.py`.
6. Ejecutar el proyecto con el comando `python main.py`.

----

## **USO**

Para utilizar esta aplicación, simplemente llame a la función run_process con las credenciales de Firebase y el archivo de Excel que desea importar. La aplicación se encargará de todo lo demás.

----

## **CONTRIBUCIÓN**

Si encuentras algún error o quieres contribuir al proyecto, por favor envía un Pull Request con tus cambios. También puedes abrir un Issue para discutir nuevas características o reportar problemas. ¡Tu ayuda es bienvenida para mi crecimiento!