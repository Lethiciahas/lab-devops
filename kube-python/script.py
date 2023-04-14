from kubernetes import client, config
from flask import Flask, Markup


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_namespaces():
    config.load_incluster_config()
    result = client.CoreV1Api()
    namespaces = [ns.metadata.name for ns in result.list_namespace().items]
    namespaces_html = Markup('<ul>' + ''.join(f'<li>{ns}</li>' for ns in namespaces) + '</ul>')

   
    return f"<meta http-equiv='refresh' content='10'>Listando Namespaces: {namespaces_html}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
