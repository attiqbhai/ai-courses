from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def demo_basic_chain():
    """Demo a basic chain using LCEL and Runnables"""

    # Component. 1 - Define a prompt tenplate using LCEL

    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Answer in one sentence. {question}"
    )

    model = ChatAnthropic(model="claude-sonnet-4-6", max_tokens=1024)
    
    parser = StrOutputParser()

    #Compose with Pipe Operator

    chain = prompt | model | parser

    # Execute the chain with the input

    result = chain.invoke({"question": "What is langchain?"})

    print("Printing result here.")
    
    print(f"Response result is :::::: {result}")

    return chain


if __name__ == "__main__":
    demo_basic_chain()
