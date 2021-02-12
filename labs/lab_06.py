from loguru import logger

from labs.tasks import add_retry_throw

my_task = add_retry_throw.delay(4, 4)
logger.info(f"Task result: {my_task.get(timeout=10)}")
