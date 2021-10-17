import json
import matplotlib
import pandas as pd
import requests

#https://fiscaldata.treasury.gov/api-documentation/
endpoint = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny'
fields = 'record_date,tot_pub_debt_out_amt'
filters = 'record_date:gte:2021-08-01'

url = endpoint + f'?fields={fields}' + f'&filter={filters}'


response = requests.get(url)
j = json.loads(response.text)
df = pd.DataFrame(j['data'])
df.set_index('record_date', inplace=True)


#Population estimates, July 1, 2019, (V2019) [US Census Bureau]
population = 328_239_523

df['netChange'] = df['tot_pub_debt_out_amt'].astype(float) - df.shift(1)['tot_pub_debt_out_amt'].astype(float)
perCapitaDebtChangeOctober14 = df.loc['2021-10-14']['netChange']

result = perCapitaDebtChangeOctober14 / population
debtChange = '${:.2f}'.format(result)

print(f'On October 14, 2021 the nation\'s debt ceiling was raised and every man, woman and child suddenly owed an additional {debtChange} in federal debt')
