import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#asctime = the time at which we run our code
#levelname = what type of logging we are doing(e.g. information log)
#modulename = the name of the module we are logging
#message = message we are logging
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")#"running_logs.log is the name of the log file"
os.makedirs(log_dir, exist_ok=True)
#exist_ok = True it means even if the directory exists, it will no raise any exception.



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),#to show logging info in file
        logging.StreamHandler(sys.stdout)#to show logging info in terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")