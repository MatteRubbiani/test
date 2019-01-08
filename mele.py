from flask_restful import Resource

class Mele (Resource):
    def get(self):
        return "hai gettato delle mele correttamente"

    def post(self):
        return "hai postato delle mele correttamente"
