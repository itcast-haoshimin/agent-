from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

"""
PromptTemplate->  StringPromptTemplate->         BasePromptTemplate->RunnableSerializable->Runnable
FewShotPromptTemplate->StringPromptTemplate->    BasePromptTemplate->RunnableSerializable->Runnable
ChatPromptTemplate->  BaseChatPromptTemplate->   BasePromptTemplate->RunnableSerializable->Runnable

Runnable接口的子类都可以用|来连接
"""

template = PromptTemplate.from_template("我的邻居是：{lastname},最喜欢：{hobby}")
res = template.format(lastname="张", hobby="看电影")
print(res, type(res))   #str
res2 = template.invoke({"lastname": "张","hobby": "看电影"})
print(res2, type(res2))   #StringPromptValue