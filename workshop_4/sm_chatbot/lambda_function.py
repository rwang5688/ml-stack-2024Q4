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
    # bedrock converse invocation
    #inference_config = {'temperature': 1.0, 'topP': 1.0, 'maxTokens': 1024}
    #response = bedrock.converse(
    #    modelId=model_id,
    #    messages=messages,
    #    inferenceConfig=inference_config
    #)

    # sagemaker endpoint invocation
    content_type = "application/json"
    # use the last entry in the chat as inputs
    inputs = messages[-1]['content'][-1]['text']
    print(inputs)
    data = {
       "inputs": inputs
    }
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
    output = response_body[-1]['generated_text']
    print(output)
    
    # bedrock converse response
    #content = response['output']['message']['content']
    #output = ''
    #for item in content:
    #    output = output + item['text'] + '\n'
    
    return output
