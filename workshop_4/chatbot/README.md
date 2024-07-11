### Bedrock Converse API: Amazon Bedrock Development Workshop - Conversational Chatbot

Lab content: https://catalog.us-east-1.prod.workshops.aws/workshops/0b6e72fe-77ee-4777-98cc-237eec795fdb/en-US/fm/06-chatbot

Deployment and Test instructions:

1. Confirm there is a deployment S3 bucket with name: `sagemaker-${AWS::Region}-${AWS::AccountId}`.

2. Install zip:
   
- sudo apt install zip
  
3. From the `chatbot` directory, add files to the deployment zip file: `my_deployment_package.zip`:
   
- zip my_deployment_package.zip lambda_function.py
- zip my_deployment_package.zip index.html

4. Copy the deployment zip file to the deployment S3 bucket:

- aws s3 cp my_deployment_package.zip s3://sagemaker-${AWS::Region}-${AWS:AccountId}/sm_chatbot/my_deployment_package.zip

5. Create and configure a Lambda function with latest Python runtime and name: `sm_chatbot`:

- Navigate to Code > Upload from > S3 locatiohn.
- Enter S3 location for zip file.
- Navigate to Configuration > General Configuration.
- Set max values for timeout (15 minutes), memory (10240 MB), and ephemeral storage (10240 MB).
- Navigate to Configuration > Permissions.
- Navigate to Lambda function exeuction role.
- Add `AmazonSageMakerFullAccess` to Lambda function execution role.

6. Create and configure an API Gateway REST API with name: `SMChatbot`

- Create an `ANY` method of Lambda function type.
- Set Lambda proxy integration to `True`.
- Set Lambda function to the ARN of the `SMChatbot` Lambda function.
- Deploy the API with a new `demo` stage.:

7. Copy and paste the `demo` stage invoke URL into the browser.

