import pandas as pd

# Création des tables de référence pour la base SQL 

encod_dic = {name:label for label,name in enumerate(set(final_df.Region))}
df_region = pd.Series(encod_dic).to_frame()
df_region.columns = ['region_id']
df_region = df_region.reset_index()
df_region.columns = ['Name', 'id']


final_df['region_id'] = final_df.Region.apply(lambda x: encod_dic[x])
final_df.drop('country',axis = 1, inplace=True)
final_df.to_csv('country_info_table.csv', index = False)
df_region.to_csv('country_id_table.csv', index = False)
#print(df_region)
#print(">>>>>>>>>>>>")
#print(final_df)
