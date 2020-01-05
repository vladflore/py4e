import time

import pandas as pd

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

start_time = None
foodfacts = None
try:
    print('loading csv...')
    start_time = time.time()
    foodfacts = pd.read_csv('en.openfoodfacts.org.products.csv', sep='\t', low_memory=False)
    print('loaded in', (time.time() - start_time), 'seconds')
    start_time = time.time()
    print('processing csv...')
except FileNotFoundError:
    print(
        '{} seems not to exist, if so download it from >https://de.openfoodfacts.org/data< and put it beside this '
        'python file'.format(
            'en.openfoodfacts.org.products.csv'))
    exit()
# foodfacts = pd.read_csv('en.openfoodfacts.org.products.csv', sep='\t', usecols=['',''])
# countries = foodfacts[['countries']].head()
# print(countries)
# print(type(countries))
# uniques_countries = foodfacts['countries'].unique()
# for country in uniques_countries:
#     print(country)

product_name_not_null = foodfacts['product_name'].notnull()
countries_not_null = foodfacts['countries'].notnull()


def areCountriesInList(countries_to_search_for, countries):
    if countries_to_search_for is None or countries is None:
        return False
    countries_str = str(countries)
    if not countries_str.isalpha():
        return False
    countries_str = countries_str.lower()
    return any(country.lower() in countries_str
               for country in countries_to_search_for)


product_sold_in_countries = foodfacts.apply(
    lambda dataset: areCountriesInList(['France'], dataset['countries']), axis=1)

res = foodfacts[product_name_not_null & product_sold_in_countries][
    ['product_name', 'countries', 'saturated-fat_100g', 'proteins_100g']]
res_sorted = res.sort_values(by=['saturated-fat_100g'], ascending=False, na_position='last')
print('processed in', (time.time() - start_time), 'seconds')
print(res_sorted.head(200))
print(res_sorted.shape)

# Romania or România 742
# Germany or Deutschland 14203
# France 409772
