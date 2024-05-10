import pandas as pd
import numpy as np

from app_store_scraper import AppStore
from ios_app_data import app_list
from utils.issue_extractor import extract_issues

# Create an empty DataFrame to store the data
reviews_df = pd.DataFrame()
issues_df = pd.DataFrame(columns=['issue_type', 'date', 'app', 'review'])

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
    reviews_df = pd.concat([reviews_df, app_df])
    
    # Process each review to extract issues
    for index, row in app_df.iterrows():
        issues = extract_issues(row['review'])
        for issue in issues:
            issue_record = {
                'issue_type': issue,
                'date': row['date'],
                'app': row['app_name'],
                'review': row['review']
            }
            issues_df = issues_df.append(issue_record, ignore_index=True)

# Save the data to a CSV file
reviews_df.to_csv('reviews.csv', index=False, sep=';', encoding='utf-8')


