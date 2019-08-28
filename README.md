# Projecto Final de la materia TAE


## Autores
David Chaverra Múnera  
Juan Felipe Múnera Vergara  
Andrés Felipe Aguilar Rendón    
Christian Camilo Guzmán Escobar


## Decisiones de diseño


### Neuronal Network
Para la implementación de las redes neuronales, se hace uso del módulo sequence de Keras para el motor de predicción. El mejor modelo se evaluó optimizando la precisión utilizando una base de datos de validación. 

#### Meta Parametros
Los meteparámetros considerados fueron:
- Número de capas y neuronas dentro de *sequential*.

- Método de activación de la neurona de salida.

- Optimizador.

- Número de epochs.

#### Resultados
Precision: Aproximádamente ~85%.


### Random Forest
Para la implementacion de este método, se hace uso del modulo DecisionTreeClassifier de sklearn para el motor de prediccion, ademas se hace uso del modulo LabelEncoder y OneHotEncoder para la generacion de las variables dummies apartir de las variables categoricas.

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
Para la implementación de este modelo, se hace uso del módulo svm de sklearn para el motor de predicción.

#### Meta Parametros
Se tienen en cuenta 3 meta parametros:  
- Kernel: Linear.
- Gamma: Por defecto (Auto).
- C: Por defecto (1).
#### Resultados
Precision: Aproximádamente 78%

### GUI
Para la gui se hace uso del modulo tkinter, para correr la GUI se ejecuta main.py.

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
En caso de no contar con un host de linux y docker, se puede correr localmente con el comando:  
python3 main.py, solo si primero se instalan las dependencias necesarias con:  
```sh
pip install --no-cache-dir -r requirements.txt
```
