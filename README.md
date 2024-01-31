# Twitter ETL Mini Project using Apache Airflow

This mini project showcases a simple ETL (Extract, Transform, Load) pipeline using Apache Airflow to fetch and refine tweets from Twitter. The pipeline consists of two main components: a DAG (Directed Acyclic Graph) definition file (`twitter_dag.py`) and an ETL script (`twitter_etl.py`).

## Files

1. **twitter_dag.py**
   - Python script defining an Apache Airflow DAG.
   - The DAG schedules the execution of the ETL process (`twitter_etl.py`) on a daily basis.
   - Uses a PythonOperator to run the ETL script.

2. **twitter_etl.py**
   - Python script containing the ETL logic.
   - Utilizes the Tweepy library to connect to the Twitter API.
   - Fetches recent tweets from a specified user (e.g., '@elonmusk').
   - Extracts relevant information from each tweet.
   - Creates a Pandas DataFrame and saves it to a CSV file named 'refined_tweets.csv'.

## Notes

- The DAG is scheduled to run the ETL process daily, fetching and refining tweets from the specified Twitter user.

- The refined tweet data is currently saved to a local CSV file (`refined_tweets.csv`). If you want to save it to an S3 bucket, additional configurations are required in the `twitter_etl.py` script.

- Ensure that you have configured the necessary environment variables or API keys to connect to the Twitter API.
