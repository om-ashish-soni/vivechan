import os
from dotenv import load_dotenv
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
# from util import get_device


def load_llm():
    load_dotenv()
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype=torch.bfloat16
    # )
    # device=get_device()
    # print("device : ",device)
    # model_id=os.getenv('HF_LLM_CHECKPOINT')
    # print("model_id",model_id)
    # print("Start Loading LLM .....")
    # # LLM_Model=AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config)
    # LLM_Model=AutoModelForCausalLM.from_pretrained(model_id)
    # LLM_Model=LLM_Model.to(device)
    # print("Done Loading LLM .....")
    # return LLM_Model

load_dotenv()
# REPLACE WITH YOUR HUGGING FACE ACCOUNT TOKEN ( Go to settings and get access token from hugging face)
hf_token=os.getenv('HF_TOKEN')
def query(payload):
    
    import requests

    # API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

    headers = {"Authorization": "Bearer "+hf_token}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def infer(Query,Context):
  try:
      # Prefix="Giving you 'Query' Below Answer appropriate based on Given 'Context'"
      Prefix="Hello, Spiritual Vivechan Expert, Answer appropriately for given 'Query' based on Given 'Context' provided"

      # Query="Who are you? and Who am I?"
      # Context="Mistral"
      output = query({
          "inputs": f"""
          <s>[INST] 
    {Prefix}
    
    'Query' : {Query}
    'Context' : {Context}
    [/INST]
    Model answer</s>
          """,
          "parameters": 
        {
          "contentType": "application/json",
          "max_tokens": 1000,
          "min_tokens": 1000,
          "return_full_text": False
        }
      })

      print("output generated",output)

      return output[0]['generated_text']
  except Exception as e:
        print(f"An error occurred: {e}")
        return f"could not generate answer Due to Error, please try after some time ,{e} "  

