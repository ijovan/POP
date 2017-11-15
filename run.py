from src.main.python.http_client import HttpClient

content = HttpClient.get("questions")

print(content)
