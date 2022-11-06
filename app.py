from flask import Flask, request, jsonify
from transcribe import *
from ytdl import *
import requests
app = Flask(__name__)

# specify URL trigger the function, default method: GET
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/transcribe', methods=['GET'])
def transcribe():
	data = request.get_json()
	url = data['url']

	print(url)
	mp3_file = ytdl_to_mp3(url)
	upload_blob( 'transcriber_audio_files', './' + mp3_file,mp3_file)
	transcript = transcribe_gcs("gs://transcriber_audio_files/" + mp3_file)
	return transcript

 
# ensure Flask app runs only when executed in the main file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)