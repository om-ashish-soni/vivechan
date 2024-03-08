import os
from dotenv import load_dotenv
from datasets import load_dataset

def load_text_dataset():
    load_dotenv()
    # REPLACE WITH YOUR HUGGING FACE ACCOUNT TOKEN ( Go to settings and get access token from hugging face)
    hf_token = os.getenv("HF_TOKEN")
    # HF_DATASET_CHECKPOINT=om-ashish-soni/shiv-mahapurana-text
    dataset_checkpoint=os.getenv("HF_DATASET_CHECKPOINT")
    
    print("Starting dataset loading ........... ")
    dataset = load_dataset(dataset_checkpoint,token=hf_token)
    print("Done dataset loading ........... ")
    texts=dataset['train']['text']
    return texts
    