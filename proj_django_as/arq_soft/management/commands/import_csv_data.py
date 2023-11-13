import csv
import pandas as pd
from django.core.management.base import BaseCommand
from arq_soft.models import Stations

class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o banco de dados'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        df = pd.read_csv(csv_file_path)

        for _, row in df.iterrows():
            row_dict = row.to_dict()
            filtered_row = {key: value for key, value in row_dict.items() if key != 'id'}
            Stations.objects.create(**filtered_row)

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

