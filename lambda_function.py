import requests
def lambda_handler(event, context):   
    response = requests.get("https://www.example.com/")
    print(response.text)
    return response.text
