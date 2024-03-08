import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

def load_encoder():
    load_dotenv()
    # REPLACE WITH YOUR HUGGING FACE ACCOUNT TOKEN ( Go to settings and get access token from hugging face)
    hf_token = os.getenv("HF_TOKEN")
    # HF_ENCODER_CHECKPOINT=all-mpnet-base-v2
    encoder_checkpoint=os.getenv('HF_ENCODER_CHECKPOINT')
    print("encoder_checkpoint : ",encoder_checkpoint)
    print("Starting loading Encoder .......")
    Encoder=SentenceTransformer(encoder_checkpoint,token=hf_token)
    print("Done loading Encoder .......")
    return Encoder


