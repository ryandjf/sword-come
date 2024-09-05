from http import HTTPStatus
import dashscope
import os
from dotenv import load_dotenv
from langchain_community.llms import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_qianwen import ChatQwen_v1
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import (
    HumanMessage,
)

_ = load_dotenv()

dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')
DASHSCOPE_API_KEY = os.environ["DASHSCOPE_API_KEY"]

def call_with_chat():
    chat = ChatQwen_v1(
        model_name="qwen-turbo",
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )

    chat([HumanMessage(content="什么是快乐星球")])

def call_with_messages():
    
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '请介绍一下通义千问'}]

    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',  # 将返回结果格式设置为 message
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))

def call_with_llm():
    
    llm=Tongyi(temperature=1)
    template='''
        你的名字是小黑子,当人问问题的时候,你都会在开头加上'唱,跳,rap,篮球!',然后再回答{question}
    '''
    prompt=PromptTemplate(
        template=template,
        input_variables=["question"]#这个question就是用户输入的内容,这行代码不可缺少
    )
    chain = prompt | llm
    question='你是谁'

    response = chain.invoke(question)#运行
    
    print(response)

if __name__ == '__main__':
    call_with_llm()
