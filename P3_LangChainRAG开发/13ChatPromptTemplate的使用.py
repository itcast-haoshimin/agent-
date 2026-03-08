from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个助手"),
        MessagesPlaceholder("history"),
        ("human", "你会什么")
    ]
)

history_data = [
    ("human", "今天天气不错"),
    ("ai", "今天真好"),
    ("human", "你叫什么名字"),
    ("ai", "我叫小王")
]

#返回类型 StringPromptValue 需要toString()
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()

model = ChatTongyi(model="qwe3n-max")

res = model.invoke(prompt_text)
print(res.content,type( res))     #message.ai.AIMessage