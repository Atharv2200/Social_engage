# 🚀 Social Engagement Analytics Engine

Hey! Thanks for checking out my project. I built this pipeline to figure out what actually makes social media content resonate with people, rather than just staring at raw view counts. 

This is a full end-to-end data engineering project. It takes raw YouTube comments, runs them through an NLP sentiment analyzer, dumps the structured data into a local MySQL database, and serves up the insights on a clean Streamlit dashboard. 

## The Stack
* **Python** (Pandas for the heavy data lifting)
* **NLTK / VADER** (NLP sentiment tagging)
* **MySQL** (Relational data storage)
* **Streamlit** (Interactive frontend)

## How it actually works
1. **The Data Prep:** Grabs raw comment data and cleans it up.
2. **The Brain:** Runs NLP over thousands of text rows to tag whether comments are "Relatable," "Neutral," etc. 
3. **The Storage:** I wrote a Python script (`05_Database_Integration.py`) that uses `pymysql` to automatically hook into a local MySQL server, spin up the `social_engage_db` schema from scratch, and bulk-insert the data. I wanted to build this like a real production app, which meant moving past just relying on CSVs.
4. **The Dashboard:** Streamlit queries the finished data to show A/B test results, engagement ratios, and trend forecasts.

## Getting it running on your machine
1. Make sure your local MySQL server is actually running.
2. Clone this repo.
3. Open `05_Database_Integration.py` and swap `YOUR_PASSWORD` with your local root password.
4. Run `python 05_Database_Integration.py` to build the database architecture and inject the data.
5. Launch the UI with `python -m streamlit run app.py`.

## Real Talk: The Biggest Challenge
Honestly, the hardest part wasn't the machine learning—it was getting the database pipeline totally bulletproof. I actually managed to lock myself out of my own local MySQL server during development because of a background service conflict. I had to drop into the Windows command line, force-kill the ghost processes, bypass the grant tables, and manually rebuild my admin privileges. 

It was a headache, but it forced me to write much better exception handling in my Python-to-SQL script so that it fails gracefully if the server is offline, rather than just crashing.
