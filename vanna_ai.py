// Import the required libraries
import os
from dotenv import load_dotenv
load_dotenv()
import openai
import re

// Set the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

// Define a function to extract SQL code from a markdown string
def __extract_sql_code(markdown_string: str) -> str:
    // Define the regex pattern to match SQL code blocks
    pattern = r"```[\w\s]*sql\n([\s\S]*?)```|```([\s\S]*?)```"
    
    // Find all matches in the markdown string
    matches = re.findall(pattern, markdown_string, re.IGNORECASE)

    // Extract the SQL code from the matches
    sql_code = []
    for match in matches:
        sql = match[0] if match[0] else match[1]
        sql_code.append(sql.strip())

    // Return the extracted SQL code
    if len(sql_code) == 0:
        if '\n\n\n' in markdown_string:
            return markdown_string.split('\n\n\n')[-1]
            
        return markdown_string

    return sql_code[0]

// Define a function to send the input to the OpenAI chat model and extract the SQL code from the response
def send_to_openai_chat(model, message_log) -> str:    
    response = openai.ChatCompletion.create(model=model, messages=message_log, max_tokens=500, stop=None, temperature=0.7)
    
    for choice in response.choices:
        if "text" in choice:
            return __extract_sql_code(choice.text)
            
    return __extract_sql_code(response.choices[0].message.content)

// Initialize Vertex AI with project and location information
import vertexai
from vertexai.language_models import CodeGenerationModel

vertexai.init(project=os.environ['GCP_PROJECT'], location=os.environ['GCP_REGION'])

// Define a function to send the input to the Vertex AI model and extract the SQL code from the response
def send_to_vertexai(message_log) -> str:
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 2048
    }
    model = CodeGenerationModel.from_pretrained("code-bison@001")
    response = model.predict(
        prefix = message_log,
        **parameters
    )

    sql = response.text

    return __extract_sql_code(sql)

// Import the 'replicate' library
import replicate

// Define a function to send the input to the Replicate model and extract the SQL code from the response
def send_to_replicate(message_log) -> str:
    output = replicate.run(
        "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        input={"prompt": message_log}
    )
    // The replicate/llama-2-70b-chat model can stream output as it's running.
    // The predict method returns an iterator, and you can iterate over that output.

    result = ""
    for item in output:
        result += item

    sql = result

    return __extract_sql_code(sql)