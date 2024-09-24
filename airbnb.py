# Import necessary packages
import pandas as pd
import numpy as np

df_review = pd.read_csv('airbnb_last_review.tsv', delimiter='\t')
df_price= pd.read_csv('airbnb_price.csv')
df_room = pd.read_excel('airbnb_room_type.xlsx')

# Join the three data frames together into one
listings = pd.merge(df_review , df_price, on='listing_id')
listings = pd.merge(listings, df_room, on='listing_id')

# What are the dates of the earliest and most recent reviews?
listings['last_review_date'] = pd.to_datetime(listings['last_review'], format='%B %d %Y')
first_reviewed = listings['last_review_date'].min()
last_reviewed = listings['last_review_date'].max()

#How many of the listings are private rooms?

listings['room_type'] = listings['room_type'].str.lower()
private_room_count = listings[listings['room_type'] == 'private room'].shape[0]

# What is the average listing price?

listings['price_clean'] = listings['price'].str.replace(' dollars', '').astype(float)
avg_price = listings['price_clean'].mean()

review_dates = pd.DataFrame({
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [private_room_count],
    'avg_price': [round(avg_price, 2)]
})

print(review_dates)

