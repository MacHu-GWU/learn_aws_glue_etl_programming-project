# -*- coding: utf-8 -*-

from chalice import Chalice
from learn_aws_glue_etl_programming.lbd import hello

app = Chalice(app_name="learn_aws_glue_etl_programming")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.high_level_api(event, context)
