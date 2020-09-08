from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines 
from .webservice_stage import WebServiceStage

class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = pipelines.CdkPipeline(self, 'PipelineToy',
            cloud_assembly_artifact=cloud_assembly_artifact,
            pipeline_name='WebinarPipeline',
            source_action= cpactions.GitHubSourceAction(
                action_name='Github',
                output= source_artifact,
                oauth_token= core.SecretValue.secrets_manager('GitHub_cdk_workshop'),
                owner='JuanGQCadavid',
                repo='cdkAwsPipe',
                trigger=cpactions.GitHubTrigger.POLL),
            synth_action= pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                synth_command='cdk synth')
            )

        pipeline.add_application_stage(WebServiceStage(self,'Pre-Prod', env={
            'region':'eu-central-1'
        }))
