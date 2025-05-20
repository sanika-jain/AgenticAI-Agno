import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.playground import Playground, serve_playground_app

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

agent=Agent(
    name="WebSearchAgent",
    model=Gemini(),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    stream=True
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("websearch:app")