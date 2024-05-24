
from langchain_community.llms import Ollama
import streamlit as st

# 모델 초기화
llm = Ollama(model='llama3')

# 세션 상태 초기화
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


def add_to_chat_history(user_input, bot_response):
    st.session_state.chat_history.append('나: ' + user_input)
    st.session_state.chat_history.append('Llama 3: ' + bot_response)


def display_chat_history():
    for message in st.session_state.chat_history:
        st.write(message)


# 사용자 입력 필드
user_input = st.text_input('사용자 입력')

# 사용자가 입력을 제출했을 때
if user_input:
    # LLM으로부터 응답받기
    bot_response = llm(user_input)

    # 대화 기록에 추가
    add_to_chat_history(user_input, bot_response)

    # 입력 필드 초기화
    st.session_state.user_input = ''

# 대화 기록 표시
display_chat_history()
