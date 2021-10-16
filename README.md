# Blue-Green SAM

This project showcase a blue-green deployment in AWS.

## Requirements for building and deploying

* SAM CLI - [Install the SAM CLI][1]
* [Python 3 installed][2]
* Docker - [Install Docker community edition][3]
* An [AWS account][4] (If you like to host the solution yourself)


## Install requirements
```bash
pip3 install -r src/requirements.txt
pip3 install -r tests/requirements.txt
```
## Build
```bash
sam build --use-container
```

## Run tests
```bash
pytest
```
## Run local
```bash
sam local invoke
```

## Deploy to AWS
*Requires that AWS credentials are configured*
```bash
sam deploy --resolve-s3 --no-confirm-changeset
```

...and you should get an output similar to this:

```
CloudFormation outputs from deployed stack
--------------------------------------------------------------------------------------------------------------
...
Key HelloWorldApi
Description       API Gateway endpoint URL for Prod stage for Hello World function
Value             https://abcd7efghi.execute-api.eu-west-1.amazonaws.com/Prod/hello/
...
--------------------------------------------------------------------------------------------------------------
```

Click the url and enjoy the beautiful restful response!

## Propose a change

To propose an awesome change, make a pull-request in the very complex [/src/app.py](./src/app.py) file.  
Note the `pytest` unit test will fail if the response do not start with the most awesome translating service in the world.

## Adopt deployment strategy

The deployment is a blue-green approach by utilizing the `AllAtOnce` deployment preference built into AWS SAM. Try out [other strategies][5] by modifying the SAM [template.yaml](./template.yaml) file.


[1]: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
[2]: https://www.python.org/downloads/
[3]: https://hub.docker.com/search/?type=edition&offering=community
[4]: https://console.aws.amazon.com/
[5]: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html