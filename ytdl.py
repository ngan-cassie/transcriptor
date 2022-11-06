import os
import subprocess
import time
from pytube import YouTube
from google.cloud import storage
from app import app


def ytdl_to_mp3(url):
    yt = YouTube(url)
    _filename = yt.title
    # yt = YouTube('https://www.youtube.com/watch?v=J38Yq85ZoyY')
	# video = yt.streams.filter(only_audio=True).first()
    yt.streams.first().download(output_path=".", filename=_filename + ".mp4")

	# out_file = video.download(output_path=".")
    # audio.download(output_path=".", filename=_filename)
    time.sleep(10)
	# base, ext = os.path.splitext(out_file)
    mp4 = "%s.mp4" % _filename
    mp3 = "%s.mp3" % _filename
    # default_name = yt.title + '.mp4'
    # new_file = 'youtube4.mp3'
    ffmpeg = "ffmpeg -i " +  "\"" + mp4 + "\" " + "\"" + mp3 + "\""
    print(ffmpeg)
    subprocess.run(ffmpeg, shell=True)
    return mp3



def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket: bucket_name = "your-bucket-name"
    # The path to your file to upload: source_file_name = "local/path/to/file"
    # The ID of your GCS object: destination_blob_name = "storage-object-name"

    storage_client = storage.Client("transcriber-366902")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

