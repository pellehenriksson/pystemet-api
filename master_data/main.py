import pandas as pd


df = pd.read_xml(f"master_data\items.xml", parser="lxml", xpath=".//artikel")

df = df[["nr", "Namn", "Namn2", "Prisinklmoms", "Volymiml", "PrisPerLiter", "Typ", "Stil", "Forpackning", "Forslutning", "Ursprung", "Ursprunglandnamn", "Producent", "Leverantor", "Alkoholhalt", "Ekologisk", "Etiskt"]]

#todo: fix names
df_items = df[["nr", "Namn", "Namn2", "Prisinklmoms", "Volymiml", "PrisPerLiter", "Forpackning", "Forslutning", "Ursprung", "Ursprunglandnamn", "Alkoholhalt", "Ekologisk", "Etiskt"]]

df_items.columns = ["number", "name", "name2", "price", "volume", "comparison_price", "packaging", "sealing", "origin", "origin_country", "alcohol_content", "is_organic", "is_ethical"]

def build_name(x, y):
    if y is None:
        return x
    
    return f"{x} {y}".strip()

def handle_none(r):
        if r is None:
              return "null"

        return f"'{r}'"

def handle_bool(r):
      
        if r > 0:
            return 'true'
        else:
            return 'false'


df_items["complete_name"] = df_items.apply(lambda row: build_name(row["name"], row["name2"]), axis=1)
df_items["alcohol_content"] = df_items["alcohol_content"].str.replace("%", "")

# 0'number', 1'name', 2'name2', 3'price', 4'volume', 5'comparison_price',  6'packaging', 7'sealing', 8'origin', 9'origin_country', 10'alcohol_content',       11'is_organic', 12'is_ethical', 13'complete_name'

with open(r'master_data\items.sql', "w", encoding='utf8') as f:
        for index, row in df_items.iterrows():
                f.write(f"""
insert into items (number, name, price, comparison_price, volume, alcohol_content, packaging, sealing, origin, origin_country, is_organic, is_ethical, producer_id, supplier_id, item_type_id, item_style_id, created_at) 
values ('{row.iloc[0]}', '{row.iloc[13]}', {row.iloc[3]}, {row.iloc[5]},{row.iloc[4]}, {row.iloc[10]}, {handle_none(row.iloc[6])}, {handle_none(row.iloc[7])}, {handle_none(row.iloc[8])}, {handle_none(row.iloc[9])}, {handle_bool(row.iloc[11])}, {handle_bool(row.iloc[12])}, 0, 0, 0, 0, NOW());\n
""")


"""
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

df_item_type = pd.DataFrame(df['Typ'].unique())
df_item_type.columns = ["name"]
df_item_type["name"] = df_item_type["name"].str.strip()

with open(r'master_data\item_types.sql', "w", encoding='utf8') as f:
        for index, row in df_item_type.iterrows():
            f.write(f"insert into item_types(name, created_at) values('{row.iloc[0]}', NOW());\n")

df_item_style = pd.DataFrame(df['Stil'].unique())
df_item_style.columns = ["name"]
df_item_style["name"] = df_item_style["name"].str.strip()

with open(r'master_data\item_styles.sql', "w", encoding='utf8') as f:
        for index, row in df_item_style.iterrows():
            f.write(f"insert into item_styles(name, created_at) values('{row.iloc[0]}', NOW());\n")

"""
