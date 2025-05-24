Memory in Agno
--
In Agno, Memory covers chat history, user preferences and any supplemental information about the task at hand.

Approach:

1. Built-In Memory: Every Agent has built-in memory that keeps track of the messages in the session, i.e., the chat history.

    *(Note: The default memory is not persisted across execution cycles. So after the script finishes running, or the request is over, the built-in default memory is lost.)*

2. Session Storage: Storage helps us save Agent sessions and state to a database or file. Adding storage to an Agent is as simple as providing a storage driver, and Agno handles the rest. You can use SQLite, Postgres, Mongo, or any other database you want.

3. User Memory: Agents can also create user memories based on the conversation history. To enable user memories, give your Agent a Memory object and set enable_agentic_memory=True.

**Built-In Memory / Default Memory:**

  i) enable_agentic_memory=True gives the Agent a tool to manage memories of the user, this tool passes the task to the MemoryManager class. You may also set enable_user_memories=True which always runs the MemoryManager after each user message.
  
  ii) add_history_to_messages=True adds the chat history to the messages sent to the Model, the num_history_runs determines how many runs to add.
  
  iii) read_chat_history=True adds a tool to the Agent that allows it to read chat history, as it may be larger than what’s included in the num_history_runs.

  **Session Storage:**

Storage has typically been an under-discussed part of Agent Engineering — but we see it as the unsung hero of production agentic applications.

In production, you need storage to:

i. Continue sessions: retrieve sessions history and pick up where you left off.

ii. Get list of sessions: To continue a previous session, you need to maintain a list of sessions available for that agent.

iii. Save state between runs: save the Agent’s state to a database or file so you can inspect it later.

iv. Storage saves our Agent’s session data for inspection and evaluations.

v. Storage helps us extract few-shot examples, which can be used to improve the Agent.

vi. Storage enables us to build internal monitoring tools and dashboards.

**User-Memory:**

User memories are stored in the Memory object and persisted in the SqliteMemoryDb to be used across multiple users and multiple sessions.

Outputs:
--
1. Built-in.py:
   
   ![image](https://github.com/user-attachments/assets/4d0e8de5-207f-46bd-8f18-1660df049933)

2. Built-in-cli.py:
   
   ![image](https://github.com/user-attachments/assets/79b74ba1-279c-4dc1-ae75-9e0002b50cf1)
   ![image](https://github.com/user-attachments/assets/7e5c61a5-0f11-407f-8b3b-8ab463159594)

3. Session-storage .py
4. session-storage-cli.py:

   
   
