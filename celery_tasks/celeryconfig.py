result_backend = "redis://localhost"
broker_url = "redis://localhost:6379/0"

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]

task_default_rate_limit = "10/s"
result_backend_max_retries = "5"

task_annotations = {
    "labs.tasks.add_rate_limit": {"rate_limit": "1/s"},
}

task_routes = {
    "labs.tasks.add_route_foo":{
        "queue": "foo",
    },
}
