from kubernetes import client, config
import pdb; pdb.set_trace()
config.load_kube_config()
v1 = client.CoreV1Api()


def list_pods():
    """列出pods"""
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces()
    for i in ret.items:
        print(f"{i.status.pod_ip}, {i.metadata.namespace}, {i.metadata.name}")


if __name__ == "__main__":
    list_pods()
