from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def submit_resume():
    return make_response({"res":"success"}, 200)


if __name__ == '__main__':
    app.run()

# getting_input_data_from_google_cloud('hackathon1415');
