import asana
from django.conf import settings

ACCESS_TOKEN = "1/1201935082081338:ea1158e3f4cc393895fb3fc2ba767db9",
CLIENT_ID = "1201946381601978",
WORKSPACE = "1201935044185017",
ASSIGNEE = "1201935082081338",

headers = {
    "Asana-Enable": "new_user_task_lists"
}

def call_this():
    client = asana.Client.access_token(ACCESS_TOKEN)

def create_task(payload):
    client = asana.Client.access_token(ACCESS_TOKEN)
    post_task = client.post('/tasks', payload, headers=headers)
    return post_task

def get_all_tasks():
    client = asana.Client.access_token(ACCESS_TOKEN)
    gen_data = client.get("/tasks", {"opt_fields": ["name", "notes", "completed", "created_at", "assignee", "assignee_status"], "assignee": ASSIGNEE, "workspace": WORKSPACE, "limit": "50"}, headers=headers)
    return gen_data

def update_task(payload, gid):
    client = asana.Client.access_token(ACCESS_TOKEN)
    result = client.put(f"/tasks/{gid}", payload, opt_pretty=True, headers=headers)
    return result

def delete_task(gid):
    client = asana.Client.access_token(ACCESS_TOKEN)
    result = client.delete(f'/tasks/{gid}', {'gid': gid}, opt_pretty=True, headers=headers)
    return result
