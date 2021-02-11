from loguru import logger

from labs.tasks import add_route_foo

my_task = add_route_foo.delay(4, 4)
logger.info(f"Task result: {my_task.get(timeout=10)}")
