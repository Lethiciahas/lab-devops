from kubernetes import client, config

def get_namespaces():
    config.load_incluster_config()
    result = client.CoreV1Api()
    namespaces = [ns.metadata.name for ns in result.list_namespace().items]
    namespaces_html = '<ul>' + ''.join(f'<li>{ns}</li>' for ns in namespaces) + '</ul>'
    return namespaces_html


def create_namespace(namespace_name):
    config.load_incluster_config()
    api = client.CoreV1Api()

    # Cria um objeto Namespace com o nome especificado
    new_namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace_name))

    # Envia a solicitação de criação do namespace para a API do Kubernetes
    api.create_namespace(new_namespace)

    return f"Namespace '{namespace_name}' criado com sucesso!"


def delete_namespace(namespace_name):
    config.load_incluster_config()
    api = client.CoreV1Api()

    try:
        api.delete_namespace(namespace_name)
        return f"Namespace {namespace_name} foi deletado com sucesso", 200
    except:
        return f"Namespace {namespace_name} não foi encontrado", 404