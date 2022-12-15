# create a resource group for the AKS cluster
az group create --name my-aks-cluster --location eastus

# create the AKS cluster
az aks create --resource-group my-aks-cluster --name my-aks-cluster --node-count 3 --generate-ssh-keys

# get the credentials for the AKS cluster
az aks get-credentials --resource-group my-aks-cluster --name my-aks-cluster

# verify that the AKS cluster is running
# create a Secret with the bank balances
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: bank-balances
type: Opaque
data:
  john-doe: NDk3
  jane-doe: NjUx
EOF

kubectl apply -f deployment.yaml
