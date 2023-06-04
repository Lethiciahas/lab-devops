from flask import Flask, render_template, request, redirect
from namespaces import get_namespaces, create_namespace, delete_namespace

app = Flask(__name__, template_folder='./templates')


@app.route('/namespaces', methods=['GET', 'POST'])
def namespaces():
    if request.method == 'POST':
        namespace = request.form['namespace']
        create_namespace(namespace)
        return redirect('/namespaces')
    
    namespaces = get_namespaces()
    return render_template('index.html', namespaces=namespaces)


@app.route('/namespaces/delete', methods=['POST'])
def namespaces_delete():
    namespace= request.form.get('namespace')
    delete_namespace(namespace)
##    return status
    return redirect('/namespaces')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)