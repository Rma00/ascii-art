#Custom modules:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from services import operation



def handler(app):

    # ASCII-ARTS ROUTES:-------------------------------------
    @app.route("/ascii_fonts", methods=["GET"])
    def ascii_fonts():
        return operation.ascii_fonts()

    @app.route("/ascii_arts", methods=["POST"])
    def ascii_arts():
        return operation.ascii_arts()

