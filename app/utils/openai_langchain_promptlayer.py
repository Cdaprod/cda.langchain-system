from langchain.callbacks import PromptLayerCallbackHandler

# OpenAI Completion Model
from langchain.llms import OpenAI

llm = OpenAI(
    model_name="text-davinci-003", 
    callbacks=[
        PromptLayerCallbackHandler(
            pl_tags=["getting_started_example"] # 🍰 PromptLayer tags
        ),
    ],
)

"""
To retrieve the pl_request_id using LangChain, we
specify a callback function (pl_id_callback) 
that receives the ID on successful logging of the request.
"""

# Callback function that saves our request_id
pl_request_id = None
def save_pl_id(pl_id):
    global pl_request_id
    print("PromptLayer Request ID:", pl_id)
    pl_request_id = pl_id

llm = OpenAI(
    model_name="text-davinci-003",
    callbacks=[PromptLayerCallbackHandler(
            pl_id_callback=save_pl_id, # Here is where we set our callback func
            pl_tags=["getting_started_example"])],
)

# Let's see what the answer is...
answer = llm("What is the capital of New York? \\n\\nThe capital of New York is")
print(answer)

# Check if the answer is correct & log score to 🍰 PromptLayer
correct_answer = "albany" in answer.lower()
promptlayer.track.score(
    request_id=pl_request_id,
    score=100 if correct_answer else 0,
)
