# fedDebtCeiling
$911.91 was added to YOUR portion of the federal debt last week on just one day! Is that true? Let's test it out in Python using high quality federal data sources

Python test framework - https://github.com/mojo-py/fedDebtCeiling
The code is short enough at about 25 lines to serve as it's own documentation, and includes a link to the official API documentation from Treasury Dept.


In this short script, we take the following steps:

1) Construct a parametized url
2) using the url, making a GET request from the US Treasury 'debt_to_penny' API endpoint
3) loading the response data into JSON
4) passing that response to create a pandas DataFrame object
5) shifting the dataframe back by 1 day to make a calculated column called ['netChange'] which is net daily debt change ie todays debt - yesterdays debt = df['netChange
6) Calculating the quotient of the numerator (net daily debt change or $299,000,000,000) over the denominator, total USA population(population=328_239_523)
7) population / df.loc['2021-10-14']['netChange'] = result
8) apply string formatting to result and interpolate result into f-string and print it

## evaluates as TRUE

Sources - >

US Census Bureau Population estimates, July 1, 2019, (V2019)
U.S. Department of the Treasury FiscalData Rest API https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?fields=record_date,tot_pub_debt_out_amt&filter=record_date:gte:2021-08-01
