import logging
import time

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("ETL Job Started")
    time.sleep(2)
    logging.info("Extracting data...")
    time.sleep(2)
    logging.info("Transforming data...")
    time.sleep(2)
    logging.info("Loading data...")
    time.sleep(2)
    logging.info("ETL Job Completed Successfully")

if __name__ == "__main__":
    main() #
