from flask import Flask
from routes.user_routes import userRoute

app = Flask(__name__)
app.register_blueprint(userRoute)
