import logging
import os
from datetime import datetime

# Define the logs directory and create it
logs_path = "logs"
os.makedirs(logs_path, exist_ok=True)

# Create a filename with timestamp
log_file_path = os.path.join(logs_path, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Set up logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s"
)

# Return logger object
def get_logger(name=__name__):
    return logging.getLogger(name)
