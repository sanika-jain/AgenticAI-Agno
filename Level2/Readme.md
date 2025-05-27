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

3. Session-storage.py:

   ![image](https://github.com/user-attachments/assets/a2ea5401-b856-425f-b763-bf1b9dd7abcb)
   ![image](https://github.com/user-attachments/assets/26b5e17b-0f25-483e-9044-11b9016652bf)

4. session-storage-cli.py:

   https://github.com/user-attachments/assets/0e7c44b3-3b6f-43b7-860c-f97a49143afa

5. user-memory.py:

   ![image](https://github.com/user-attachments/assets/e02bad5a-22ff-41a4-b979-f56abe5a9129)
   ![image](https://github.com/user-attachments/assets/42252f89-8939-40ee-a6b0-b491c5381de0)

6. user-memory-cli.py:

   ![image](https://github.com/user-attachments/assets/c45a812f-72cc-46e5-922d-06934ce16135)
   ![image](https://github.com/user-attachments/assets/9fc6c99f-a395-48c0-b8e5-f081db019bba)
   ![image](https://github.com/user-attachments/assets/5738eac2-3891-45ac-a885-f6b954c6c215)
   ![image](https://github.com/user-attachments/assets/9907250f-51d2-4d71-8596-9e4979ec3347)
   ![image](https://github.com/user-attachments/assets/700be53e-c1c9-4087-83b1-e1a1e25a53f1)
   ![image](https://github.com/user-attachments/assets/8edc5b33-488b-41f4-a2fa-b54739fc9b76)






   
   
