#!/usr/bin/env python
# coding: utf-8

# # 랭체인 실습

# In[16]:


get_ipython().system('pip install langchain-community langchain-core')


# In[17]:


from langchain_community.llms import Ollama

llm = Ollama(model='llama3')
llm('Hi')


# In[28]:


get_ipython().run_cell_magic('writefile', 'app.py', "\nfrom langchain_community.llms import Ollama\nimport streamlit as st\n\n# 모델 초기화\nllm = Ollama(model='llama3')\n\n# 세션 상태 초기화\nif 'chat_history' not in st.session_state:\n    st.session_state.chat_history = []\n\n\ndef add_to_chat_history(user_input, bot_response):\n    st.session_state.chat_history.append('나: ' + user_input)\n    st.session_state.chat_history.append('Llama 3: ' + bot_response)\n\n\ndef display_chat_history():\n    for message in st.session_state.chat_history:\n        st.write(message)\n\n\n# 사용자 입력 필드\nuser_input = st.text_input('사용자 입력')\n\n# 사용자가 입력을 제출했을 때\nif user_input:\n    # LLM으로부터 응답받기\n    bot_response = llm(user_input)\n\n    # 대화 기록에 추가\n    add_to_chat_history(user_input, bot_response)\n\n    # 입력 필드 초기화\n    st.session_state.user_input = ''\n\n# 대화 기록 표시\ndisplay_chat_history()\n")


# In[ ]:


get_ipython().system('streamlit run app.py')


# In[ ]:




