import time
import random

from loguru import logger

from labs.tasks import add_priority_low, add_priority_high, add_critical

ticker = 0

while True:
    if ticker % 11 == 0:
        task_amount = random.randint(20, 40)
        for i in range(task_amount):
            add_priority_low.apply_async((1, 1))
        logger.info(f"Send {task_amount} add_priority_low to broker")
        task_amount = random.randint(20, 40)
        for i in range(task_amount):
            add_priority_high.apply_async((2, 2))
        logger.info(f"Send {task_amount} add_priority_high to broker")

    if ticker % 13 == 0:
        task_amount = random.randint(10, 20)
        for i in range(task_amount):
            add_critical.apply_async((2, 2))
        logger.info(f"Send {task_amount} add_critical to broker")

    time.sleep(1)
    ticker += 1
