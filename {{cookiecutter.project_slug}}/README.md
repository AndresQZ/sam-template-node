# {{cookiecutter.project_name.replace(' ', '-')}}

# Packaging and deployment

This lambda uses AWS SAM to package, test and deploy.

template.yaml defines all resources needed by lambda and allows to define entry point.


# run lambda locally
sam build -u && sam local invoke -e event.json -n local.env.json {{cookiecutter.lambda_name}}
```