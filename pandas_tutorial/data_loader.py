import pandas as pd


def get_data(csv_path):
    """
    Return csv as DataFrame
    """
    return pd.read_csv(csv_path)

def validate_date_format():
    from datetime import datetime

    data = get_data(r"D:\oop_project\pandas_tutorial\all-weeks-countries.csv")
    #print(data.index)

    cols_type = None

    for item in data['week'].replace(to_replace = '   ', value = '1900-01-01'):        
        try:
            dto = datetime.strptime(item, '%Y-%m-%d').date()
            cols_type = 'date'
        except:
            print(f"Not a valid data: {item}")

            cols_type = "varchar"
            print(item)
        
    return cols_type



if __name__ == '__main__':
    import json
    all_weeks_country_data = get_data(r"D:\oop_project\pandas_tutorial\all-weeks-countries.csv")
    all_weeks_global_data =get_data(r"D:\oop_project\pandas_tutorial\all-weeks-global.csv")
    most_popular_data = get_data(r"D:\oop_project\pandas_tutorial\most-popular.csv")

    # SqLite minden korlátjával

    test_df = all_weeks_global_data[["weekly_rank", "show_title"]]

    print(test_df.query("weekly_rank >= 1 & weekly_rank <=5 ")) 

    import pandasql as psql
    
    sdf = lambda e: psql.sqldf(e, globals()) # locals(), globals() paraméterek
    
    sql_statement= """
        select country_name from all_weeks_country_data
        limit 10
    """

    data = sdf(sql_statement)

    print(data)




    # ha az és kapcsolatot akarom használni akkor &
    # ha a vagy kapcsolatot akkow |
    # ha egyenlőség vizsgálat mint a pythonban: ==

    # df = pd.merge(all_weeks_country_data, all_weeks_global_data, on=["show_title", "season_title"], how="inner")

    # df2 = df.to_json("test.json")

    # df3 = df[0:4].to_excel("output.xlsx")

    #print(df.head(100))
    #weekly_hours_viewed
    # country_name

    # print(df[["weekly_hours_viewed", "country_name"]].head(100))
    
    # print(df.shape)

    # print()

    # print(df.info)
    
    
    # következő lépés: ezeket mergelni
    #print(dict(all_weeks_country_data.dtypes))

    # col_type = validate_date_format()

    # print(col_type)

    # print(most_popular_data.dtypes)

    #print(all_weeks_country_data.head(10))
    #print(all_weeks_global_data.head(10))
    #print(all_weeks_country_data.head(10))
    # print(data.shape) # visszaad egy tuple, hogy hány sor és hány oszlop van a dataframeben
    # print(data.axes)

    # print(data.columns)

    #print(all_weeks_country_data.info)

    # cnt = 0
    # for row_index, row in all_weeks_country_data.iterrows():
    #     cnt += 1
    #     print(row_index, row)

    #     if cnt == 10:
    #         break
        