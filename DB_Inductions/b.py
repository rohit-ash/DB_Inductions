import pandas as pd
df = pd.read_csv(r"data_csv.csv")
df = df.sort_values('Name')
df.index=df.Code
df = df.drop("Code", axis=1)
country = df.to_dict()
country = country['Name']
country1 = input()
country2 = input()
for key in country:
    if(country[key]>country[country1]):
        if(country[key]<country[country2]):
            print(country[key])