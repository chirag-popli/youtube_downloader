from flask import Flask,render_template,request
from pytube import YouTube
app = Flask(__name__)


@app.route('/')
def main1():
    return render_template('app.html')
@app.route('/main',methods=['GET','POST'])
def main():
    link=request.form['link']
    llink=request.form['llink']
    yt = YouTube(link)
    title = yt.title
    finales = yt.streams.get_highest_resolution()
    finales.download(output_path=llink)
    return 'Successfully Downloaded'


if __name__ == '__main__':
    app.run(debug=True)