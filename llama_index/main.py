import os
from typing import Any, Coroutine, List
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.base import BaseEmbedding, Embedding
from InstructorEmbedding import INSTRUCTOR
import re
import time
from utils import simplify_txt
# export env variable
os.environ['LLAMA_INDEX_CACHE_DIR'] = "/Volumes/taogoddd/Developer/cache/string"
os.environ['OPENAI_API_KEY'] = "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"

class InstructorEmbeddings():
    _model: Any
    _instruction: str

    def __init__(
        self, 
        instructor_model_name: str = "hkunlp/instructor-large",
        instruction: str = "Represent the financial report for retrieving CEO Pay Ratio:",
        **kwargs: Any,
    ) -> None:
        self._model = INSTRUCTOR(instructor_model_name)
        self._instruction = instruction

    def _get_query_embedding(self, query: str) -> List[float]:
      embeddings = self._model.encode([[self._instruction, query]])
      return embeddings[0]

    def _get_text_embedding(self, text: str) -> List[float]:
      embeddings = self._model.encode([[self._instruction, text]])
      return embeddings[0] 

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
      embeddings = self._model.encode([[self._instruction, text] for text in texts])
      return embeddings
    def class_name(self) -> str:
        return "InstructorEmbeddings"
    def _aget_query_embedding(self, query: str) -> Coroutine[Any, Any, Embedding]:
           return None
year = 2021
dir_list = [f"./data_{year}/sec-edgar-filings/{code}/DEF 14A/{os.listdir(f'./data_{year}/sec-edgar-filings/{code}/DEF 14A')[0]}" for code in os.listdir(f"./data_{year}/sec-edgar-filings")]
dir_list = dir_list[:1]
print(dir_list)
file_list = [f"{dir}/{os.listdir(dir)[0]}" for dir in dir_list]
for file in file_list:
    simplify_txt(file)
simplified_file_list = [f"{dir}/{os.listdir(dir)[0].replace('.txt', '_simplified.txt')}" for dir in dir_list]

instructor = InstructorEmbeddings(instructor_model_name="hkunlp/instructor-large", instruction="Represent the financial report for retrieving CEO Pay Ratio:")
service_context = ServiceContext.from_defaults(embed_model=instructor)

reader = SimpleDirectoryReader(input_files=simplified_file_list)
print("Loading documents")
docs = reader.load_data()
print(f"Loaded {len(docs)} documents")

print("Building index")
start_index_time = time.time()
index = VectorStoreIndex.from_documents(documents=docs)
end_index_time = time.time()
print(f"Index built in {end_index_time - start_index_time} seconds")
print("Index built")

print("Querying index")
query_engine = index.as_query_engine()
response = query_engine.query("ceo pay ratio")
print(response)