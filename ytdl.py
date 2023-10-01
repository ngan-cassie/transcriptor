import os
import subprocess
import time
from pytube import YouTube
from google.cloud import storage
from pydub import AudioSegment


def ytdl_to_mp3(url):
    yt = YouTube(url)
    _filename = yt.title
    yt.streams.first().download(output_path=".", filename=_filename + ".mp4")

    time.sleep(10)
    video = AudioSegment.from_file("%s.mp4" % _filename, "mp4")

    mp4 = "%s.mp4" % _filename
    mp3 = "%s.mp3" % _filename
    flac = "%s.flac" % _filename
    audio = video.export(flac, format="flac")
    return flac



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

