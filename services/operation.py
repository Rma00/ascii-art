from flask import request, jsonify, Response

# Custom Modules:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from middleware.controller import ascii




# ASCII-ARTS:-------------------------------------
def ascii_fonts():
    fonts = ascii.list_available_fonts()
    print('fonts', fonts)

    return jsonify({'code': 200, 'message': "Success !", 'data': fonts}), 200


def ascii_arts():
    # Ensure the request contains JSON
    if not request.is_json:
        return jsonify({'code': 400, "message": "Invalid content type"}), 400

    data = request.json
    if not data.get('text'):
        return jsonify({'code': 400, "message": "TEXT is missing or invalid"}), 400
    
    text = data["text"].upper()
    font = data["font"]
    ascii_arts = ascii.create_ascii_art(text, font)
    print('ascii_arts\n', ascii_arts)
    return Response(ascii_arts, mimetype='text/plain')

