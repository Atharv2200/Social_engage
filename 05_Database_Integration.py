import pandas as pd
import pymysql
import uuid

connection = pymysql.connect(host='localhost', user='root', password='root123')
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS social_engage_db")
cursor.execute("USE social_engage_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS content_performance (
    video_id VARCHAR(50) PRIMARY KEY,
    topic_category VARCHAR(100),
    video_length_seconds INT,
    format_type VARCHAR(50),
    total_views INT, total_likes INT, total_shares INT, total_saves INT,
    published_date TIMESTAMP
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS audience_comments (
    comment_id VARCHAR(100) PRIMARY KEY,
    video_id VARCHAR(50),
    author_name VARCHAR(100),
    raw_comment TEXT,
    sentiment_tag VARCHAR(50),
    reply_count INT,
    FOREIGN KEY (video_id) REFERENCES content_performance(video_id)
)""")

cursor.execute("INSERT IGNORE INTO content_performance (video_id, topic_category) VALUES ('TEST_VID_01', 'Portfolio Demo')")
connection.commit()

df = pd.read_csv('sentiment_tagged_data_sample.csv')
df['comment_id'] = [str(uuid.uuid4())[:8] for _ in range(len(df))]
df['video_id'] = 'TEST_VID_01'

print("Uploading NLP data to MySQL database...")
try:
    for index, row in df.iterrows():
        sql = "INSERT IGNORE INTO audience_comments (comment_id, video_id, author_name, raw_comment, sentiment_tag, reply_count) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (row['comment_id'], row['video_id'], row['Author'], row['Comment'], row['Sentiment_Tag'], row['Reply Count'])
        cursor.execute(sql, values)
    
    connection.commit()
    print("✅ Pipeline sync complete! Data is now live in MySQL Workbench.")
except Exception as e:
    print(f"Error: {e}")
finally:
    connection.close()