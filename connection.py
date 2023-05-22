from flask import Flask 
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class Request(Resource):
    def post(self,data):
        pass
        
api.add_resource(Request,"/detect/<string:data>")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
    