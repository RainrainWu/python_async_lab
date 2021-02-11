import time

from loguru import logger

from labs.tasks import add

my_task = add.delay(4, 4)
logger.debug(f"Task ready: {my_task.ready()}")
time.sleep(1)
logger.debug(f"Task ready: {my_task.ready()}")
logger.debug(f"Task result: {my_task.get()}")
