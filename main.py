import pulumi
import pulumi_digitalocean as do

# Configure the DigitalOcean provider
# Ensure you have your DO_TOKEN environment variable set.
# pulumi config set digitalocean:token YOUR_DIGITALOCEAN_TOKEN

# Create a DigitalOcean Kubernetes cluster
doks_cluster = do.KubernetesCluster("my-doks-cluster",
    region="nyc3",  # Choose your preferred region
    version="1.28.1-do.0", # Specify a Kubernetes version
    node_pool=do.KubernetesClusterNodePoolArgs(
        name="default",
        size="s-2vcpu-4gb",  # Choose your node size
        node_count=3,       # Number of nodes in the pool
    ))

# Export the cluster's endpoint and kubeconfig
pulumi.export("doks_cluster_endpoint", doks_cluster.endpoint)
pulumi.export("doks_cluster_kubeconfig", doks_cluster.kube_config)
