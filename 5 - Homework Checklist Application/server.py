from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

class Test1(Resource):
    def get(self):
        print('restfull connection success') #print to console 
        return "This is test1" # response body

class Test2(Resource):
    def get(self):
        return "This is test2" # response body

class Sum(Resource):
    def get(self):
        args = request.args
        print(args)
        return "sum" # response body
        

api.add_resource(Test1, '/test1')
api.add_resource(Test2, '/test2')
api.add_resource(Sum, '/sum')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5002')
