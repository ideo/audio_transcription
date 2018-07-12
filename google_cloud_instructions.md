## Configuring Google Cloud API (DRAFT)

#### Getting Started
1. Create a [Google Cloud](https://cloud.google.com/) account. While Google offers a free trial, you still need to supply a credit card to create and account.
2. Follow the [instructions](https://developers.google.com/api-client-library/python/start/installation) for installing the Python API Library.

#### Create a New Project
1. Navigate to the Google Cloud Platform [Console](https://console.cloud.google.com/home/).
2. Click the project drop down in the upper right and then select NEW PROJECT.
3. Enter a project name and hit CREATE.
4. If the "Project Info" card does not list the project you just created, go back to the project drop down in the upper right and select it.
5. From the "Getting Started" card, select "Enable APIs and get credentials like keys."
6. Select ENABLE APIS AND SERVICES
7. Search for and enable the following APIs:
	* Cloud Natural Language API
	* Cloud Speech API
	* Google Cloud Storage
	* Google Cloud Storage JSON API

#### Authentication
1. Return to the APIs and SERVICES [Dashboard](https://console.cloud.google.com/apis/dashboard)
2. From the left side menu, select "Credentials."
3. From the "Create credentials" drop down, select "Service Account Key."
4. Under the "Service Account" drop down, select "New Service Account."
5. Give it a name. Under "Select a Role," choose "Project" -> "Owner."
6. Create and download a JSON key.
7. Save it in a secure location, then add the folloing like to your `.bash_profile` file:
	`GOOGLE_APPLICATION_CREDENTIALS="path/to/secure/location/service_account_key.json"`  
	Note: Keep this key private. Do not upload this key to GitHub.

<!--May not need this-->
8. Return to your Google Cloud Platform [Dashboard](https://console.cloud.google.com/home/dashboard)
9. From the left side menu select "IAM and admin."
10.