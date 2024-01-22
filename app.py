from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_get():

    if request.method == 'POST':
        xml = create_xml(request.data)
        print(request.data)
        return "<h1> XML gerado com sucesso! </h1>"

    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True)