from mlflow.gateway import query, set_gateway_uri

set_gateway_uri(gateway_uri="http://127.0.0.1:5000")


route_name = "my_completions_route"
data = dict(
    prompt="Name three potions or spells in harry potter that sound like an insult. Only show the names.",
    candidate_count=2,
    temperature=0.2,
    max_tokens=1000,
)

response = query(route_name, data)
print(response)
