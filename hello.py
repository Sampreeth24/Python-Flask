from flask import Flask #importing the Flask class
app = Flask(__name__) #creating an instance of the Flask class

#use the route() decorator to register the hello_world function for the / route. 
#When this route is requested, hello_world is called and the message “Hello World!” is returned to the client.
@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()

