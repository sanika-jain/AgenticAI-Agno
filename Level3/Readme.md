Tools in Agno:
Tools are functions that an Agent can call to interact with the external world.
Tools make agents - “agentic” by enabling them to interact with external systems like searching the web, running SQL, sending an email or calling APIs.

Two Approachs :
1. Writing your own Tool
2. Using ToolKits

A) Writing Your Own Tools
    The rule is simple:
        1. Any python function can be used as a tool by an Agent.
        2. Use the @tool decorator to modify what happens before and after this tool is called.
| *Parameter*            | *Type*           |*Description*                                                                 |
| ---------------------- | ---------------- | ---------------------------------------------------------------------------- |
| `name`                 | `str`            | Override for the function name                                               |
| `description`          | `str`            | Override for the function description                                        |
| `show_result`          | `bool`           | If `True`, shows the result after the function call                          |
| `stop_after_tool_call` | `bool`           | If `True`, the agent will stop after the function call                       |
| `tool_hooks`           | `list[Callable]` | List of hooks to run before and after the function is executed               |
| `cache_results`        | `bool`           | If `True`, enable caching of function results                                |
| `cache_dir`            | `str`            | Directory to store cache files                                               |
| `cache_ttl`            | `int`            | Time-to-live for cached results in seconds (default: 3600 seconds or 1 hour) |


B) ToolKits
    A Toolkit is a collection of functions that can be added to an Agent. The functions in a Toolkit are designed to work together, share internal state and provide a better development experience.

    1) Search: Arvix, BaiduSearch, DuckDuckGo, Exa, Google Search, HackerNews, Pubmed, SearxNG, Serpapi, Travily, Wikipedia
    2) Social: Discord, Email, Gmail, Slack, Telegram, Twilio, Webex, X, Zoom
    3) Web Scraping: AgentQL, Browserbase, Crawl4AI, Jina Reader, Newspaper, Newspaper4k, Website, Firecrawl, Spider
    4) Data: CSV, DuckDb, Pandas, Postgres, SQL, Zep

    ToolKit Parameters for DuckDuckGo:
    | *Function*          | *Description*                                             |
    | ------------------- | --------------------------------------------------------- |
    | `duckduckgo_search` | Use this function to search DuckDuckGo for a query.       |
    | `duckduckgo_news`   | Use this function to get the latest news from DuckDuckGo. |

    | *Parameter*         | *Type*   | *Default*   | *Description*                                                                |
    | ------------------- | -------- | ----------- | ---------------------------------------------------------------------------- |
    | `search`            | `bool`   | `True`      | Enables the use of the `duckduckgo_search` function to search DuckDuckGo.    |
    | `news`              | `bool`   | `True`      | Enables the use of the `duckduckgo_news` function to fetch latest news.      |
    | `fixed_max_results` | `int`    | `-`         | Sets a fixed number of maximum results to return. Must be specified if used. |
    | `headers`           | `Any`    | `-`         | Accepts any header values to be sent with HTTP requests.                     |
    | `proxy`             | `str`    | `-`         | Specifies a single proxy address as a string for HTTP requests.              |
    | `proxies`           | `Any`    | `-`         | Accepts a dictionary of proxies for HTTP requests.                           |
    | `timeout`           | `int`    | `10`        | Sets the timeout for HTTP requests, in seconds.                              |
