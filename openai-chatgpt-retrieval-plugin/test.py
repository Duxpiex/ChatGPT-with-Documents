from llama_index.readers import ChatGPTRetrievalPluginReader
import os

bearer_token = os.getenv("BEARER_TOKEN")

reader = ChatGPTRetrievalPluginReader(
    endpoint_url="http://127.0.0.1:8000",
    bearer_token=bearer_token
)

documents = reader.load_data("Explain what your learning goals are")
print(len(documents))

from llama_index import ListIndex

index = ListIndex(documents)

query_engine = index.as_query_engine(response_mode="compact")
response = query_engine.query(
    "Explain what your learning goals are",
)

print(response)