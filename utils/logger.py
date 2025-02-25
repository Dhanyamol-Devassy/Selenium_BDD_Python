# utils/logger.py

import logging
import os
from datetime import datetime
    
def get_logger():
    """
    Set up and return a logger for the test execution.
    """
    log_dir = 'logs'
    # Create the logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
            print(f"Log directory created at: {log_dir}")
        except Exception as e:
            print(f"Error creating log directory: {e}")
            raise

    # Create a log file with a timestamp
    log_file = os.path.join(log_dir, f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

    # Create logger
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create a console handler for real-time logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Set up a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

