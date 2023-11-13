import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records')

if __name__ == "__main__":
    csv_file_path = "/home/leodedeus/Downloads/basebikes/df_stations.csv"
    json_file_path = "/home/leodedeus/django_proj/proj_as/proj_django_as/arq_soft/fixtures/df_station.json"

    csv_to_json(csv_file_path, json_file_path)
