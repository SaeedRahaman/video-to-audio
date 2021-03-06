from flask import Flask, render_template, request, redirect
import youtube_dl

app = Flask(__name__)

@app.route('/formData', methods=['POST'])
def formData():

   # get form data in dictionary
   # index with url key
   url = request.form['url']
   # print(url)

   opts =  {
      'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192'
      }],
      'ffmpeg_location': 'ffmpeg-4.2.1/ffmpeg',
       'youtube_include_dash_manifest': 'False'
   }

   with youtube_dl.YoutubeDL(opts) as ytdl:
      ytdl.download([url])

   # # make youtube-dl command
   # command = 'python3 youtube_dl/__main__.py -x --audio-format "mp3" --audio-quality 0 --ffmpeg-location ffmpeg-4.2.1/ffmpeg ' + url
   # os.system(command)

   # return to index page with proper url route
   return redirect('/', code=302)

# render html
@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   # run flask
   app.run(debug=True, port=8000)
