# Webkrone_Task
# Todo With Asana

![todoasana](https://user-images.githubusercontent.com/90948477/157844378-84fd9692-081e-460e-b3a5-67f02ce1330a.png)

## This is an TODO Webapp using django and Asana Api. Here we can perform CRUD operations in Asana from this todo app.
## For using ASANA API we have to sign in and get all API details
you can visit here [ASANA](https://app.asana.com)
```
ACCESS_TOKEN
CLIENT_ID
```
We can generate a Personal Access Token from the [Asana developer console](https://app.asana.com/0/developer-console). See the [Authentication Quick Start](https://developers.asana.com/docs/authentication-quick-start) for detailed instructions on getting started with PATs.
And also we need to create a workspace in asana.
<li>Click your profile photo and select My Profile Settings from the list</li> 
<li>Click the Account tab</li>
<li>Select Create New Workspace.</li>
<br>
To find our workspace gid and assignee, in the way what i worked on it, it will dynamic when there is more than one assignee and workspace.
put all the details in utils.py and settings.py where i mentioned all the above fields because till my * Access token and client id * will may or may not be work.
To find the workspace gid go to https://app.asana.com/api/1.0/workspaces. 
<br>
<br>
<li>clone repository from here https://github.com/Ameer-Amr/Webkrone_Task.git</li>
<li>go inside directory where <b>manage.py</b> file is located or inside <b>todo_asana</b></li>
<li>now you can install <b>requirements.txt</b></li>

```
pip install -r requirements.txt
```

<li> if you want to create virtualenv you can create that and then pip install requirements, after that activate virtualenv and fire your development server</li>
<li>else now going from 3 step you can fire your development server</li>

```
python manage.py runserver
```


