import logging


def setup_logging(path: str):
    logging.basicConfig(
        filename=path,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
