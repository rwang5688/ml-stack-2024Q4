import json
import boto3

endpoint_name = 'distilgpt2-pt-ep-2024-07-11-06-38-39'
sagemaker = boto3.client(service_name='sagemaker-runtime')

def lambda_handler(event, context):
    if (event['httpMethod'] == 'GET'):
        output = load_html()
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': output
        }
    elif (event['httpMethod'] == "POST"):
        body = json.loads(event['body'])
        messages = body['messages']
        print(messages)
        output = chat(messages)
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': output
        }
    else:
         return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': "OK"
        }

def load_html():
    html = ''
    with open('index.html', 'r') as file:
        html = file.read()
    return html

def chat(messages):
    # assemble sagemaker endpoint invocation parameters
    content_type = "application/json"
    # use the latest entry in the chat history as prompt
    inputs = messages[-1]['content'][-1]['text']
    print(inputs)
    data = {
       "inputs": inputs
    }

    # invoke sagemaker endpoint
    response = sagemaker.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType=content_type,
        Body=json.dumps(data)
    )
    print(response)

    # sagemaker endpoint invocation response
    response_body_str = response["Body"].read().decode("utf-8")
    print(response_body_str)
    response_body = json.loads(response_body_str)

    # assemble output
    output = ''
    for item in response_body:
        output = output + item['generated_text'] + '\n'
    print(output)
    
    return output
