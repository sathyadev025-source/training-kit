import requests, zipfile, io, json, os
import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2
import logging

# --- LOGGING SETUP ---
logging.basicConfig(level=logging.INFO)

# --- 1. SETTINGS ---
RAW_DIR ="/home/sathya/projects/training-kit/data/raw"
os.makedirs(RAW_DIR, exist_ok=True)
DB_URL = 'postgresql://postgres:postgres@localhost:5432/cricket_db'
engine = create_engine(DB_URL)

# --- 2. EXTRACTION ---
logging.info("Step 1: Downloading data...")
url = "https://cricsheet.org/downloads/t20s_json.zip"
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(RAW_DIR)
logging.info("✅ Files unzipped!")

# --- 3. TRANSFORMATION LOGIC ---
def transform_match(file_path, file_name):
    with open(file_path) as f:
        data = json.load(f)
    records = []
    m_id = file_name.replace(".json", "")
    for inning in data.get('innings', []):
        team = inning.get('team')
        for over in inning.get('overs', []):
            o_num = over.get('over')
            for delivery in over.get('deliveries', []):
                records.append({
                    'match_id': m_id,
                    'batting_team': team,
                    'over': o_num,
                    'batter': delivery.get('batter'),
                    'bowler': delivery.get('bowler'),
                    'runs': delivery.get('runs', {}).get('batter', 0)
                })
    return pd.DataFrame(records)

# --- 4. LOADING ---
all_files = [f for f in os.listdir(RAW_DIR) if f.endswith('.json') and f[0].isdigit()]
logging.info("Step 2: Loading matches into PostgreSQL...")

with engine.connect() as conn:
    for file in all_files[:100]:
        try:
            logging.info(f"Processing file: {file}")
            df = transform_match(os.path.join(RAW_DIR, file), file)
            df.to_sql('ball_by_ball', conn, schema='public', if_exists='append', index=False)
        except Exception as e:
            logging.error(f"Error processing {file}: {e}")
            continue

logging.info("✅ Data pushed and PERMANENTLY SAVED to Postgres!")

# --- 5. EXPORT TO CSV ---
logging.info("Step 3: Creating CSV report...")
try:
    query = text("SELECT * FROM public.ball_by_ball LIMIT 1000")

    with engine.connect() as conn:
        df_all = pd.read_sql(query, conn)

    df_all.to_csv("final_stats.csv", index=False)
    logging.info("✅ CSV report 'final_stats.csv' created!")
except Exception as e:
    logging.error(f"❌ CSV Step failed: {e}")

logging.info("✅ ALL DONE!")
