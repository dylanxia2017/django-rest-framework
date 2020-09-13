from sqlalchemy import create_engine
import pandas as pd


def mysql_assistance():
    eng = create_engine('mysql+pymysql://root:abc123456@127.0.0.1:3306/eleme?charset=utf8')
    try:
        df_eleme = pd.read_csv("eleme_ok.csv")
        df_eleme.to_sql(name="api_entry",con = eng, if_exists="append", index = False)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    mysql_assistance()