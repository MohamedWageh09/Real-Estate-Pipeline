from sqlalchemy import create_engine
import os

db = 'postgresql://admin:admin@localhost:5432/real_estate_db'

def load_to_postgres(df, table_name):
    try:
        engine = create_engine(db)
        df.toPandas().to_sql(table_name, engine, if_exists='replace', index=False)
    except Exception as e:
        print(e)

