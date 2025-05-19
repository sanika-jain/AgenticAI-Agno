import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.storage.sqlite import SqliteStorage
from agno.models.google.gemini import Gemini
from agno.playground import Playground, serve_playground_app

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

memory_db = SqliteMemoryDb(table_name="user-memory", db_file="tmp/user-memory.db")
memory = Memory(db=memory_db,model=Gemini())

storage=SqliteStorage(table_name="memory", db_file="tmp/memory.db")

user_id = "default_user"

agent = Agent(
    model=Gemini(),
    name="UserMemoryAgent",
    memory=memory,
    storage=storage,
    user_id=user_id,
    enable_agentic_memory=True,
    enable_user_memories=True,
    add_history_to_messages=True,
    stream=True,
    num_history_runs=3,
    markdown=True,
    enable_session_summaries=True,
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("user-memory:app")