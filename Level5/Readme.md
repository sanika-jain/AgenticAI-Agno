Multi-Source Summarization and Podcast Generation
--
Both l5-1.py and l5-2.py are advanced workflows built on the Agno framework, designed to process and summarize content from multiple sources—such as PDFs, YouTube videos, webpages, and plain text. They also feature podcast generation capabilities, transforming summarized content into audio.

However, l5-2.py introduces significant enhancements and architectural improvements over l5-1.py

Key Differences Between l5-1.py and l5-2.py:

| **Feature**                         | **l5-1.py (Monologue)** 🎙️    | **l5-2.py (Dialogue)** 🗣️🗣️             |
| ----------------------------------- | ------------------------------ | ----------------------------------------- |
| **Podcast Style**                   | Single speaker 🧍‍♂️           | Two speakers in dialogue format 👥        |
| **Podcast Agent/Team**              | One agent 👤                   | Team of two speaker agents 👥👤           |
| **Audio Segment Combination**       | Not combined ❌                 | Combined with natural pauses ⏸️✅          |
| **URL Extraction & Classification** | Regex-based function 🔗🧾      | Dedicated agent with JSON correction 🤖🧹 |
| **Modular Agent/Team Structure**    | Basic setup 🧩                 | Advanced modular team structure 🧠🧩      |
| **Routing**                         | Manual routing in workflow 🛠️ | Team-based dynamic routing 🔄🤝           |
| **Error Handling**                  | Basic try/except handling ⚠️   | Stepwise and granular error recovery 🪜✅  |
| **Intermediate Step Streaming**     | Limited or minimal 🔄🚫        | Extensive and transparent streaming 🌐    |
| **User Engagement**                 | Lower engagement 📉            | Higher engagement via natural dialogue 📈 |
| **Podcast Voices**                  | Single voice 🗣️               | Two distinct voices 🗣️🗣️                |


1. Podcast Generation Style

    l5-1.py:
    - Generates a monologue podcast: The podcast is a single-speaker narration of the combined summary.
    - Uses a single Podcast Generator agent with one ElevenLabs voice.
    - The summary is converted directly to audio (no dialogue or speaker turns).
    
    l5-2.py:
    - Generates a dialogue podcast: The podcast is a simulated conversation between two speakers (Speaker A and Speaker B).
    - Uses a Podcast Conversation Team with two distinct speaker agents, each with their own ElevenLabs voice.
    - The conversation is parsed into segments, each segment is synthesized with the appropriate speaker’s voice, and all segments are combined into a single            podcast audio file.

2. Agent and Team Structure

    l5-1.py:
    - Has a simpler agent structure: one agent each for scraping, summarizing PDFs, YouTube, web, text, and a single podcast agent.
    - Uses a single Team in "coordinate" mode to process all content types and podcast generation.
    
    l5-2.py:
    - Has a more modular and advanced agent/team structure:
    - URL Handler Agent: Extracts and classifies URLs from the prompt.
    - JSON Corrector Agent: Ensures the URL handler’s output is valid JSON.
    - Dedicated agents for scraping, PDF, YouTube, web, and text processing.
    - Podcast Conversation Team: Two agents simulate a dialogue.
    - Routing Team: Routes tasks to the appropriate agent or team based on content type and request.

3. Podcast Audio Processing

    l5-1.py:
    - Generates a single audio file for the podcast (monologue).
    - Uses write_audio_to_file utility to save the audio.
    
    l5-2.py:
    - Generates multiple audio segments (one per speaker turn).
    - Uses pydub to combine segments with pauses, creating a more natural conversational flow.
    - Saves the final podcast in a dedicated directory.

4. URL Extraction and Validation

    l5-1.py:
    - Uses regular expressions and a classify_url function to extract and classify URLs.
    - No explicit JSON validation step.
    
    l5-2.py:
    - Uses a dedicated URL Handler agent to extract and classify URLs, returning a structured JSON.
    - Adds a JSON Corrector agent to ensure the output is always valid JSON, improving robustness.

5. Workflow Routing and Error Handling

    l5-1.py:
    - Handles routing and error handling within the main workflow logic.
    - Warnings are collected and added to the response metadata.
    
    l5-2.py:
    - Uses a routing team to delegate tasks to the correct agent or team.
    - More granular error handling, retries, and warnings at each step (URL extraction, JSON correction, content processing, audio generation).

6. Intermediate Steps and Debugging

    l5-1.py:
    - Logs and warnings are present but less modular.
    
    l5-2.py:
    - Streams intermediate steps, logs each stage, and provides more detailed debugging information.

7. Customization and Extensibility

    l5-1.py:
    - Easier to follow for basic multi-source summarization and single-speaker podcast generation.
    
    l5-2.py:
    - More extensible and robust, supporting multi-speaker podcasts, modular agent design, and easier future expansion.

In summary:

l5-1.py is best for simple, single-speaker podcast generation from multi-source summaries.

l5-2.py is best for advanced, conversational podcasts with two speakers, robust URL handling, modular agent design, and improved error handling and evaluation.

l5-1:
--
l5-1.py is an advanced workflow script that demonstrates multi-source summarization and podcast generation using the Agno framework, Gemini language model, and various AI tools.

What does this file do?

1. Loads environment variables and API keys from a .env file for secure configuration.
2. Classifies and processes multiple content sources from a user prompt, including:
    - PDFs: Downloads, chunks, and summarizes PDF content using a vector database and Gemini embeddings.
    - YouTube videos: Fetches and summarizes video transcripts.
    - Webpages: Scrapes and summarizes webpage content.
    - Plain text: Summarizes any remaining text in the prompt.
3. Combines all summaries into a single, concise output.
4. Optionally generates a podcast (audio file) from the combined summary using ElevenLabs voice synthesis if requested by the user.
5. Handles errors and retries with exponential backoff for robust scraping and summarization.
6. Provides an interactive Agno Playground web UI for users to input prompts, view summaries, and download generated podcasts.

How to use
1. Install dependencies - *pip install agno chromadb google-genai python-dotenv opentelemetry-sdk*
2. Set up your environment
- Create a .env file in the project directory and add your API keys:
      GOOGLE_API_KEY=your_google_api_key
  
      ELEVEN_LABS_API_KEY=your_elevenlabs_api_key
  
      LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
  
      LANGFUSE_SECRET_KEY=your_langfuse_secret_key
3. Run the script- *python l5-1.py*
4. Open the web interface :Follow the instructions in the terminal to access the Agno Playground and interact with the multi-source summarization and podcast workflow.

Customization:
- Add or modify agent instructions to tailor summaries for your use case.
- Change the voice or model settings for podcast generation.
- Adjust retry and backoff logic for different reliability needs.

Dependencies
- agno
- chromadb
- google-genai
- python-dotenv
- opentelemetry-sdk
- elevenlabs (for podcast audio)

This script is ideal for building an AI-powered assistant that can summarize content from multiple sources and generate podcasts, all through a single conversational interface.


l5-2:
--
l5-2.py is a comprehensive workflow script that demonstrates multi-source content extraction, summarization, and podcast generation using the Agno framework, Gemini language model, and a team of specialized AI agents.

What does this file do?
1. Loads environment variables and API keys from a .env file for secure configuration.
2. Extracts and classifies content sources from user prompts, including:
    - PDFs: Downloads, chunks, and summarizes PDF content using a vector database and Gemini embeddings.
    - YouTube videos: Fetches and summarizes video transcripts.
    - Webpages: Scrapes and summarizes webpage content.
    - Plain text: Summarizes any remaining text in the prompt.
3. Combines all summaries into a single, concise output.
4. Optionally generates a podcast (audio file) from the combined summary using ElevenLabs voice synthesis, with a simulated conversation between two speakers.
5. Handles errors and retries with exponential backoff for robust scraping and summarization.
6. Provides an interactive Agno Playground web UI for users to input prompts, view summaries, and download generated podcasts.
7. Includes modular agents and teams for each content type, with stepwise error reporting and JSON validation for robust evaluation and debugging.

How to use
1. Install dependencies : *pip install agno chromadb google-genai python-dotenv pydub*
2. Set up your environment

   Create a .env file in the project directory and add your API keys:

       GOOGLE_API_KEY=your_google_api_key
      
       ELEVEN_LABS_API_KEY=your_elevenlabs_api_key  

3. Run the script
4. Open the web interface :Follow the instructions in the terminal to access the Agno Playground and interact with the multi-source summarization and podcast workflow.

Evaluation and Debugging
1. Structured JSON validation: Ensures all extracted and classified URLs and content are valid and well-structured before further processing.
2. Stepwise error reporting: Each stage (URL extraction, classification, content processing, audio generation) logs warnings and errors, which are returned to the user for transparency.
3. Intermediate step streaming: The workflow streams intermediate steps and agent responses, making it easy to debug and evaluate each part of the process.
4. Team-based routing: By routing tasks to specialized agents (for PDFs, YouTube, web, text, and podcast generation), the workflow enables granular evaluation of each content type and processing step.
5. Podcast generation evaluation: The podcast conversation is parsed, segmented, and synthesized into audio, with each segment and the final output checked for success and logged for review.

Dependencies
- agno
- chromadb
- google-genai
- python-dotenv
- pydub
- elevenlabs (for podcast audio)

This script is ideal for building, evaluating, and debugging AI-powered assistants that can summarize content from multiple sources and generate podcasts, all through a single conversational interface. The modular agent design and stepwise evaluation make it easy to monitor and improve each stage of the workflow.

OUTPUT:
--
WebPage:(https://notebooklm.google)
![image](https://github.com/user-attachments/assets/3bf20df3-6ee6-402f-ad09-f0f0a414b296)

YouTube Video: (https://youtu.be/69tPv5xZJjc)
![image](https://github.com/user-attachments/assets/01b38e08-7357-4ebb-bf82-9c7787cc9b36)

PDF : (https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf)
![image](https://github.com/user-attachments/assets/61004c82-f4e5-4468-aee0-256be1821b25)

Plain Text:
![image](https://github.com/user-attachments/assets/261c7629-8b04-4c48-9aab-af4754c20243)

