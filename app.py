from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
usuarios = []

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

@app.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    email = request.form['email']
    usuarios.append({'nombre': nombre, 'email': email})
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        usuarios[id]['nombre'] = request.form['nombre']
        usuarios[id]['email'] = request.form['email']
        return redirect(url_for('index'))
    return render_template('editar.html', usuario=usuarios[id], id=id)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    usuarios.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
