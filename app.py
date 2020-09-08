#!/usr/bin/env python3

from aws_cdk import core

from pipelines_webinar.pipelines_webinar_stack import PipelinesWebinarStack
from pipelines_webinar.pipeline_stack import PipelineStack

app = core.App()
PipelinesWebinarStack(app, "pipelines-webinar")
PipelineStack(app,'PipelineStack', env = {
    'region':'eu-central-1'
})
app.synth()
