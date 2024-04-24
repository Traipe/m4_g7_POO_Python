
Desafio dia 12 - individual

Este proyecto consiste en un script de Python diseñado para leer un archivo de texto que contiene datos de usuarios en formato JSON, crear instancias de usuario a partir de estos datos y manejar posibles excepciones durante el proceso. También registra cualquier error en un archivo de registro para su posterior revisión.

Requisitos:

Python 3.x

Uso:

- Clona este repositorio o descarga el archivo script.py en tu sistema local.
- Asegúrate de tener un archivo de texto llamado usuarios.txt en el mismo directorio que contiene los datos de los usuarios en formato JSON.
- Ejecuta el script script.py utilizando Python:

python script.py

- El script leerá cada línea del archivo usuarios.txt, intentará crear una instancia de usuario a partir de los datos y manejará cualquier excepción que ocurra durante este proceso.
- Los errores detectados se registrarán en el archivo error.log ubicado en el mismo directorio.

Estructura del Proyecto:

- script.py: El script principal que lee el archivo de usuarios, crea instancias de usuario y maneja las excepciones.
- usuario.py: Archivo que contiene la definición de la clase Usuario.
- usuarios.txt: Archivo de texto que contiene los datos de los usuarios en formato JSON.
- error.log: Archivo de registro que registra cualquier error que ocurra durante la ejecución del script.

### Ejemplo de Uso

tienes un archivo `usuarios.txt` con el siguiente contenido:

```json
{
  "nombre": "Inger",
  "apellido": "Baldcock",
  "email": "ibaldcock9@alibaba.com",
  "genero": "Female"
}
