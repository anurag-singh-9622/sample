# Code Documentation

## Importing Libraries
- `os`: provides a way to interact with the operating system.
- `load_dotenv`: loads environment variables from a .env file.
- `openai`: library for interacting with the OpenAI API.
- `re`: provides support for regular expressions.

## Extract SQL Code Function
- `__extract_sql_code(markdown_string: str) -> str`: extracts SQL code blocks from a Markdown string.
    - Uses a regex pattern to match SQL code blocks.
    - Finds all matches in the markdown string.
    - Extracts the SQL code from the matches.
    - Returns the extracted SQL code or the last part of the string if no code blocks are found.

## Send to OpenAI Chat Function
- `send_to_openai_chat(model, message_log) -> str`: sends a message log to the OpenAI Chat API.
    - Creates a chat completion using the specified model and message log.
    - Extracts SQL code from the response choices or the default choice.

## Initializing VertexAI
- Initializes VertexAI with project and location information from environment variables.

## Send to VertexAI Function
- `send_to_vertexai(message_log) -> str`: sends a message log to a Code Generation Model on VertexAI.
    - Sets parameters for model prediction.
    - Predicts SQL code using the specified model and message log.

## Send to Replicate Function
- `send_to_replicate(message_log) -> str`: sends a message log to a model on Replicate.
    - Runs the specified model with the input prompt.
    - Streams output from the model and extracts SQL code.

These functions provide ways to interact with different AI models for generating SQL code based on input messages.