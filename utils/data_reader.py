import csv
import os


def read_login_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'login_data.csv')
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
