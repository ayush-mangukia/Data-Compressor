import os
from flask import Flask, render_template, request, url_for, redirect, send_file
from werkzeug.utils import secure_filename
from count import count
from huffman import huffman
from compress import compressor
from ratio import ratio
from decompress import decompressor

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("main.html")

@app.route('/compress')
def compress():
    return render_template("compress.html")

@app.route('/download_compressed')
def download_compressed():
    return send_file('compressed_file.txt',
                     attachment_filename='Compressed_File.txt',
                     as_attachment=True)

@app.route('/download_decompressed')
def download_decompressed():
    return send_file('decompressed_file.txt',
                     attachment_filename='Decompressed_File.txt',
                     as_attachment=True)

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

@app.route("/decompress/huffman", methods = ['GET','POST'])
def decompress_huffman():
    if request.method == 'GET':
        return render_template("decompress_file_huffman.html")
    
    if request.method == 'POST':
        if 'file' not in request.files:
                return redirect(url_for('decompress_huffman'))
        file = request.files['file']
        if os.path.exists("huffman.pkl"):
            os.remove("huffman.pkl")
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), filename))
        os.rename(filename,"huffman.pkl")
        return redirect(url_for('decompress_file'))

@app.route("/decompress/file", methods = ['GET','POST'])
def decompress_file():
    if request.method == 'GET':
        return render_template("decompress_file_file.html")
    
    if request.method == 'POST':
        if 'file' not in request.files:
                return redirect(url_for('decompress_file'))
        file = request.files['file']
        if os.path.exists("compressed_file.txt"):
            os.remove("compressed_file.txt")
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), filename))
        os.rename(filename,"compressed_file.txt")
        decompressor()
        return render_template("decompress.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)