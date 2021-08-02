#!/bin/sh

function install_k8s {

	apt update
	for i in $@
	do
		apt install -y $i
	done

}

install_k8s apt-transport-https ca-certificates curl
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list

install_k8s kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl
