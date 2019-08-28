# Projecto Final de la materia TAE


## Autores
David Chaverra Munera  
Juan Felipe Munera Vergara  
Andres Felipe Aguilar Rendon    
Christian Camilo Guzmán Escobar


## Decisiones de diseño

### Neuronal Network
### Random Forest
Para la implementacion de este metdo, se hace uso del modulo DecisionTreeClassifier de sklearn para el motor de prediccion, ademas se hace uso del modulo LabelEncoder y OneHotEncoder para la generacion de las variables dummies apartir de las variables categoricas. 

#### Meta Parametros
Se tienen en cuenta 3 meta parametros:  
- Numero de estimadores: 100.
- Numero de categorias: 7.
- Maximo de profundidad: 16.
#### Resultados


Real vs  Pedicha | <=50k | >50k 
---- | ---- | ---- 
<=50k | 10788 | 571
| >50k | 1561 | 2139 

Logrando una precision del: 86%

### Suport-Vector Machine
### GUI
Para la gui se hace uso del modulo tkinter

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
