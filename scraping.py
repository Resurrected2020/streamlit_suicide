import pandas as pd

def scraping(url):
    df_list = pd.read_html(url)
    df = df_list[4]
    return df
    
url = "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate"
df=scraping(url)
df.to_csv('homicide_rate.csv', index = False)