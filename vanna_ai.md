# Code Documentation

## Importing Required Libraries
- The code imports necessary libraries such as `os`, `load_dotenv`, `openai`, and `re`.
- The `load_dotenv()` function is used to load environment variables from a .env file.
- The `openai.api_key` is set to the value stored in the environment variable `OPENAI_API_KEY`.

## Extract SQL Code from Markdown String
- The `__extract_sql_code()` function is defined to extract SQL code from a markdown string.
- It uses a regex pattern to match SQL code blocks within the markdown string.
- The function finds all matches using `re.findall()` and extracts the SQL code from the matches.
- If no SQL code is found, it returns the original markdown string.

## Send Input to OpenAI Chat Model
- The `send_to_openai_chat()` function sends input to the OpenAI chat model and extracts SQL code from the response.
- It creates a chat completion using `openai.ChatCompletion.create()` and extracts the SQL code from the response choices.

## Initialize Vertex AI
- The code initializes Vertex AI with project and location information.
- It imports necessary modules from `vertexai` and defines a function to send input to the Vertex AI model.

## Send Input to Vertex AI Model
- The `send_to_vertexai()` function sends input to the Vertex AI model and extracts SQL code from the response.
- It sets parameters for the model and uses `CodeGenerationModel.from_pretrained()` to load the model.
- The function predicts the output based on the input message log.

## Import 'replicate' Library
- The code imports the `replicate` library to use a specific model for generating SQL code.

## Send Input to Replicate Model
- The `send_to_replicate()` function sends input to the Replicate model and extracts SQL code from the response.
- It runs the specified model with the input prompt and retrieves the output as an iterator.
- The function iterates over the output and extracts the SQL code from the result.