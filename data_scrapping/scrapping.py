from google_play_scraper import reviews, Sort
import pandas as pd
from pathlib import Path

# target data Gojek App
app_id = 'com.gojek.app'

all_reviews = []
count = 0
target = 70000  # total data

continuation_token = None

while count < target:
    result, continuation_token = reviews(
        app_id,
        lang='id',
        country='id',
        sort=Sort.NEWEST,
        count=200,
        continuation_token=continuation_token
    )

    if not result:
        break

    for r in result:
        all_reviews.append({
            'review': r['content'],
            'score': r['score']
        })

    count = len(all_reviews)
    print(f"Collected: {count}")

    if continuation_token is None:
        break

df = pd.DataFrame(all_reviews)

# save to csv
output_dir = Path(__file__).resolve().parents[1] / "dataset"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "gojek_reviews.csv"

df.to_csv(output_file, index=False)

print(f"Scraping selesai!")
print(f"Total Data: {len(all_reviews)}")