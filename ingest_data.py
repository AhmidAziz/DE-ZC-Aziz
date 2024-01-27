import argparse
import pandas as pd
import os
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time, sleep

def main(params):
    user = "root"
    password = "root"
    host = "pgdatabase"
    port = "5432"
    db = params.db
    table = params.table
    url = params.url
    file_name = url.split('/')[-1]
    
    print(user,password,host,port,db,table,url,file_name)
    
    # download csv from URL using wget
    os.system(f'wget {url} -O {file_name}')

    # postgresql://root:root@localhost:5432/ny_taxi
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    if file_name.endswith('.parquet'):
        pf = pq.read_table(file_name)
        data = pf.to_pandas()
    elif file_name.endswith('.csv') or file_name.endswith('.csv.gz'):
        data = pd.read_csv(file_name, compression='infer')
    else:
        print(f'Unsupported file format: {file_name}')
        return

    df_len = data.shape[0]

    # Data Definition Language (DDL): defines the schema
    print(pd.io.sql.get_schema(data, name=table, con=engine))

    chunk_size = 100000
    chunk_count = 0
    chunks = [data.iloc[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    for df in chunks:
        chunk_count += chunk_size
        if chunk_count >= df_len:
            completion = 100
        else:
            completion = (chunk_count/df_len) * 100
        t_start = time()
        df.to_sql(name=table, con=engine, if_exists='append')
        t_end = time()
        print(f'inserted another chunk, took {(t_end-t_start):.3f} seconds. {completion:.3f} % Complete.') 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    #password, host, port, database name, table name, url of the csv

    parser.add_argument('--db', help='database name')
    parser.add_argument('--table', help='name of the tabler')
    parser.add_argument('--url', help='url of the csv')                   

    args = parser.parse_args()

    main(args)
