import time
from labs.tasks import add

result = add.delay(4, 4)
print(result.ready())
time.sleep(1)
print(result.ready())
print(result.get(timeout=1))
print(result.ready())
