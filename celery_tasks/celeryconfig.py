import os

result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost")
broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]

task_default_rate_limit = "10/s"
result_backend_max_retries = "5"
broker_transport_options = {
    "queue_order_strategy": "priority",
}

task_annotations = {
    "labs.tasks.add_rate_limit": {"rate_limit": "1/s"},
}

task_routes = {
    "labs.tasks.add_route_foo": {"queue": "foo",},
    "labs.tasks.add_priority_high": {"queue": "priority", "priority": 0,},
    "labs.tasks.add_priority_low": {"queue": "priority", "priority": 9,},
    "labs.tasks.add_critical": {"queue": "critical",},
}
