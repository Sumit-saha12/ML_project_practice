import logging
from datetime import datetime

logging.basicConfig(
    filename=f"logs/{datetime.now()}.log",
    filemode='w',
    format="%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
 
    level= logging.INFO
)