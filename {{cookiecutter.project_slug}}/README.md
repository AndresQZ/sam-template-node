# {{cookiecutter.project_name.lower().replace(' ', '-')}}

# Packaging and deployment

This lambda uses AWS SAM to package, test and deploy.

template.yaml defines all resources needed by lambda and allows to define entry point.


# run lambda locally
sam local invoke -e event.json {{cookiecutter.lambda_na}}
```