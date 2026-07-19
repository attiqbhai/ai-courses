import importlib.metadata
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core import __version__ as core_version
from langgraph import graph as gr
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def main():

    #llm = ChatAnthropic(model="claude-sonnet-4-6", max_tokens=1024)

    #response = llm.invoke("Say, 'Setup complete' in one word")

    #print(response.content)
    print("I am alive and kicking !")



if __name__ == "__main__":
    main()