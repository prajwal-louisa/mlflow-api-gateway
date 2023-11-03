from mlflow.gateway import query, set_gateway_uri

set_gateway_uri(gateway_uri="http://127.0.0.1:5000")


route_name = "my_chat_route_gpt_3.5_turbo"
data = dict(
     messages=[
        {"role": "system", "content": "You are the sorting hat from harry potter."},
        {"role": "user", "content": "I am brave, hard-working, wise, and backstabbing."},
        {"role": "user", "content": "Which harry potter house am I most likely to belong to?"}
    ],
    candidate_count=3,
    temperature=.5,
)

response = query(route_name, data)

print(response)