import json
import matplotlib
import pandas as pd
import requests


endpoint = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny'
fields = 'record_date,tot_pub_debt_out_amt'
filters = 'record_date:gte:2021-08-01'

url = endpoint + f'?fields={fields}' + f'&filter={filters}'


response = requests.get(url)
j = json.loads(response.text)
df = pd.DataFrame(j['data'])

df['netChange'] = df['tot_pub_debt_out_amt'].astype(float) - df.shift(1)['tot_pub_debt_out_amt'].astype(float)

df.fillna(0, inplace = True)

print(
    df['netChange'].apply(lambda x: '${:.3f}B'.format((x/1_000_000_000))),
    '\n')

ax = df.tail(30).plot.bar(x='record_date', y='netChange')
