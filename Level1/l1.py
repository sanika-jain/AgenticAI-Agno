import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.playground import Playground, serve_playground_app

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

gemini_agent = Agent(
    name="HelloWorld",
    model=Gemini(),
    markdown=True
)

app = Playground(agents=[gemini_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("l1:app", reload=True)
