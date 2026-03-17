from search_engine import search_topic
from scraper import scrape_content
from cleaner import clean_text
from storage import save_data

def run_pipeline(topic):

    print("Step 1: Searching topic")

    url = search_topic(topic)

    print("URL:", url)

    print("Step 2: Scraping content")

    raw_data = scrape_content(url)

    print("Raw length:", len(raw_data))

    print("Step 3: Cleaning data")

    cleaned = clean_text(raw_data)

    print("Cleaned length:", len(cleaned))

    print("Step 4: Saving data")

    save_data(topic, cleaned)

    print("Pipeline completed")

if __name__ == "__main__":

    run_pipeline("Deep Learning")