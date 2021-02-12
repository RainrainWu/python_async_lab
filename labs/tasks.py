from celery_tasks.celery import celery_app as app


@app.task
def add(x, y):
    return x + y


@app.task
def add_err(x, y):
    raise ValueError(f"Error raised by {self.name}")
    return x + y


@app.task
def add_rate_limit(x, y):
    return x + y


@app.task(
    bind=True,
    default_retry_delay=3,
    autoretry_for=(ValueError, ),
    retry_kwargs={"max_retries": 5,},
    retry_jitter=True,
)
def add_retry_success(self, x, y):
    if self.request.retries < 3:
        raise ValueError(f"Error raised by {self.name}")
    return x + y


@app.task(
    bind=True,
    default_retry_delay=3,
    autoretry_for=(ValueError, ),
    retry_kwargs={"max_retries": 5,},
    retry_jitter=True,
)
def add_retry_fail(self, x, y):
    raise ValueError(f"Error raised by {self.name}")
    return x + y


@app.task(
    bind=True,
    default_retry_delay=3,
    throws=(ZeroDivisionError, ),
    autoretry_for=(ValueError, ),
    retry_kwargs={"max_retries": 5,},
    retry_jitter=True,
)
def add_retry_throw(self, x, y):
    if self.request.retries == 2:
        raise ZeroDivisionError(f"Error raised by {self.name}")
    raise ValueError(f"Error raised by {self.name}")
    return x + y


@app.task
def add_route_foo(x, y):
    return x + y
