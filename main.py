from flask import Flask, render_template, request, redirect, url_for
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/') #homepage
def home():
    return render_template('index.html', data=None) #conecta ao HTML

@app.route('/generate', methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.form.get('link') #pega o dado, no caso o link, do input lá do html com o name 'link'

    if not data:
        return redirect(url_for('home'))
    
    img = qrcode.make(data) #transforma o link acima em uma imagem qr
    img.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," +  b64encode(memory.getvalue()).decode('ascii')
    
    return render_template('index.html', data=base64_img)

@app.route('/clear')
def clear():
    return redirect(url_for('home'))

if __name__ == '__main__': #iniciar server /  digitar no cmd: python main.py
    app.run(debug=True)