import requests
import json
headers = {"Content-Type": "application/json"}




# create task
def create_task():
    url = "http://localhost:5000/tasks"
    url = "http://172.29.1.101:5000/tasks"
    # url = "http://18.162.213.147:5000/tasks"
    data = {'name':'2021-01-01','description':'p1','pk':'@YykxvfW6PQvDPuHSEje'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code,response.json())


# get task
def get_task():
    url = "http://localhost:5000/tasks/distribute"
    url = "http://172.29.1.101:5000/tasks/distribute"
    data = {'pk':'@YykxvfW6PQvDPuHSEje'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code,response.json())

# update task status
def update_task():
    url = "http://localhost:5000/tasks/status"
    url = "http://172.29.1.101:5000/tasks/status"
    data = {'status':'completed','id':2,'pk':'@YykxvfW6PQvDPuHSEje'}
    response = requests.put(url, headers=headers, data=json.dumps(data))
    print(response.status_code,response.json())



import requests
import json
headers = {"Content-Type": "application/json"}
import pandas as pd
import datetime
end_dates = pd.date_range('2019-01-01', datetime.datetime.strptime('2021-12-31', "%Y-%m-%d").date())
end_dates = [str(i).replace(' 00:00:00', '') for i in end_dates]
end_dates.sort(reverse=True)
url = "http://172.29.1.101:5000/tasks"
# url = "http://18.162.213.147:5000/tasks"
for i,d in enumerate(end_dates):
    data = {'name': d, 'status': 'todo', 'pk': '@YykxvfW6PQvDPuHSEje'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code, response.json())
    print(data)

