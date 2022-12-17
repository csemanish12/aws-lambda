# aws-lambda

# Working with python
Your python code may or may not need additional packages/libraries to run. 
In order to deploy your code, You need to create a deployment package (a zip file with source code and required packages/libraries) which are not included in lambda runtime environment. These are some of the ways for creating your deployment package.

## Deployment package with no dependency
To create the deployment package

1. Open a command prompt and create a my-lambda-function project directory. For example, on macOS:

```
mkdir my-lambda-function
```

2. Navigate to the my-lambda-function project directory.

```
cd my-lambda-function
```

Copy the contents of the Python code from here and save it in a new file named lambda_function.py. Your directory structure should look like this:

```
my-lambda-function$
| lambda_function.py
```

Add the lambda_function.py file to the root of the .zip file.

```
zip my-deployment-package.zip lambda_function.py
```

This generates a my-deployment-package.zip file in your project directory. The command produces the following output:
```
adding: lambda_function.py (deflated 50%)
```

## Deployment package with dependency

To create the deployment package

Open a command prompt and create a my-sourcecode project directory. For example, on macOS:

```
mkdir my-sourcecode
```

Navigate to the my-sourcecode project directory.

```
cd my-sourcecode
```

Copy the contents of the following sample Python code and save it in a new file named lambda_function.py:

Your directory structure should look like this:

```
my-sourcecode$
| lambda_function.py
```

Install the requests library to a new package directory.

```
pip install --target ./package requests
```

Create a deployment package with the installed library at the root.


```
cd package
zip -r ../my-deployment-package.zip .
```

This generates a my-deployment-package.zip file in your project directory. The command produces the following output:

Add the lambda_function.py file to the root of the zip file.

```
cd ..
zip my-deployment-package.zip lambda_function
```
