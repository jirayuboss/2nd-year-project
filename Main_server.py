import requests
import threading
import ssl

from flask import Flask
from flask import session
from flask import redirect
from flask import current_app


app = Flask(__name__)
get_err = False
 
#@app.route('/')
def get_data():
    global get_err
    threading.Timer(5.0, get_data).start()

    try :
        requests.packages.urllib3.disable_warnings()
        reply = requests.get('https://203.154.59.52:5000/check', verify=False).content 
        reply = reply.decode()
        if reply == "Reply back":
	    get_err = False
            print("Server's working // PORT:5000")
        else:
            print("Server timeout")
            
    except requests.exceptions.ReadTimeout as err:
        print("Read timeout")
    except requests.exceptions.ConnectionError as err:
        get_err = True
        print("Connection Error: Server timeout // Connect to PORT:8000")

#@app.route('/')
def redirect_url1(custom_path=""):
    print(custom_path)
    global get_err
    if get_err == False:
        return redirect("https://203.154.59.52:5000/{}".format(custom_path), code=307)
    elif get_err == True:
        return redirect("https://203.154.59.52:8000/{}".format(custom_path), code=307)


app.add_url_rule(
    "/",
    view_func=redirect_url1,
    strict_slashes=False,
    methods=["GET", "POST"])

app.add_url_rule(
    "/<path:custom_path>",
    view_func=redirect_url1,
    strict_slashes=False,
    methods=["GET", "POST"])

 
get_data()
app.run("0.0.0.0",port=5555 ,ssl_context=('cert.pem', 'key.pem'))

