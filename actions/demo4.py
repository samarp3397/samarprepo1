import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
     def run(self,id):
        try:
                id1= str(id);
                headers={'content-type': 'application/json'}
                url='https://fakerestapi.azurewebsites.net/api/Books/'+id1
                res=requests.get(url,headers=headers,timeout=6.0)
                print(res)
                y=res.json()
                print(y)
        except requets.exceptions.Timeout:
               print("Request timeout")
               sys.exit(0)
