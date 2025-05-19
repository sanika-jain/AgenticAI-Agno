import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.storage.sqlite import SqliteStorage
from agno.playground import Playground, serve_playground_app

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    model=Gemini(),
    name="SessionStorageAgent",
    # Fix the session id to continue the same session across execution cycles
    session_id="fixed_id_for_demo",
    storage=SqliteStorage(table_name="memory", db_file="tmp/memory.db"),
    add_history_to_messages=True,
    num_history_runs=3,
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("session-storage:app")