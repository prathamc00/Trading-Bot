import logging

def init_logger():
    logging.basicConfig(
        filename="trading.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
