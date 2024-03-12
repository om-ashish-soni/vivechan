from util import generate_unique_audio_filename,delete_temp_audio,generate_context,display_footer,write_answer
from text_to_speech import speak
from dataset.dataset import load_text_dataset
from indices.index import load_index
from encoder.encoder import load_encoder
from LLM.LLM import infer
import streamlit as st
import textwrap
import time
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

k=10
max_line_length = 80

def main():
    
    st.set_page_config(
        page_title="Vivechan AI",
        page_icon="✨",
        # layout="wide",
    )
    
if __name__ == "__main__":
    main()

@st.cache_resource
def get_cached_encoder():
    return load_encoder()

@st.cache_resource
def get_cached_index():
    return load_index()

@st.cache_resource
def get_cached_text_dataset():
    return load_text_dataset()

# print("Going to call : get_cached_encoder")
Encoder=get_cached_encoder()

# print("Going to call : get_cached_index")
VectorIndex=get_cached_index()

# print("Going to call : get_cached_text_dataset")
Texts=get_cached_text_dataset()



st.title("Vivechan AI 🌟")
st.subheader("AI based on Shiv Maha Puran")


st.markdown(
    """
    <style>
        .reportview-container {
            width: 90%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

query = st.text_input("Ask any question related to the Shiv Mahapuran: ")

asked=False

if asked:
    st.write("generating answer .....")

if "state" not in st.session_state:
    if st.button('Ask'):
        st.session_state['state']=1
        
        asked=True
        encoded=Encoder.encode([query])
        D,I=VectorIndex.search(encoded,k)
        Context=generate_context(Texts,I[0])
        # print("Going to infer")
        # Answer=infer(query,Context)
        # print("Retrived Answer")
        Answer=Context
        asked=False
        
        write_answer(Answer,max_line_length)
        speak(Answer)

        del st.session_state['state']
        asked=False
        
        
else:
    if asked:
        st.write("Generating Answer ......")
    

    
display_footer()