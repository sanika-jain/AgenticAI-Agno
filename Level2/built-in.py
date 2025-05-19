import os
from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.playground import Playground, serve_playground_app
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    name="Built-In Memory Agent",
    model=Gemini(),
    # Set add_history_to_messages=true to add the previous chat history to the messages sent to the Model.
    add_history_to_messages=True,
    # Number of historical responses to add to the messages.
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("built-in:app")