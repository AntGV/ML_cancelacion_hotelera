import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


def total_transform(df_main):
    
    df = nombres_columnas(df_main)
    #---------------------------- CAMBIO 1-----------------------------------------
    # ASIGNACIÓN DE MEDIANA A POMOCIONES Y DEVOLUCIONES
    # ASIGNACIÓN DE MEDIANA A VALORES NULL
    # TRANSFORMACIÓN LOGÍSTICA A LA COLUMNA 'daily_price'
    df.loc[df["daily_price"] <= 0, "daily_price"] = 95.2
    df.loc[df["daily_price"].isnull(), "daily_price"] = 95.2
    df["daily_price"] = np.log10(df["daily_price"])
    #---------------------------- CAMBIO 2-----------------------------------------
    # ASIGNACIÓN DE MEDIANA A VALORES INCONSISTENTES Y TRANSFORMACIÓN LOGÍSTICA A LA COLUMNA 'lead_time'
    df.loc[df["lead_time"] <= 0, "lead_time"] = 66
    df.loc[df["lead_time"].isnull(), "lead_time"] = 66
    df["lead_time"] = np.log10(df["lead_time"])
    #---------------------------- CAMBIO 3-----------------------------------------
    # ASIGNACIÓN DE MEDIANA EN 'adults' DE REGISTROS CON VALOR 0 COINCIDENTES EN LAS COLUMNAS 'adults' Y 'children'
    # ASIGNACIÓN DE MEDIANA A VALORES NULL
    df.loc[df["adults"].isnull(), "adults"] = 2
    df.loc[df["children"].isnull(), "children"] = 0
    df.loc[(df["adults"] < 0), "adults"] = 0
    df.loc[(df["children"] < 0), "children"] = 0
    df.loc[((df["adults"] <= 0)&(df["children"] <= 0)), "adults"] = 2
    #---------------------------- CAMBIO 4-----------------------------------------
    # TRANSFORMACIÓN DE 'children' A CATEGÓRICA BINARIA
    df.loc[df["children"] > 0, "children"] = 1
    #---------------------------- CAMBIO 5-----------------------------------------
    # TRANSFORMACIÓN DE 'total_book' A CATEGÓRICA BINARIA
    # ASIGNACIÓN DE MEDIANA A VALORES NULL
    df.loc[df["total_book"].isnull(), "total_book"] = 0
    df.loc[df["total_book"] < 0, "total_book"] = 0
    df.loc[df["total_book"] > 0, "total_book"] = 1
    #---------------------------- CAMBIO 6-----------------------------------------
    # TRANSFORMACIÓN DE 'pre_cancel' Y 'pre_not_cancel' A CATEGÓRICA BINARIA
    # ASIGNACIÓN DE MEDIANA A VALORES NULL
    df.loc[df["pre_cancel"].isnull(), "pre_cancel"] = 0
    df.loc[df["pre_not_cancel"].isnull(), "pre_not_cancel"] = 0
    df.loc[df["pre_cancel"] < 0, "pre_cancel"] = 0
    df.loc[df["pre_not_cancel"] < 0, "pre_not_cancel"] = 0
    df.loc[df["pre_cancel"] > 0, "pre_cancel"] = 1
    df.loc[df["pre_not_cancel"] > 0, "pre_not_cancel"] = 1    
    #---------------------------- CAMBIO 7-----------------------------------------
    # ASIGNACIÓN DE MEDIANA EN VALORES INCONSISTENTES COINCIDENTES EN LAS COLUMNAS 'week_nights' y 'weekend_nights'
    # TRANSFORMACIÓN DE ETIQUETAS PARA UNIFICAR LOS VALORES POR ENCIMA DE 5 EN 'week_nights' Y POR ENCIMA DE 2 EN 'weekend_nights'
    # ASIGNACIÓN DE MEDIANA A VALORES NULL
    df.loc[df["week_nights"].isnull(), "week_nights"] = 2
    df.loc[df["weekend_nights"].isnull(), "weekend_nights"] = 1
    df.loc[df["week_nights"] < 0, "week_nights"] = 0
    df.loc[df["weekend_nights"] < 0, "weekend_nights"] = 0
    df.loc[((df["week_nights"] == 0)&(df["weekend_nights"] == 0)), "week_nights"] = 2    
    df.loc[df["week_nights"] > 5, "week_nights"] = 6
    df.loc[df["weekend_nights"] > 2, "weekend_nights"] = 3
    #---------------------------- CAMBIO 8-----------------------------------------
    # TRANSFORMACIÓN DE 'meal_plan' A VARIABLE NUMÉRICA CON ORDINAL ENCODER
    # ASIGNACIÓN DE MODA A VALORES NULL
    list_meal = ["SC","RO","BB","HB","FB"]
    df.loc[df["meal_plan"].isnull(), "meal_plan"] = "BB"
    df.loc[~df["meal_plan"].isin(list_meal), "meal_plan"] = "BB"   
    encoder = OrdinalEncoder(categories=[["SC","RO","BB","HB","FB"]])    
    df[["meal_plan"]] = encoder.fit_transform(df[["meal_plan"]])
    #---------------------------- CAMBIO 9-----------------------------------------
    # TRANSFORMACIÓN DE 'parking' A VARIABLE BINARIA
    # ASIGNACIÓN DE MEDIANA A VALORES NULL
    df.loc[df["parking"].isnull(), "parking"] = 0
    df.loc[df["parking"] < 0, "parking"] = 0
    df.loc[df["parking"] > 0, "parking"] = 1
    #---------------------------- CAMBIO 10-----------------------------------------
    # ELIMINACIÓN DE 'arr_date'
    df.drop(columns = ["arr_date"], inplace = True)

    return df


def nombres_columnas(df_names):
    df_names.rename(columns = {"is_canceled":"booking_status",
                      "arrival_date_year":"arrival_year",
                      "arrival_date_month":"arrival_month",
                      "arrival_date_day_of_month":"arrival_date",
                      "stays_in_weekend_nights":"no_of_weekend_nights",
                      "stays_in_week_nights":"no_of_week_nights",
                      "adults":"no_of_adults",
                      "children":"no_of_children",
                      "meal":"type_of_meal_plan",
                      "market_segment":"market_segment_type",
                      "is_repeated_guest":"repeated_guest",
                      "previous_cancellations":"no_of_previous_cancellations",
                      "previous_bookings_not_canceled":"no_of_previous_bookings_not_canceled",
                      "reserved_room_type":"room_type_reserved",
                      "required_car_parking_spaces":"required_car_parking_space",
                      "total_of_special_requests":"no_of_special_requests",
                      "adr":"avg_price_per_room",
                      }, inplace = True)

    df_names.rename(columns = {"no_of_adults":"adults",
                        "no_of_children":"children",
                        "no_of_weekend_nights":"weekend_nights",
                        "no_of_week_nights":"week_nights",
                        "type_of_meal_plan":"meal_plan",
                        "required_car_parking_space":"parking",
                        "room_type_reserved":"room_type",
                        "lead_time":"lead_time",
                        "arrival_year":"arrival_year",
                        "arrival_month":"arrival_month",
                        "arrival_date":"arrival_day",
                        "market_segment_type":"ms_type",
                        "repeated_guest":"repeated_guest",
                        "no_of_previous_cancellations":"pre_cancel",
                        "no_of_previous_bookings_not_canceled":"pre_not_cancel",
                        "avg_price_per_room":"daily_price",
                        "no_of_special_requests":"special_req",
                        "booking_status":"canceled",
                        }, inplace = True)

    return df_names


def tipifica_variables(df: pd.DataFrame, umbral_categoria: int, umbral_continua: float):
    """
    Recibe un DataFrame y parámetros para tipificar las columnas

    Argumentos:
    df: cualquier dataframe.
    umbral_categoria: marca el límite a partir el cual se va a considerar una variable categorica.
    umbral_continua: marca el límite a partir el cual se va a diferenciar entre numérica continua o discreta,

    Retorna:
    DataFrame: un dataframe nuevo, donde las columnas del de entrada se convierten en filas y cada columna refleja el tipo de la variable.
    """
    
    filas = []
    tipos = []

    for col in df:
        n_unique = df[col].nunique()
        cardinalidad_porcentaje = (n_unique / len(df)) * 100

        if n_unique == 2:
            tipo = 'Binaria'

        elif n_unique < umbral_categoria:
            tipo = 'Categorica'

        else:

            if cardinalidad_porcentaje >= umbral_continua:
                tipo = 'Numérica Continua'
            else:
                tipo = 'Numérica Discreta'

        filas.append(col)
        tipos.append(tipo)

    return_df = pd.DataFrame({
        'nombre_variable': filas,
        'tipo_sugerido': tipos
    })

    return return_df

