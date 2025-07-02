
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, mannwhitneyu, pearsonr


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


def nombres_columnas(df):
    df.rename(columns = {"is_canceled":"booking_status",
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

    df.rename(columns = {"no_of_adults":"adults",
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

