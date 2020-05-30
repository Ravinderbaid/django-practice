import requests
def login():
	data = {
	  'username': 'ravinder.baid',
	  'password': 'ravi1234'
	}

	response = requests.post('http://127.0.0.1:8000/api/auth/token/', data=data)
	return response.json()

def get_comments(token):
	headers = {
    	'Authorization': 'JWT %s' % token,
	}
	response = requests.get('http://127.0.0.1:8000/api/comments/', headers=headers)
	return response

def post_comments_one(token):
	"""
			Equivalent curl request
			curl -X POST -H "Authorization: JWT <token>" -H "Content-Type: application/json" -d '{"content":"some reply to another try"}' 
			'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'
	"""
	headers = {
	    'Content-Type': 'application/json',
	    'Authorization': 'JWT %s' % token
	}
	data = '{"content":"Wow this works"}'
	response = requests.post('http://127.0.0.1:8000/api/comments/create/?type=post&slug=legend&parent_id=23', headers= headers, data=data)

	# response = requests.post('http://127.0.0.1:8000/api/comments/create/?type=post&slug=legend', headers= headers, data=data)
	return response.text
#json returns dictionary
#text returns unicode
token = login()
print(token["token"])
# print(get_comments(token["token"]).text) """valid"""
print(post_comments_one(token["token"]))