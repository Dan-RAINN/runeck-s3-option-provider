# s3-option-provider

Simple Flask python web app that serves as an option provider for Rundeck, which gives rundeck a list of artifacts stored in an S3 bucket. 

Usage
-----

This application assumes that your .boto file is already set up with AWS credentials or you are running the app from an EC2 instance with an IAM role that has access to your bucket. Pip install the requirements.txt file (preferably in a virtual environment), then replace ['your_bucket_name'] with the name of your bucket like so, 'my-bucket'. After that just run the script on your server. You can then add an option in Rundeck and point to a remote url like http://[s3-option-provider_url]/?artifacts_folder=myfolder/ to get a list of artifacts in a given folder in your S3 bucket. If you don't store your atrifacts in a folder, you can skip the parameter query (?artifacts_folder=myfolder/) in the url.

