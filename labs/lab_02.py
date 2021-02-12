import time

from loguru import logger

from labs.tasks import add_err

my_task = add_err.delay(4, 4)
logger.debug(f"Task ready: {my_task.ready()}")
time.sleep(1)
logger.debug(f"Task ready: {my_task.ready()}")
logger.warning(f"Task traceback: {my_task.traceback}")
# logger.debug(f"Task result: {my_task.get(timeout=1)}")
