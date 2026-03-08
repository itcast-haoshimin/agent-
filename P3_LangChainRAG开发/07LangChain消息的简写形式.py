from langchain_community.chat_models.tongyi import ChatTongyi
#from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 得到模型对象, qwen3-max就是聊天模型
model = ChatTongyi(model="qwen3-max")
"""
messages = [
    SystemMessage(content="你是一个边塞诗人。"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="按照你上一个回复的格式，在写一首唐诗。")
]
二者区别：静态的一步到位 直接就封装得到了Message类的类对象
下面是动态的 需要在运行时 由LangChain内部机制转换为Message类对象（提供什么就转换什么Message）
好处在于：避免导包，写起来来简单 支持内部填充{变量}占位
"""


# 准备消息列表
messages = [
    # (角色，内容)  角色：system/human/ai
    ("system", "你是一个边塞诗人。"),
    ("human", "写一首唐诗。"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照你上一个回复的格式，在写一首唐诗。")
]

# 调用stream流式执行
res = model.stream(input=messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in res:
    print(chunk.content, end="", flush=True)
