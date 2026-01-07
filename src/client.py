import boto3
from langchain_aws import ChatBedrock
from dotenv import load_dotenv

load_dotenv()


def create_client(region="us-east-1"):
    """Create and return a Bedrock runtime client."""
    return boto3.client(
        service_name="bedrock-runtime",
        region_name=region
    )


def create_llm(client, model_id="us.amazon.nova-lite-v1:0"):
    """Create and return a ChatBedrock LLM instance."""
    return ChatBedrock(
        model_id=model_id,
        client=client,
        model_kwargs={"temperature": 0.7}
    )
