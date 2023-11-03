from mlflow.gateway import query, set_gateway_uri
import time
import json

set_gateway_uri(gateway_uri="http://127.0.0.1:5000")


route_name = "my_completions_route_gpt4"

prompt_template = """
You would be given a user input which is a small description about the user.
Based on the user input, your task is to analyze the input and
- identify the key skill of the user and geography if mentioned
- generate %s expertise tags based on the input.
  Each tag should be added to a list. Use title case wherever applicable.
- generate a contextual formal biography for the user whose name is <name> in
  first person focussing on broad domains.
You are free to take some creative liberties. Do not use too many of the generated
tags in the bio. Limit it to maximum 50 words.
- generate at least 5 tags.
- the output should be in following JSON structure
  {{"expertise_tags": [".."], "bio": ".."}} 
"""

user_input = input("Enter your 2 line bio: ")
prompt = prompt_template + user_input

data = dict(
    prompt=prompt,
    candidate_count=1,
    temperature=0.7,
    max_tokens=1000,
)

start_time = time.time()
response = query(route_name, data)
end_time = time.time()

response_time = end_time - start_time

formatted_response = json.dumps(response, indent=3)

print(f"response:\n\n {response}")

print(f"\nResponse time: {response_time} seconds")