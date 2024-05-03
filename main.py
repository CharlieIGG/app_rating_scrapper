import pandas as pd
import numpy as np

from app_store_scraper import AppStore
from ios_app_data import app_list

# Create an empty DataFrame to store the data
df = pd.DataFrame()

# Iterate over the app_list
for app in app_list:
    # Create an instance of AppStore for each app
    data_source = AppStore(country="de", app_name=app["app_name"], app_id=app["app_id"])

    # Fetch the reviews for each app
    data_source.review(how_many=1000)

    # Convert the data to a pandas DataFrame
    base_df = pd.DataFrame(np.array(data_source.reviews), columns=['review'])
    app_df = base_df.join(pd.DataFrame(base_df.pop('review').tolist()))
    # Add an extra column for the app_name
    app_df['app_name'] = app["app_name"]

    # concat the app_df to the main DataFrame
    df = pd.concat([df, app_df])

# Save the data to a CSV file
df.to_csv('data.csv', index=False, sep=';', encoding='utf-8')