import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(
    filename='logs.log',
    encoding='utf-8',
)

formatter = handler.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)

logger.addHandler(handler)

# logger.debug("test")
