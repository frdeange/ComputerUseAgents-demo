from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import asyncio
import threading
import webbrowser
import time
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm import ChatAzureOpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Computer Use Agents v2.0", description="AI-powered web automation interface")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Global variables for agent state
agent_running = False
current_task = None

class TaskRequest(BaseModel):
    task: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit_task")
async def submit_task(task_request: TaskRequest):
    global agent_running, current_task
    
    if agent_running:
        raise HTTPException(status_code=400, detail="A task is already running")
    
    task = task_request.task.strip()
    
    if not task:
        raise HTTPException(status_code=400, detail="Please enter a valid task")
    
    current_task = task
    
    # Run the agent in a separate thread
    thread = threading.Thread(target=run_agent_async, args=(task,))
    thread.daemon = True
    thread.start()
    
    # Open browser console after a small delay
    threading.Timer(2.0, open_browser_console).start()
    
    return JSONResponse({
        'status': 'success', 
        'message': f'Task started: {task}',
        'console_url': 'http://localhost:6080'
    })

@app.get("/status")
async def get_status():
    return JSONResponse({
        'running': agent_running,
        'current_task': current_task
    })

def run_agent_async(task):
    """Run the agent asynchronously"""
    global agent_running
    agent_running = True
    
    try:
        asyncio.run(run_agent(task))
    except Exception as e:
        print(f"Error running agent: {e}")
    finally:
        agent_running = False

async def run_agent(task):
    """Main agent function"""
    try:
        agent = Agent(
            task=task,
            llm=ChatAzureOpenAI(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT"), 
                api_key=os.getenv("AZURE_OPENAI_KEY")
            )
        )
        await agent.run()
    except Exception as e:
        print(f"Agent error: {e}")

def open_browser_console():
    """Open the browser console on port 6080"""
    try:
        # Try to open in host's browser
        os.system('$BROWSER http://localhost:6080 &')
    except Exception as e:
        print(f"Could not open browser automatically: {e}")

if __name__ == '__main__':
    import uvicorn
    print("🚀 Starting Computer Use Agents v2.0")
    print("📱 Web interface available at: http://localhost:5000")
    print("🖥️  Browser console at: http://localhost:6080")
    
    uvicorn.run("app_browser:app", host='0.0.0.0', port=5000, reload=True)
