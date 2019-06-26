# pip3 install elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch import helpers


def getActions():
	actions = []
	for num in range(0,100):
		action = {
          "email": "asdfas@gmail.com",
          "id": num,
          "mobile": "19823422376",
          "name": "用户abel",
          "createTime": 1553158991278,
          "address": "New York"}
		actions.append(action)
		# es.index(index='user', doc_type='userInfo', body=action, id=None)
	return actions

# es = Elasticsearch(["127.0.0.1"], http_auth=('elasticsearch', 'admin'),port=9200)
es = Elasticsearch(["127.0.0.1"],port=9200)
actions=getActions()
helpers.bulk(es, actions,index="middle_user",doc_type='userInfo', raise_on_error=True)
print("批量插入完成")
