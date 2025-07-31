# Computer User Agent (CUA)

## Overview
Computer User Agent (CUA) is an intelligent assistant designed to autonomously perform complex web-based tasks on behalf of the user. Leveraging advanced language models and browser automation, CUA can interpret natural language instructions, interact with web pages, and summarize or extract relevant information. This project demonstrates how an AI agent can be used to automate real-world information gathering and processing tasks.

## What does the Assistant do?
The assistant in this project is capable of:
- Understanding and executing user-defined tasks (e.g., "Find the 4 most important news on marca.com and summarize them").
- Using Azure OpenAI for natural language understanding and reasoning.
- Automating browser actions to navigate, search, and extract content from websites.
- Returning concise, human-readable summaries of the gathered information.

## Project Structure
- `simplyagent.py`: Main entry point. Loads environment variables, initializes the language model, and runs the agent with a sample task.
- `requirements.txt`: Lists all Python dependencies required to run the project.
- `.fake.env`: Example environment file with placeholder values (see below).

## Getting Started

### 1. Development Environment
This project is designed to be used with a [devcontainer](https://containers.dev/), providing a pre-configured development environment with Python, and Azure CLI tools installed. You can open this project directly in GitHub Codespaces or any compatible devcontainer setup for a seamless experience.

### 2. Environment Variables
Sensitive configuration (such as Azure OpenAI credentials) is managed via environment variables. For security, the repository includes a `.fake.env` file with example values. **You must create your own `.env` file before running the project:**

1. Copy `.fake.env` to `.env`:
   ```sh
   cp .fake.env .env
   ```
2. Edit `.env` and fill in your actual Azure OpenAI and deployment details:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_DEPLOYMENT`
   - `AZURE_OPENAI_API_VERSION`
   - `AZURE_OPENAI_KEY`

### 3. Install Dependencies
With your devcontainer or local environment ready, install the required Python packages (it would be installed by default with the build of the devcontainer, only required if you copy the repo to your local machine and do not use a devcontainer):

```sh
pip install -r requirements.txt
```

### 4. Run the Assistant
To launch the agent with the default task, run:

```sh
python simplyagent.py
```

You can modify the `task` variable in `simplyagent.py` to change the agent's behavior.

## Usage Instructions

### Running the Project with a Visual Environment
This project requires launching a browser (embedded with Playwright and Chromium) to perform its tasks. Since the browser needs a visual environment, you must run the application using a virtual framebuffer, at least if you execute the project from the devcontainer. To start the agent, use the following command:

```sh
xvfb-run python simplyagent.py
```

This will ensure that the browser can run headlessly in environments without a physical display (such as devcontainers or remote servers).

### Devcontainer Setup
All necessary dependencies, including Playwright, Chromium, and supporting tools, are pre-installed in the devcontainer. You do not need to install anything manually. Simply:

1. Open the project in your devcontainer (e.g., GitHub Codespaces or VS Code with devcontainer support).
2. Copy and configure your `.env` file as described above.
3. Customize the `task` variable in `simplyagent.py` to define what you want the agent to do.
4. Run the application with the command above.

You are ready to use the Computer User Agent for your automated web tasks!

## What is Computer User Agent (CUA)?
Computer User Agent (CUA) is a concept and implementation of an autonomous software agent that can:
- Receive high-level instructions in natural language.
- Use large language models (LLMs) to interpret and plan actions.
- Interact with web browsers and APIs to accomplish tasks.
- Summarize and present results in a user-friendly format.

This project serves as a practical example of CUA, focusing on web information retrieval and summarization using Azure OpenAI and browser automation.

## License
This project is provided for educational and demonstration purposes. Please review the license terms before using it in production.
