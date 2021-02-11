from loguru import logger

from labs.tasks import add_retry_success

my_task = add_retry_success.delay(4, 4)
logger.info(f"Task result: {my_task.get(timeout=10)}")
