import time

from loguru import logger

from labs.tasks import add_rate_limit

TASKS_AMOUNT = 15

tasks_list = []
for i in range(TASKS_AMOUNT):
    tasks_list.append(add_rate_limit.delay(i, i))

for i in range(TASKS_AMOUNT):
    logger.debug(f"All tasks state: {[task.state for task in tasks_list]}")
    time.sleep(1)
