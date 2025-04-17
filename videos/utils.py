import csv
from pathlib import Path
import dateutil.parser

CSV_FILE = Path(__file__).resolve().parent / 'videos.csv'
FIELDS = ['source_post_id', 'post_url', 'post_description',
          'post_created', 'likes_count', 'shares_count',
          'views_count', 'comments_count']


def read_videos():
    videos = []
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            video = map_fields_to_api_format(row)
            videos.append(video)
    return videos


def write_videos(data):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
        writer.writeheader()

        formatted_videos = [map_fields_to_csv_format(video) for video in data]
        writer.writerows(formatted_videos)


def format_date(date_str):
    """
    Convert date from M/D/YY to YYYY-MM-DD format
    """
    try:
        return str(dateutil.parser.parse(date_str).date())
    except ValueError:
        return date_str


def map_fields_to_api_format(row):
    """
    Map original CSV fields to required CSV schema for the API
    """
    return {
        "id": row["source_post_id"],
        "name": row["post_description"],
        "href": row["post_url"],
        "post_date": format_date(row["post_created"]),
        "views_count": int(row["views_count"]),
    }


def map_fields_to_csv_format(video):
    """
    Map API fields back to original CSV fields
    """
    return {
        "source_post_id": video["id"],
        "post_url": video["href"],
        "post_description": video["name"],
        "post_created": video["post_date"],
        "likes_count": "0",
        "shares_count": "0",
        "views_count": str(video["views_count"]),
        "comments_count": "0",
    }
