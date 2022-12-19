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

3. Copy the contents of the Python code from [here](https://github.com/csemanish12/aws-lambda/blob/main/lambda_function.py) and save it in a new file named lambda_function.py. Your directory structure should look like this:

```
my-lambda-function$
| lambda_function.py
```

4. Add the lambda_function.py file to the root of the .zip file.

```
zip my-deployment-package.zip lambda_function.py
```

This generates a my-deployment-package.zip file in your project directory. The command produces the following output:
```
adding: lambda_function.py (deflated 50%)
```

## Deployment package with dependency

To create the deployment package

1. Open a command prompt and create a my-sourcecode project directory. For example, on macOS:

```
mkdir my-sourcecode
```

2. Navigate to the my-sourcecode project directory.

```
cd my-sourcecode
```

3. Copy the contents of the following sample Python code from [here](https://github.com/csemanish12/aws-lambda/blob/main/lambda_function.py) and save it in a new file named lambda_function.py:

Your directory structure should look like this:

```
my-sourcecode$
| lambda_function.py
```

4. Install the requests library to a new package directory.

```
pip install --target ./package requests
```

5. Create a deployment package with the installed library at the root.


```
cd package
zip -r ../my-deployment-package.zip .
```

This generates a my-deployment-package.zip file in your project directory. The command produces the following output:

6. Add the lambda_function.py file to the root of the zip file.

```
cd ..
zip my-deployment-package.zip lambda_function
```

## Deployment package while using virtualenv

1. Activate the virtual environment. For example:

```
~/my-function$ source myvenv/bin/activate
```

2. Install libraries with pip.

```
(myvenv) ~/my-function$ pip install requests
```

3. Deactivate the virtual environment.

```
(myvenv) ~/my-function$ deactivate
```

4. Create a deployment package with the installed libraries at the root.

```
~/my-function$cd myvenv/lib/python3.8/site-packages
zip -r ../../../../my-deployment-package.zip .
```

The last command saves the deployment package to the root of the my-function directory.

Tip:

A library may appear in site-packages or dist-packages and the first folder lib or lib64. You can use the pip show command to locate a specific package.

5. Add function code files to the root of your deployment package.

```
~/my-function/myvenv/lib/python3.8/site-packages$ cd ../../../../
~/my-function$ zip -g my-deployment-package.zip lambda_function.py
```

After you complete this step, you should have the following directory structure:

```
my-deployment-package.zip$
  │ lambda_function.py
  │ __pycache__
  │ certifi/
  │ certifi-2020.6.20.dist-info/
  │ chardet/
  │ chardet-3.0.4.dist-info/
  ...
```
