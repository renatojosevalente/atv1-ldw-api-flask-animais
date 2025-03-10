from flask import render_template, request
import urllib
import json

compradores = []
animallist = [{'nome': 'Fido', 'ano': 2020, 'raça': 'Pastor Alemão'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/animals', methods=['GET', 'POST'])
    def animals():
        animal = animallist[0]

        if request.method == 'POST':
            comprador = request.form.get('comprador')
            if comprador:
                compradores.append(comprador)

        return render_template('animals.html', animal=animal, compradores=compradores)

    @app.route('/cadanimals', methods=['GET', 'POST'])
    def cadanimals():
        if request.method == 'POST':
            nome = request.form.get('nome')
            ano = request.form.get('ano')
            raca = request.form.get('raça')

            if nome and ano and raca:
                animallist.append({'nome': nome, 'ano': ano, 'raça': raca})

        return render_template('cadanimals.html', animallist=animallist)
    

    @app.route('/apianimals', methods=['GET', 'POST'])
    def apianimals():
        url = 'https://dog.ceo/api/breed/hound/images'
        res = urllib.request.urlopen(url)
        data = res.read()
        animalsjson = json.loads(data)  # Correção aqui

        # Como o JSON retorna uma chave "message" com a lista de imagens, pegamos apenas essa parte
        images = [{"image_url": img} for img in animalsjson["message"]]

        return render_template('apianimals.html', animalsjson=images)



