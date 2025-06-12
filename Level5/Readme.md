Multi-Source Summarization and Podcast Generation
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



