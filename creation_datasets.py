import pandas as pd 

def rename_columns(df_homocide):
    homicid_col = ["Country (or dependent territory, subnational area, etc.)", "Rate", "Count"]
    df_homocide = df_homocide[homicid_col]
    df_homocide.columns = ['country', "homicide_rate", "homicide_count"]
    return df_homocide

df_homocide = pd.read_csv('homicide_rate.csv')
df_homocide=rename_columns(df_homocide)
df_homocide.to_csv('homicide_rate_clean.csv',index=False)


df_happy = pd.read_csv('archive/2015.csv')
df_happy.rename(columns={"Country": "country"}, inplace=True)
df_happy.to_csv('happy.csv', index=False)


print(df_happy.head(),df_homocide.head())

df_suicide = pd.read_csv('datasets taux de suicide/master.csv')
df_suicide_2016 = df_suicide[df_suicide["year"]==2016]



"""
Groupement des données par pays pour l'année 2016. Pour chaque pays, on donne les résultats des colonnes suivantes : 
gdp_per_capita ($), gdp_for_year ($) population, suicides_no, gdp_per_capita ($). Puis on calcule le nombre 
de suicides pour 100 000 habitants pour chaque pays et on ajoute les résultats obtenus dans la colonne 
'suicide_rate_per_100k' puis on enregistre le dataset obtenu. 
"""


df_suicide = pd.read_csv('datasets taux de suicide/master.csv')
df_suicide_2016 = df_suicide[df_suicide["year"]==2016]

def nettoyage_dataset_suicide(df_suicide_2016):
    df_suicide_2016[" gdp_for_year ($) "] = df_suicide_2016[" gdp_for_year ($) "].str.replace(',','').astype(float)
    
    mean_groupby = df_suicide_2016.groupby('country').mean()[['gdp_per_capita ($)', ' gdp_for_year ($) ']]
    sum_groupby = df_suicide_2016.drop('suicides/100k pop', axis = 1).groupby('country').sum()[['population', 'suicides_no', 'gdp_per_capita ($)']]
    
    
    df_suicide_2016_processed = pd.concat([mean_groupby, sum_groupby], axis=1)
    df_suicide_2016_processed['suicide_rate_per_100k'] = (df_suicide_2016_processed['suicides_no']/df_suicide_2016_processed['population'])*100_000
    return df_suicide_2016_processed

df_suicide_2016_processed=nettoyage_dataset_suicide(df_suicide_2016)

df_suicide_2016_processed.to_csv('suicide.csv')