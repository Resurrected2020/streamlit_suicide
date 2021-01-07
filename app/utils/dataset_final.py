import pandas as pd

# Vérification de la présence de doublons dans les pays ou de pays manquants dans les trois datasets.


df_suicide_2016_processed, df_happy, df_homocide = pd.read_csv('suicide.csv'), pd.read_csv('happy.csv'), pd.read_csv('homicide_rate_clean.csv')

def get_len_country(df):
    number_unique_country = len(df.country.unique())
    print(f"- {number_unique_country} unique countries")

def check_if_duplicate(df):
    has_duplicate = df.country.duplicated().any()
    print(f"- has duplicated countries : {has_duplicate}")
    
def get_missing_courntry(set1, set2):
    return list(set1 - set2)
    
def check_similar_country(df1, *args):
    for df in args:
        set_colu_df1, set_colu_df2 = set(df1.country.unique()), set(df.country.unique())
        is_subset = set_colu_df1.issubset(set_colu_df2)
        print(f"All countries in df1 are present in df2 : {is_subset}")
        if not is_subset:
            missing_col = get_missing_courntry(set_colu_df1, set_colu_df2)
            print(f"missing col in df2 {missing_col}")
    
d = {
    "df_suicide_2016_processed":df_suicide_2016_processed,
    "df_happy":df_happy,
    "df_homocide":df_homocide,
} 
for name, df in d.items():
    print(name)
    get_len_country(df)
    check_if_duplicate(df)
    
check_similar_country(df_suicide_2016_processed, df_happy, df_homocide)

"""

countries1 = {"france"}
countries2 = {"france", "allemagne"}
countries1.issubset(countries2)
countries2.issubset(countries1)

"""
# Fusion des trois datasets dans un seul dataset final sur la colonne "pays" commune aux trois datasets

first_merge = df_suicide_2016_processed.merge(df_happy,on="country")
final_df = first_merge.merge(df_homocide,on="country")
final_df.to_csv('whole_data.csv', index = False)
