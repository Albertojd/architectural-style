# Architectural Styles Classification

En este proyecto intentaré clasificar el estilo arquitectónico de edifcios cargando una imagen en nuestra web; aún solo tengo 4 estilos arquitenctonicos entrenados, (Barroco, Bizantino, Egipcio, y Gótico), poco a poco iré incluyendo todos.

### Herramientas:

- **Redes neuronales:**
Las redes neuronales están diseñados para imitar el comportamiento del cerebro humano; el propósito de estas generalmente se reduce a 3 aspectos: aprender de la experiencia, obtener información, y generalizar lo ya aprendido en nuevos elementos.
![solarized dualmode](https://miro.medium.com/max/700/1*-eLjPY7UGSoQhSyW5qC6gw.gif)

- **CNN (Convolutional Neural Network):** Las redes neuronales convolucionales es un algoritmo de Deep Learning que está diseñado para trabajar con imágenes, tomando estas como input, asignándole importancias (pesos) a ciertos elementos en la imagen para así poder diferenciar unos de otros. 

 ![solarized dualmode](https://adeshpande3.github.io/assets/Cover.png)


- **Keras:** Es una biblioteca de python que ayuda en la creación de redes neuronales; Capaz de correr sobre los frameworks TensorFlow, CNTK, o Theano

- **TensorFlow:** Con esta librería somos capaces, entre otras operaciones, de construir y entrenar redes neuronales para detectar correlaciones y descifrar patrones, análogos al aprendizaje y razonamiento usados por los humanos.​

## Arquitectura:

Para construir la arquitectura de nuestro red convuncional hemos usado la biblioteca keras, en esta caso hemos diseñado 3 capas para entrenar el modelo

![solarized dualmode](./images/Captura.png)

## Entrenamiento:

Este modelo funciona bastante bien para 4 clases(estilos arquitectónico), para pode en un futuro cuando se incluyan más habrá que mejorarloL.

Para mejorar el modelo no solo hemos mejorado las capas, si no que he multiplicado las mismas fotos pero, rotandolas, aplicando zoom, o cambiando el brillo y contraste; con todo esto de accuracy es de: **0.9102444112300873**

En las siguientes gráficas podemos ver como avanza el entranmiento hacía un mejor acurracy, y un menor loss:

![solarized dualmode](/images/accuracy.png)
![solarized dualmode](/images/loss.png)

## Flask:

En este paso creamos una pequeña web, valiendonos de Flask.

Esta web carga nuestro modelo de predicción junto a una imagen y nos devolverá el estilo al que pertenece 

![solarized dualmode](/images/webexample.png)