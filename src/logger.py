#it is used of the purpose that any execution happens we have to have the info about it and track it

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    #best format
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # 
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has Started")

'''where ever we use logging.info and write any print message
if uses the specified basic config to create the the filename and use the 
specified format'''