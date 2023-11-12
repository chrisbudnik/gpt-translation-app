import json
from typing import Dict, Tuple
from datetime import datetime
import pandas as pd
from google.cloud import bigquery
from config import Config
from auth import grant_access


def check_latest_campaigns() -> str:
    """Get the latest campaign name from BigQuery."""

    config = Config()
    bigquery_client = bigquery.Client()
    query = f"""
        SELECT 
            campaign_name 
        FROM 
            {config.BIGQEURY_MARKETING_TABLE_ID}
        ORDER BY
            campaign_name DESC, created_at DESC
        LIMIT
            1
    """
    query_result: pd.DataFrame = bigquery_client.query(query).to_dataframe()

    # if no campaigns found
    if query_result.empty:
        return "No campaigns found"
    
    return query_result["campaign_name"].values[0]


def save_to_bigquery(translation: Tuple) -> None:
    """
    Send formatted data to BigQuery.

    Parameters:
        report_data (list): The data to be inserted into BigQuery.
        table_id (str): The ID of the BigQuery table to insert data into.
    """
    config = Config()
    bigquery_client = bigquery.Client()

    table = bigquery_client.get_table(config.BIGQEURY_MARKETING_TABLE_ID)
    bigquery_client.insert_rows_json(table, [translation])

@grant_access
def save_translations_to_bigquery(
        campaign_name: str,
        translations_upload: dict[str: str],
    ) -> None:
    """Save translations to BigQuery."""

    upload_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for country, sales_copy in translations_upload.items():
        row_insert_data = {
            "campaign_name": campaign_name,
            "created_at": upload_datetime,
            "country": country,
            "sales_copy": sales_copy
        }
        save_to_bigquery(row_insert_data)
