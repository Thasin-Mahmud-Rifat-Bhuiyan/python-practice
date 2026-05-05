import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler (writes logs to a file)
file_handler = logging.FileHandler("mylog.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Console handler (prints logs to terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter (defines log message format)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example log messages
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")

try:
    a = 5
    a / 0
except ZeroDivisionError:
    logger.exception("Zero division error occurred")

logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")
