## 1. crear un ambiente virtual enviromment
creal el virtual envariomment para la instalacion de las librerias necesarias para el proyecto
````shell
python3 -m venv .venv
````
## 2. crear el archivo .gitnore
crear el archivo **.gitignore** para configurar los recursos que no necesitamos que se sincronicen
````shell
*.pyc
__pycache__/
.venv/
````
## 3. activar el cirtual enviromment
activar el **virtual envirromment** para realizar la instalacion de las librerias necesarias
````shell
source .venv/bin/activate
````
## 4. actualizar pip
actualizar el instalador de paquetes de python pip
````shell
pip install --upgrade pip
````
## 5. crear el archivo **runtime.txt**
crear el archivo **runtime.txt** con la version utilizada de python3
````shell
python3 -V > runtime.txt
````
## 6. instalar el micro-framework **web.py**
instalar el micro-framework **web.py** en el ambiente virtual
````shell
pip install web.py
````
## 7. crear el archivo requeriments.txt
crear el archivo requirements.txt con las versiones de las librerias instaladas en el ambiente virtual
````shell
pip freeze > requirements.txt
````
## 8. indexar el contenido del repositorio
indexar todo el contenido de repositorio para incluir todos los archivos nuevos y las modificaciones realizadas
al codigo.
````shell
git add.
````
## 9. creamos un commit
crear un punto de control con los cambios realizados al proyecto
````shell
git commit -m "CREATED configuracion del ambiente virtual"
````
## 10. realizar un push hacia el repositorio
realizar un push hacia el repositorio ára sincronizar los cambios realizados en el proyecto
````shell
git push -u origin main
````
tarea se creara nueva carpeta llamada urls
agregar 10 urls con su respectivo mensaje
## lista de ejercicios
lista de ejercicios con web.py
|NO.|Ejercicios|Descripcion|
|--|--|--|
|1|Hola_mundo|hola mundo de web.py|

maso menos