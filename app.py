from flask import Flask,request
from flask_restful import Resource , Api
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
## request module is used to send json Payload

app= Flask(__name__)
app.secret_key="jshsfkfhsfk"
api=Api(app)
jwt=JWT(app,authenticate,identity)

students=[]

class Student(Resource):
    @jwt_required()
    def get(self,name):
        result= next(filter(lambda x: x["name"]==name,students),None)
        #for student in students:
            #if student["name"]== name:
                #return student
        if result==None:
            return {"Error":"No match for specified name"} , 404
        else:
            return result,200

    def post(self,name):
        if next(filter(lambda x: x["name"]==name,students),None) is not None:
            return {"error":"Student already exists"},400
        data=request.get_json()
        students.append({"name":name,"data":data})
        return {"name":name,"data":data, "action":"added"},200

class Students(Resource):
    def get(self):
        if len(students)==0:
            return {"error":"empty"},404
        return students ,200

class Hello(Resource):
    def get(self):
        return {"hello":"World"} ,200


api.add_resource(Student,'/student/<string:name>')
api.add_resource(Students,'/students')
api.add_resource(Hello,'/')


app.run(port=5000, debug=True)
