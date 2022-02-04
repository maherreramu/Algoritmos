import pandas as pd
url_data_time = 'https://co.mejoresrutas.com/tabla-de-distancias-entre-ciudades/co.csv?measure=time&type=road'
url_data_distance = 'https://co.mejoresrutas.com/tabla-de-distancias-entre-ciudades/co.csv?measure=metric&type=road'

df_time = pd.read_csv(url_data_time, index_col=0)
i = df_time.index
i_l = list(i)
df_time = df_time.drop(labels=[i_l[15], i_l[16], i_l[17]], axis=0)

df_dist = pd.read_csv(url_data_distance, index_col=0)
i = df_dist.index
i_l = list(i)
df_dist = df_dist.drop(labels=[i_l[15], i_l[16], i_l[17]], axis=0)
#print(df_time['Bucaramanga']['Pasto'])