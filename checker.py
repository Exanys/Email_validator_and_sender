from validate_email_address import validate_email
import pandas as pd
import time


class Checker:
    file = ''
    result_name = ''
    columns = []
    email_col = ''
    valid = []
    invalid = []

    def __init__(self, file: str, result_name: str, columns: list, email_col: str):
        self.file = file
        self.result_name = result_name
        self.columns = columns
        self.email_col = email_col

    def get_data(self):
        excel_data = pd.read_excel(self.file)
        data = pd.DataFrame(excel_data, columns=self.columns).to_dict('list')
        return data

    def validate(self, data: list):
        for i in range(0, len(data[self.email_col])):
            if str(data[self.email_col][i]) != 'nan' and str(data[self.email_col][i]) != 'Neuvedeno' and str(data[self.email_col][i]) not in self.valid:
                # print(data[self.email_col][i])
                if validate_email(data[self.email_col][i], verify=True):
                    self.valid.append([data[self.columns[0]][i], data[self.email_col][i], data[self.columns[2]][i]])
                else:
                    self.invalid.append(data[self.email_col][i])
        self.valid.sort(key=lambda x: x[1])

    def save(self):
        to_write = pd.DataFrame(self.valid, columns=self.columns)
        to_write.to_excel(self.result_name, sheet_name='Valid e-mails', index=False)
        print(to_write)
        print(f'File {self.result_name} has been created!')

