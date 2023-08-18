from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# User homepage for selecting language and making get request using without reloading page
@app.route('/')
def homePage():
    return render_template('index.html')

# hello api
@app.route('/hello', methods=['GET'])
def hello_world_api():
    
    # Accepting the language input from get request
    language = request.args.get('language', None)
    
    # If language parameter is not passed as argument
    if language is None:
        error_response = {
            "error_message": "Language parameter is required"
        }
        return jsonify(error_response), 400
    
    # Dictionary containing language name along with translation
    greetings = {
        'english': 'Hello world',
        'french': 'Bonjour le monde',
        'hindi': 'Namastey sansar'
    }
    
    language = language.lower()
    
    # checks whether the language given is supported
    # If yes, then end the JOSN containing ID and the translated message
    if language in greetings:
        response_data = {
            "ID" : "A123456789",
            "msgText": greetings[language]
        }
        return jsonify(response_data), 200
    else:
        # runs when the language is not supported by api
        error_response = {
            "error_message": "The requested language is not supported"
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
