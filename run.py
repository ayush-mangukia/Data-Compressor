import os
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from count import count
from huffman import huffman
from compress import compressor
from ratio import ratio

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("main.html")

@app.route('/compress')
def compress():
    return render_template("compress.html")

@app.route('/compress/file', methods = ['GET','POST'])
def compress_file():
    if request.method == 'GET':
        return render_template("compress_file.html")
    
    if request.method == 'POST':
        if 'file' not in request.files:
                return redirect(url_for(compress_file))
        file = request.files['file']
        if os.path.exists("file.txt"):
            os.remove("file.txt")
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), filename))
        os.rename(filename,"file.txt")
        count()
        huffman()
        compressor()
        orig,comp = ratio()
        return render_template("result.html", orig = orig, comp = comp)

@app.route('/compress/result')
def compress_res():
    return "Hi"
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)