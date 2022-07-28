from chalice import Chalice
from chalice import BadRequestError
from chalice import Response

app = Chalice(app_name='hello')




@app.route('/badrequest')
def badrequest():
    raise BadRequestError("This is a bad request")
    
@app.route('/badresponse')
def badresponse():
    return Response(body='Plain text error message',
                    headers={'Content-Type': 'text/plain'},
                    status_code=400)


@app.route('/')
def index():
    return {'hello': 'world'}
    
@app.route('/a')
def a():
    return {'view': 'a'}
    
@app.route('/a/{first}/b/{second}')
def users(first, second):
    return {'first': first, 'second': second}
    
@app.route('/users/{name}')
def users(name):
    result = {'name': name}
    if app.current_request.query_params is not None and app.current_request.query_params.get('include-greeting') == 'true':
        result['greeting'] = 'Hello, %s' % name
    return result


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
