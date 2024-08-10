import json

def base_format(data, message):
    return {
        'message': message,
        'data': data
    }
    
def response_json(request, raw):
    return request.make_response(json.dumps(raw), headers={'Content-Type': 'application/json'})