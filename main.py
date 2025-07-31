import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatAzureOpenAI

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatAzureOpenAI(
            model= os.getenv("AZURE_OPENAI_DEPLOYMENT"), 
            api_key=os.getenv("AZURE_OPENAI_KEY")
        )
    )
    await agent.run()

asyncio.run(main())