import pandas as pd

df = pd.read_xml(f"master_data\items.xml", parser="lxml", xpath=".//artikel")

df = df[["Artikelid", "Namn", "Namn2", "Prisinklmoms", "Volymiml", "PrisPerLiter", "Typ", 
        "Stil", "Forpackning", "Forslutning", "Ursprung", "Ursprunglandnamn", "Producent",
       "Leverantor", "Alkoholhalt", "Sortiment", "SortimentText", "Ekologisk", "Etiskt", "Alkoholhalt"]]


df_producers = pd.DataFrame(df['Producent'].unique())
df_producers.columns = ["name"]

df_producers["name"] = df_producers["name"].str.replace("'", '"')
df_producers["name"] = df_producers["name"].str.strip()

with open(r'master_data\producers.sql', "w", encoding='utf8') as f:
        for index, row in df_producers.iterrows():
            f.write(f"insert into producers(name, created_at) values('{row.iloc[0]}', NOW());\n")

df_suppliers = pd.DataFrame(df['Leverantor'].unique())
df_suppliers.columns = ["name"]
df_suppliers["name"] = df_suppliers["name"].str.replace("'", '"')
df_suppliers["name"] = df_suppliers["name"].str.strip()

with open(r'master_data\suppliers.sql', "w", encoding='utf8') as f:
        for index, row in df_suppliers.iterrows():
            f.write(f"insert into suppliers(name, created_at) values('{row.iloc[0]}', NOW());\n")
