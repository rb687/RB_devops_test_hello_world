from flask import Flask, Response, request
from lib.common_utils import is_username_valid, user_exists, get_dob_message, is_request_valid, update_db
import lib.config as config
from lib.config import log
from lib.constants import ERROR_RESPONSE_MESSAGE
from waitress import serve

app = Flask(__name__)

#landing page. Can be used as a health checker endpoint for simple configurations
@app.route("/")
def hello_world_health_check():
    return "I am up and running", 200


@app.route("/hello/<username>", methods=["GET", "PUT"])
def hello_world(username):
    # Ideally we should be using an authentication test here ie. only let authorized users to enter
    # otherwise throw 401. But keeping it simple for now as this is a test code
    if request.method == "GET":
        # We can use Response OOB module but there is no need for it here. To keep the code clean and easily maintained.
        # However, if the response was a template based etc, we would move to render template and
        # response library with Flask.
        log.info("Got a GET request for user {username}".format(username=username) )
        if is_username_valid(username):
            log.info("User name is valid, returning birthday message")
            if user_exists(username):
                return get_dob_message(username)
            else:
                msg = "No data exist for {username}".format(username=username)
                return {"message": msg}, 204
        else:
            log.info("User name is invalid, returning error response")
            return {"message": ERROR_RESPONSE_MESSAGE}, 400
    elif request.method == "PUT":
        req = request.json
        log.info("Received a PUT request for user " + username + " with payload " + str(request.json))
        if is_request_valid(req):
            log.info("PUT request is valid, updating DB")
            update_db(username, req.get('dateOfBirth'))
            log.info("Update successful for {username}".format(username=username))
            return {"message": "Update successful"}, 204
        else:
            log.info("Bad PUT request received, returning error response")
            return {"message": ERROR_RESPONSE_MESSAGE}, 400
    else:
        message = "Illegal call made using method, payload and ip " + request.method + request.json
        log.warning(message)
        #Dont need to return anything, flask will automatically return a 405




if __name__ == "__main__":
    #app.run(host='localhost', port=5555)
    serve(app, host='0.0.0.0', port=5555)