
# Langchain

[`LangChain : official document`](https://python.langchain.com/v0.2/docs/introduction/)  

---

### description
- 언어모델 기반 애플리케이션을 개발하기 위한 프레임워크
- API 호출 / 외부데이터 인식 / 외부 애플리케이션과 상호작용
- OpenSource

![image](https://github.com/Choe-minsung/TIL/assets/145301343/e8dcda71-2033-4e0d-b496-05d67d45e942)

### composition
1. LangChain Library
2. LangSmith
3. LangServe
4. LangChain Templete

![image](https://github.com/Choe-minsung/TIL/assets/145301343/76b16af1-fdbb-498a-b09e-1ff53f366b13)

---
# 실습

### Ollama 설치 & Llama3 run
[`Ollama`](https://ollama.ai/)
- Ollama : 로컬에서 다양한 언어 모델을 실행하고 웹 앱에서 활용할 수 있도록 지원하는 오픈 소스 도구

![image](https://github.com/Choe-minsung/TIL/assets/145301343/b8a674e9-1424-481b-9e61-09985364ed06)
![image](https://github.com/Choe-minsung/TIL/assets/145301343/eba73397-2d14-4de1-813e-45151ba97116)

### LangChain과 연결
[`langchain_community`](https://api.python.langchain.com/en/latest/llms/langchain_community.llms.ollama.Ollama.html)

- Web code
```
!pip install langchain-community langchain-core
%%writefile app.py

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

!streamlit run app.py
```

- test
![image](https://github.com/Choe-minsung/TIL/assets/145301343/1bd667b3-3689-4869-93dc-25da99d8ffe0)
