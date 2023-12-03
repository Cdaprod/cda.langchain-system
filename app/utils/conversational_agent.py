from langchain.llms import OpenAI
from langchain.conversations import ConversationChain, ConversationBufferWindowMemory
from .semantic_parser import semantic_content_parser  # Import your parser function
from .dependencies import get_minio_client, get_weaviate_client
from .rag_fusion import execute_rag_fusion_chain
import json

class ConversationalAgent:
    def __init__(self):
        self.llm = OpenAI()  # Adjust based on your setup
        self.memory = ConversationBufferWindowMemory(window_size=1)
        self.chain = ConversationChain(llm=self.llm, memory=self.memory)


    def process_with_semantic_parser(self, message):
        # Here, you can add conditions or preprocess the message if needed
        return semantic_content_parser(message)


    def process_message(self, message, bucket_name):
        self.chain.add_message("user", message)

        # Decide when to use the semantic parser
        if "use semantic parser" in message:
            parsed_content = self.process_with_semantic_parser(message)
            response = f"Processed Content: {parsed_content}"
        else:
            response = self.chain.generate_response()
            if "trigger RAG Fusion" in message:
                response += execute_rag_fusion_chain(message, bucket_name, get_weaviate_client())
        
        self.save_chat_history(bucket_name)
        return response

    def save_chat_history(self, bucket_name):
        minio_client = get_minio_client()
        # Serialize the current chat history
        chat_history = json.dumps(self.chain.messages)
        try:
            minio_client.put_object(bucket_name, 'chat_history.json', data=chat_history, length=len(chat_history))
        except Exception as e:
            print(f"Error saving chat history to MinIO: {e}")

    def load_chat_history(self, bucket_name):
        minio_client = get_minio_client()
        try:
            data = minio_client.get_object(bucket_name, 'chat_history.json').data
            loaded_history = json.loads(data)
            for message in loaded_history:
                self.chain.add_message(message['speaker'], message['text'])
        except Exception as e:
            print(f"Error loading chat history from MinIO: {e}")