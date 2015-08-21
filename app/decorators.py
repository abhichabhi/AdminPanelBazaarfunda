from functools import wraps
import json
from bson import json_util
from flask import Response

def mongoJsonify(func):
	@wraps(func)
	def JSON(*args, **kwargs):
		return json.dumps(func(*args, **kwargs), indent = 4, default = json_util.default)
	return JSON

def jsonResponse(func):
	@wraps(func)
	def JSON(*args, **kwargs):
		text = json.dumps(func(*args, **kwargs), indent = 4, default = json_util.default)
		return Response(response = text, status = 200, mimetype = 'application/json')
	return JSON
