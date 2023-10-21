import yaml
import os, sys
import pandas as pd

def write_schema_yaml(csv_file):
    df = pd.read_csv(csv_file)

    number_of_cols = len(df.columns)

    columns_name = df.columns.to_list()

    column_dtypes = df.dtypes.astype(str).to_list()

    # Create schema dictionary
    schema = {
        "filename" : os.path.basename(csv_file),
        "NumberOfColumns" : number_of_cols,
        "ColumnsNames" : dict(zip(columns_name, column_dtypes))
    }

    # write schema to schema.yaml file

    ROOT_DIR = os.getcwd()
    SCHEMA_FILE_PATH = os.path.join(ROOT_DIR, 'config', 'schema.yaml')

    with open (SCHEMA_FILE_PATH, 'w') as schema_file:
        #yaml.dump(value,file_name)
        yaml.dump(schema, schema_file)

