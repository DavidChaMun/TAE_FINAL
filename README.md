# Projecto Final de la materia TAE


## Autores
David Chaverra Munera  
Juan Felipe Munera Vergara  
Andres Aguilar  


## Decisiones de diseño

### Neuronal Network
### Random Forest
Para la implementacion de este metdo, se hace uso de
#### Meta Parametros
Se tienen en cuenta 3 meta parametros:  
-feature
#### Resultados
### Suport-Vector Machine

## Despliegue
### Docker
Se tiene un Dockerfile, la imagen se construye usando:  
```sh
docker build -t tae_final .  
```
En la consola de comandos, en el path del proyecto. Una vez la imagen ha sido construida para poder correrla se debe primero usar el comando:  
```sh
xhost +local:root
```
La imagen solo esta diseñada para correr en un host de linux. Luego se usa:  
```sh
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY tae_final
```

### Otros
En caso de no contar con un host de linus y docker, se puede correr localmente con el comando:  
python3 main.py, solo si primero se instalan las dependencias necesarias con:  
```sh
pip install --no-cache-dir -r requirements.txt
```