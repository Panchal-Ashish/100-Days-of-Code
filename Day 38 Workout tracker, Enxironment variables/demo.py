import os

## To set an environment variable... Method 1
## Examples
# os.environ["API_KEY"] = '0456'
# print(os.getenv("API_KEY"))


## To use an environment variable... Method 2... using pycharms edit configurations
## define the evnironment variavle in the environment variables section
# a = os.environ['API']
# print(a)


## To use an environment variable... Method 3...
## step 1: install 'env file' plugin... create and env file and store the keys
## step 2: go to edit configuration > envfile
## step 3: check the enable envfile option
## step 4: click on + button to Add an env file...  add the env that we created

# a = os.getenv("ENV_APP_KEY")
# # a = os.environ.get('348c17c3fd7488d4eaf6c4c8f89dbb3a')
# print(a)

