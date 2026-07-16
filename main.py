# =========================================================
# PROJECT 6 — Few-Shot Intent Classifier
# Concepts: FewShotChatMessagePromptTemplate
# =========================================================

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3.2:latest", temperature=0)  # 0 -> classification needs to be consistent, not creative

# 1) Example inputs/outputs that SHOW the model the exact format we want back.
#    Instead of just describing "classify into complaint/question/praise", we demonstrate it.
examples = [
    {"message": "My order arrived broken and no one is responding to my emails.", "label": "complaint"},
    {"message": "Does this product come in a larger size?", "label": "question"},
    {"message": "This is honestly the best purchase I've made this year!", "label": "praise"},
    {"message": "Why hasn't my refund been processed yet?", "label": "complaint"},
    {"message": "What are your store hours on weekends?", "label": "question"},
]

# 2) Template for ONE example — how each example pair gets formatted into messages
example_prompt = ChatPromptTemplate.from_messages([
    ("user", "{message}"),
    ("assistant", "{label}")
])

# 3) FewShotChatMessagePromptTemplate takes the examples + example_prompt and
#    expands them into a full sequence of messages (all examples, back to back)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

# 4) Final prompt: system instructions -> all the few-shot examples -> the real user message
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "Classify each customer message as one of: complaint, question, praise. Reply with only the label."),
    few_shot_prompt,          # inserts all example messages here
    ("user", "{message}")     # the actual message we want classified
])

chain = final_prompt | llm | StrOutputParser()

def classify_message():
    print("Few-Shot Intent Classifier (type 'exit' to quit)\n")

    while True:
        message = input("Customer message: ")

        if message.lower() == "exit":
            print("Goodbye!")
            break

        label = chain.invoke({"message": message})
        print(f"Predicted label: {label}\n")

if __name__ == "__main__":
    classify_message()

