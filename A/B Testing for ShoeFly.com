import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source = ad_clicks\
  .groupby(['utm_source', 'is_click'])\
  .user_id.count()\
  .reset_index()

clicks_pivot = clicks_by_source\
  .pivot(index='utm_source',
         columns='is_click',
         values='user_id')\
  .reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked'] = \
  clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

ad_counts = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ad_counts)

clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

clicks_pivot_group = clicks_by_group.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()

clicks_pivot_group['percent_clicked'] = clicks_pivot_group[True] / (clicks_pivot_group[True] + clicks_pivot_group[False])

print(clicks_pivot_group)
print()

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_group = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_group = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

a_clicks_pivot = a_clicks_group.pivot(index = 'day',
            columns = 'is_click',
            values = 'user_id').reset_index()
b_clicks_pivot = b_clicks_group.pivot(index = 'day',
            columns = 'is_click',
            values = 'user_id').reset_index()

a_clicks_pivot['percentage_clicked'] = a_clicks_pivot[True] /(a_clicks_pivot[True] + a_clicks_pivot[False])
b_clicks_pivot['percentage_clicked'] = b_clicks_pivot[True] /(b_clicks_pivot[True] + b_clicks_pivot[False])

print(a_clicks_pivot)
print()
print(b_clicks_pivot)

