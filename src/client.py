import os
import boto3
from dotenv import load_dotenv
from langchain_aws import ChatBedrock

def create_client():
    """Create AWS Bedrock client"""
    load_dotenv()
    
    return boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )

def create_llm(client=None):
    """Create LLM instance"""
    if client is None:
        client = create_client()
    
    return ChatBedrock(
        model_id="us.amazon.nova-lite-v1:0",
        client=client,
        model_kwargs={
            "max_tokens": 1500,
            "temperature": 0.7
        }
    )
