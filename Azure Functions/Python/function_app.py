import logging
import azure.functions as func
import time
from multiprocessing import current_process
from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import get_logger
import time
import os
import socket

app = func.FunctionApp()

@app.schedule(schedule="0 0 */6 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def main(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    logger = get_logger()
    # configure a stream handler
    logger.addHandler(logging.StreamHandler())
    # log all messages, debug and up
    logger.setLevel(logging.INFO)
    # get the current process
    process = current_process()
    processes = cpu_count()
    print ('utilizing %d cores\n' % processes)
    pool = Pool(processes)
    pool.map(f, range(processes))
        

def f(x):
    logger = get_logger()
    # configure a stream handler
    logger.addHandler(logging.StreamHandler())
    # log all messages, debug and up
    logger.setLevel(logging.INFO)
    # get the current process
    process = current_process()
    set_time = 50
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    i=0
    while True:
        i += 1
        logger.info(f"Hostname:- {socket.gethostname()} App Name: {os.environ.get('WEBSITE_SITE_NAME')} Counter: {i}")
        if time.time() > timeout:
            break
        x*x

