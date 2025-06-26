import numpy as np
import pandas as pd

def cambiar_numerica_binaria(df,columna):
    ncol = df.columns.get_loc(columna)
    for ind,val in enumerate(df[columna]):
        if val > 0:
            df.iloc[ind,ncol] = 1

