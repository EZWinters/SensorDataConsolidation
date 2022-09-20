import os
from pathlib import Path

import pandas as pd


class DataConsolidation:
    def generate_path(self, sensor, subject):
        path = 'SensorData/' + sensor + '/' + subject
        return path

    def get_filename_list(self, sensor, subject):
        path = self.generate_path(sensor, subject)
        list_of_files = os.listdir(path)
        return list_of_files

    def consolidate_data(self, sensor, subject):
        print('Consolidating data for...', sensor, '....and subject...', subject)
        filenames = self.get_filename_list(sensor, subject)
        filepath_prefix = 'SensorData/' + sensor + '/' + subject + '/'
        filepaths = [filepath_prefix + x for x in filenames]
        df = pd.concat(map(pd.read_csv, filepaths), ignore_index=True)
        output_path = Path('Output/consolidated_data.csv')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path)
        print("Consolidated data is available in Output folder")
