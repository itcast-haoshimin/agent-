from langchain_community.embeddings import DashScopeEmbeddings

#创建模型对象 不传model默认使用的是 text-embeddings-v1
model = DashScopeEmbeddings()

#不用invoke stream
#embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "你喜欢我","晚上吃啥"]))