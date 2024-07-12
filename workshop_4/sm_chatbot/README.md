### SageMaker Invoke Endpoint API: SageMaker Chatbot

Deployment and Test instructions:

1. Confirm there is a SageMaker S3 bucket with name: `sagemaker-${AWS::Region}-${AWS::AccountId}`.

2. Install zip:
   
- sudo apt install zip
  
3. From the `sm_chatbot` directory, add files to the deployment zip file: `my_deployment_package.zip`:
   
- zip my_deployment_package.zip lambda_function.py
- zip my_deployment_package.zip index.html

4. Upload the deployment zip file to the SageMaker S3 bucket:

- aws s3 cp my_deployment_package.zip s3://sagemaker-${AWS::Region}-${AWS:AccountId}/sm_chatbot_yyyymmdd/my_deployment_package.zip

5. Create and configure a Lambda function with latest Python runtime and name: `sm_chatbot_yyyymmdd`:

- Navigate to Code > Upload from > S3 location: S3 URI.
- Enter S3 location for zip file.
- Navigate to Configuration > General Configuration.
- Set memory (10240 MB), ephemeral storage (10240 MB), max values for timeout (15 minutes). 
- Navigate to Configuration > Permissions.
- Navigate to Lambda function execution role.
- Add `AmazonSageMakerFullAccess` to Lambda function execution role.

6. Create and configure an API Gateway REST API with name: `sm_chatbot_yyyymmdd`

- Create an `ANY` method of Lambda function type.
- Set Lambda proxy integration to `True`.
- Set Lambda function to the ARN of the `sm_chatbot` Lambda function.
- Deploy the API with a new `demo` stage.:

7. Copy and paste the `demo` stage invoke URL into the browser.

