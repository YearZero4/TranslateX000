from flask import Flask, render_template, request, Response
import os, requests

app = Flask(__name__)

def translate(texto, i1, i2):
 url = f"https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dj=1&hl=es&ie=UTF-8&oe=UTF-8&ome=auto&otf=1&q={texto}&sl={i1}&tl={i2}"
 response = requests.get(url)
 data = response.json()
 traduccion = data['sentences']
 trans0=''
 for i in enumerate(traduccion):
  trans0+=traduccion[i[0]]['trans'].encode('utf-8').decode('utf-8')
 return trans0

@app.route('/favicon.ico')
def favicon():
 return Response(status=204)

@app.route('/', methods=['GET', 'POST'])
def index():
 contenido = ""
 if request.method == 'POST':
  traducir = request.form['traducir']
  i1 = request.form['idioma1']
  i2 = request.form['idioma2']
  contenido = translate(traducir, i1, i2)
 return render_template('index.html', contenido=contenido)

if __name__ == '__main__':
 app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
