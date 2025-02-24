import streamlit as st

st.set_page_config(page_title='Chat with multipl PDFs', page_icon=":BOOKS:")
st.header("Chat with multipl PDFs :BOOKS:")
st.text_input("Ask a question about document")
with st.sidebar:
  st.subheader("Your documents")
  st.file_uploader("Upload your Documents here and click 'Process'")
  st.button("Process")
