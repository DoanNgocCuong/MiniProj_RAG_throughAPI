import streamlit as st
import requests
import json

def query_api(text, top_k=5, return_doc=True):
    url = "http://103.253.20.13:9225/flashrag/predict"
    headers = {"Content-Type": "application/json"}
    data = {
        "text": text,
        "top_k": top_k,
        "return_doc": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def main():
    st.title("Chatbot UI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is your question?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = query_api(prompt)
            answer = response["result"]["pred_answer_list"][0]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()
