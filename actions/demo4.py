import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
     def run(self,id):
        try:
                x={"ID": id}
                url='https://fakerestapi.azurewebsites.net/api/Books/9'
                res=requests.get(url)
                print(res)
                y=res.json()
                print(y)
        except:
                sys.exit(0)
