from validate_email_address import validate_email
import pandas as pd
import time
FILE_NAME = 'hafio_hlidaci_emaily.xlsx'
# FILE_NAME = 'Databaze_firem_2021.xlsx'
RESULT_FILE = 'result.xlsx'
excel_data = pd.read_excel(FILE_NAME)
# data = pd.DataFrame(excel_data, columns=['E-mail']).to_dict('list')
data = pd.DataFrame(excel_data, columns=['Emaily']).to_dict('list')
valid = []
invalid = []
# for i in range(0, len(data['E-mail'])):
#     if validate_email(data['E-mail'][i], verify=True):
#         valid.append(data['E-mail'][i])
#     else:
#         invalid.append(data['E-mail'][i])
#     time.sleep(1)
for i in range(0, len(data['Emaily'])):
    valid.append(data['Emaily'][i]) if validate_email(data['Emaily'][i], verify=True) else invalid.append(data['Emaily'][i])
    time.sleep(0.5)

to_write = pd.DataFrame(valid, columns=['Valid e-mails'])
to_write.to_excel(RESULT_FILE, sheet_name='Valid e-mails', index=False)
