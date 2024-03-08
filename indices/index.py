import faiss
import os
from dotenv import load_dotenv

def load_index():
    load_dotenv()
    # FAISS_INDEX_FILE_PATH=indices/shiv-mahapuran-sankshipt.faiss
    index_file_path=os.getenv('FAISS_INDEX_FILE_PATH')
    print("Starting Loading Index .....")
    VectorIndex=faiss.read_index(index_file_path)
    print("Done Loading Index .....")
    return VectorIndex
