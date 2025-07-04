<p align="center";">
  <img src="./src/img/cabeceralite.jpg" alt="imagen" style=width: 98%;">
  <i><i">Imagen creada con NightCafe</i>
</p>
  
# RESERVA CONFIRMADA
### Proyecto Machine Learning de predicción de cancelación de reservas hoteleras.

---

Autor: Antonio García Valverde

---

### Objetivo del proyecto
Una compañía de alojamiento turístico plantea la elaboración de un modelo de predicción que clasifique las futuras reservas que reciban en posibles confirmaciones o cancelaciones, con el objetivo de anticiparse a las cancelaciones y poder aplicar mejores propuestas de marketing y promociones a sus clientes a partir de la previsión.
La compañía facilita los datos de las reservas recibidas entre los años 2015-2018 para su análisis.

---

### Datasets empleados
Los datos se han extraído de las siguientes fuentes:
* **[Hotel_Reservations]("https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset")**
* **[Hotel_Bookings]("https://www.kaggle.com/datasets/moro146/hotel-bookings")**

A lo largo del proyecto se ha llevado a cabo un proceso de adecuación de las variables contenidas en ambos para poder ser empleados en conjunto.  
Posteriormente se han transformado sus valores para una mejor evaluación del modelo.  

---

### Solución aportada
La propuesta de solución es el desarrollo de un modelo supervisado clasificador, para predecir si las futuras reservas serán confirmadas o canceladas.  

---

### Estructura de directorios
Los directorios incluidos en este proyecto siguen la siguiente estructura:  

```python
├── ML_CANCELACION_HOTELERA/  # Directorio raiz del proyecto.  
    ├── src/                  # Subdirectorio de almacenamiento.
        ├── data/             # Carpeta que contiene los dataset de trabajo una vez modificados los dataset fuente. 
        ├── data_sample/      # Carpeta que incluye una muestra del dataset de trabajo (dos archivos, con y sin target), para su empleo posterior en pruebas.
        ├── img/              # En esta carpeta se guardan las imágenes empleadas en el proyecto.
        ├── models/           # Carpeta donde se almacenará para producción el modelo desarrollado.
        ├── notebooks/        # Contiene los diferentes notebooks de trabajo y evaluación empleados en el proyecto.
        ├── utils/            # En este directorio se almacenan losarchivos con funciones recurrentes empleadas en el análisis.
    ├── main.ipynb            # Notebook donde se incluye el proceso completo, paso a paso, de creación del modelo.
    ├── presentacion.pdf      # Archivo pdf con la presentación del proyecto.
```

---


    
