### Amazon Bedrock Development Workshop: Bedrock Chatbot

Reference: https://catalog.us-east-1.prod.workshops.aws/workshops/0b6e72fe-77ee-4777-98cc-237eec795fdb/en-US/fm/06-chatbot

Deployment and Test instructions:

1. Create and configure a Lambda function: `bedrock_chatbot_yyyymmdd`.

- Navigate to Lambda functions console.
- Click **Create function**.
- Set Function name: `bedrock_chatbot_yyyymmdd` and Runtime: Latest Python runtime.
- Click **Create function**.

2. Add and deploy code for the Lambda function: `bedrock_chatbot_yyyymmdd`.

- Nvigate to Code.
- Copy and paste contents of repo's `lambda_function.py` to file `lambda_function.py`.
- Click **File > Save**.
- Create a new file: `index.html`.
- Copy and paste contents of repo's `index.html` to file `index.html`.
- Click **File > Save**.
- Click **Deploy**.

3. Configure the Lambda function: `bedrock_chatbot_yyyymmdd`.

- Navigate to Configuration > General Configuration.
- Click **Edit**.  Set timeout to 1 minute (60 seconds). Click **Save**.
- Navigate to Configuration > Permissions.
- Navigate to the Lambda function's exeuction role.
- Click **Add permissions > Create inline policy**.
- Click **JSON**.
- Copy and paste the following policy statement:

```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": [
				"bedrock:InvokeModel",
				"bedrock:InvokeModelWithResponseStream",
				"bedrock:ListFoundationModels"
			],
			"Resource": "*",
			"Effect": "Allow"
		},
		{
			"Action": [
				"aoss:APIAccessAll"
			],
			"Resource": "*",
			"Effect": "Allow"
		},
		{
			"Action": [
				"secretsmanager:GetSecretValue"
			],
			"Resource": "*",
			"Effect": "Allow"
		},
		{
			"Action": [
				"ec2:CreateNetworkInterface",
				"ec2:DeleteNetworkInterface",
				"ec2:DescribeNetworkInterfaces"
			],
			"Resource": "*",
			"Effect": "Allow"
		},
		{
			"Action": [
				"logs:CreateLogGroup",
				"logs:CreateLogStream",
				"logs:PutLogEvents"
			],
			"Resource": "*",
			"Effect": "Allow"
		}
	]
}
```

- Click **Next**.
- Set Policy name, e.g.: `bedrock_chatbot_yyyymmdd`.
- Click **Create policy**.
- Navigate back to and refresh the Lambda function's Configuration > Permissions page.
- Confirm the Lambda function's execution role has the newly added permissions.

4. Test the Lambda function: `bedrock_chatbot_yyyymmdd`.

- Navigate to Test.
- Select `Create new event`.
- Set Event name: `test`.
- Copy and paste contents of repo's `test_event.json` to Event JSON.
- Click **Save**.
- Click **Test**.
- Confirm Lambda function executes successfully.

5. Create and configure an API Gateway REST API with name: `bedrock_chatbot_yyyymmdd` and stage: `demo`.

- Navigate to API Gateway APIs console.
- Click **Create API**.
- Click `REST API`.
- Click **Build**.
- Select `New API`.
- Set API Name: `bedrock_chatbot_yyyymmdd` and API endpoint type: `Regional` (default).
- Click **Create API**.
- Navigate to Resources.
- Click **Create method**.
- Set Method type: `ANY`, Integration type: `Lambda function`, and Lambda proxy integration: `True`.
- Set Lambda function: ARN of the `bedrock_chatbot_yyyymmdd` Lambda function.
- Click **Create method**.
- Click **Deploy API**.
- Set Stage: `*New stage*` and Stage name: `demo`.
- Click **Deploy**.

6. Test Bedrock Chatbot: `bedrock_chatbot_yyyymmdd`.

- Copy `demo` stage's Invoke URL: `https://<api id>.execute-api.us-west-2.amazonaws.com/demo`
- Open new web browser tab.
- Past `demo` stage's Invoke URL.
- Wait for Bedrock Chatbot page to appear.
- Enter prompt, e.g., `How are you?`
- Click **Send**.
- Wait for response to appear.
