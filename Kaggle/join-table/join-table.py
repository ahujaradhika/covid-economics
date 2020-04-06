import pandas as pd
import json
import numpy as np

base_path = 'country_by_date'

def add_column(new_path, base_path, new_col_name, base_col_name, col_pos, new_name):
    base_data = pd.read_csv(base_path + '.csv')
    new_data = pd.read_csv(new_path + '.csv')
    new_col = []
    for index, row in base_data.iterrows():
        i = new_data[new_col_name] == row[base_col_name]
        try:
            new_col.append(new_data[i].iloc[0, col_pos])
        except:
            new_col.append(np.nan)
    base_data[new_name] = new_col
    base_data.to_csv(base_path + '_updated.csv')

# get total testing
tot_testing_path = 'datasets/data_total_testing'
add_column(tot_testing_path, base_path, 'entity', 'Country_Region', 2, 'Total Testing')

# get hdi
hdi_path = 'datasets/data_hdi'
add_column(hdi_path, base_path, 'Country', 'Country_Region', 2, 'HDI')

# get population density
pop_density_path = 'datasets/data_population_density'
add_column(pop_density_path, base_path, 'Country Name', 'Country_Region', 62, 'Population Density')


