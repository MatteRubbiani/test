from flask import Flask
from flask_restful import Api


from mele import Mele


app= Flask(__name__)
app.secret_key="Matteo"
api=Api(app)






api.add_resource(Mele, "/mele")



app.run(port=5000, debug=True)
