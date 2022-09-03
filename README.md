# dockerizar-una-aplicacion-de-Python


## Requerimientos de la Tarea

Dockerizar una aplicación en python, se requiere un repositorio que contenga:
- El Dockerfile
- Readme

La imagen debe estar publicada en Docker Hub, y el Readme debe incluir las instrucciones para ejecutar el contenedor

## Instrucciones para correr el dockerfile, descargando la imagen desde Docker hub

### 1
Se ejecuta el comando para descargar la imagen desde DockerHub:

- sudo docker pull fabricio2000gjuarez/pythonapp:latest

## 2 
Se ejecuta el siguiente comando para levantar el contenedor en la maquina local:

- sudo docker run -d -it -p 80:80 fabricio2000gjuarez/pythonapp:latest 


