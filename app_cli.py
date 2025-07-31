import os
import asyncio
import sys
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatAzureOpenAI

async def main():
    # Allow specifying task as command line argument
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
    else:
        task = input("🤖 Enter the task you want to perform: ")
    
    if not task.strip():
        print("❌ No task specified.")
        return
    
    print(f"🚀 Executing task: {task}")
    
    agent = Agent(
        task=task,
        llm=ChatAzureOpenAI(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"), 
            api_key=os.getenv("AZURE_OPENAI_KEY")
        )
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())