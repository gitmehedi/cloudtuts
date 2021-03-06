# Certified Kubernetes Application Developer (CKAD) 
A set of exercises that helped me prepare for the Certified Kubernetes Application Developer exam, offered by the Cloud Native Computing Foundation, organized by curriculum domain. They may as well serve as learning and practicing with Kubernetes.

During the exam, you are allowed to keep only one other browser tab open to refer official documentation. Make a mental note of the breadcrumb at the start of the excercise section, to quickly locate the relevant document in kubernetes.io. It is recommended that you read official documents before attempting exercises below it.

Table of Contents
==================
* [Document History](#document-history)
* [Chapter 1: Core Concepts  (13%)](#chapter-1-core-concepts--13)
   * [PODS](#pods) 
   * [ReplicaSets](#replicasets)
   * [Deployments](#deployments)
   * [Namespaces](#namespaces)
   * [Resource Quota](#resource-quota)
   * [Imperative Commands](#imperative-commands)   

* [Chapter 2: Configuration (18%)](#chapter-2-configuration-18)
   * [Environment Variables](#environment-variables) 
   * [ConfigMaps](#configmaps)
   * [Secrets](#secrets)
   * [Docker Security](#docker-security)
   * [Security Contexts](#security-contexts)
   * [Service Account](#service-account)
   * [Resource Requirements](#resource-requirements)
   * [Taints and Tolerations](#taints-and-tolerations)
   * [Node Selectors](#node-selectors)
   * [Node Affinity](#node-affinity)
   
* [Chapter 3: Multi-Container Pods (10%)](#chapter-3-multi-container-pods-10)
   * [Multi-Container Pods](#multi-container-pods)

* [Chapter 4: Observability (18%)](#chapter-4-observability-18)
   * [Readiness Probes](#readiness-probes)
   * [Liveness Probes](#liveness-probes)
   * [Container Logging](#container-logging)
   * [Monitor and Debug Application](#monitor-and-debug-application)
   
* [Chapter 5: Pod Design (20%)](#chapter-5-pod-design-20)
   * [Labels, Selectors and Annotations](#labels-selectors-and-annotations)
   * [Rolling Updates and Rollback in Deployments](#rolling-updates-and-rollback-in-deployments)
   * [Update Deployments](#update-deployments)
   * [Jobs](#jobs)
   * [CronJobs](#cronjobs)
  
* [Chapter 6: Services & Networking (13%)](#chapter-6-services--networking-13)
   * [Services](#services)
   * [Ingress Networking](#ingress-networking)
   * [Network Policies](#network-policies)
  
* [Chapter 7: State Persistence (8%)](#chapter-7-state-persistence-8)
   * [Volumes](#volumes)
   * [Persistent Volumes](#persistent-volumes)
   * [Persistent Volume Claims](#persistent-volume-claims)
   * [Storage Classes](#storage-classes)
   * [Stateful Sets](#stateful-sets)
   * [Headless Services](#headless-services)
     
* [Appendix](#appendix)
   * [Kubernetes Primary Commands](#kubernetes-primary-commands)
   * [Kubectl Options](#kubectl-options)
   * [ETCD Server Commands](#etcd-server-commands)
   * [Firewall Related Commands](#firewall-related-commands)
   * [Kubernetes Imperative Commands ](#kubernetes-imperative-commands)
   * [Namespace](#namespace)
   * [Kubernetes Configuration Directory Architecture](#kubernetes-configuration-directory-architecture)

## Document History

```
Document History:
2020-12-18	V1 Mehedi Hasan  "Certified Kubernetes Applcation Developer (CKAD) Curriculum"
```


# Chapter 1: Core Concepts  (13%)
   ## PODS 
   A pod is the smallest execution unit in Kubernetes. A pod encapsulates one or more applications. Pods are ephemeral 
   by nature, if a pod (or the node it executes on) fails, Kubernetes can automatically create a new replica of that 
   pod to continue operations. Pods include one or more containers (such as Docker containers).
   Pods can be represent in YAML
   ```bash
   -- Create a pod with docker image nginx 

    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: nging
      name: nging
    spec:
      containers:
      - image: nginx
        name: nging
        resources: {}
      dnsPolicy: ClusterFirst
      restartPolicy: Always
    status: {}
   ```
   A pods can be create in kubernetes using YAML file or directory from command line using kubernetes imperative command.
   
   **Create Pod using YAML File**
   ```bash
   -- create a file with image redis and store all information in a YAML file named 'redis.yaml'
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: nging
      name: nging
    spec:
      containers:
      - image: nginx
        name: nging
        resources: {}
      dnsPolicy: ClusterFirst
      restartPolicy: Always
    status: {}

    -- run the file using kuberneted imperative commands
    $ kubernetes create -f redis.yaml
   ```

   **Create Pods using Kubernetes Imperative Command**
   ```bash 
   -- Start a nginx pod.
   $ kubectl run nginx --image=nginx
  
   -- Start a hazelcast pod and let the container expose port 5701.
   $ kubectl run hazelcast --image=hazelcast/hazelcast --port=5701
  
   -- Start a hazelcast pod and set environment variables "DNS_DOMAIN=cluster" and "POD_NAMESPACE=default" in the
   container.
   $ kubectl run hazelcast --image=hazelcast/hazelcast --env="DNS_DOMAIN=cluster" --env="POD_NAMESPACE=default"
  
   -- Start a hazelcast pod and set labels "app=hazelcast" and "env=prod" in the container.
   $ kubectl run hazelcast --image=hazelcast/hazelcast --labels="app=hazelcast,env=prod"
  
   -- Dry run. Print the corresponding API objects without creating them.
   $ kubectl run nginx --image=nginx --dry-run=client
  
   -- Start a nginx pod, but overload the spec with a partial set of values parsed from JSON.
   $ kubectl run nginx --image=nginx --overrides='{ "apiVersion": "v1", "spec": { ... } }'
  
   -- Start a busybox pod and keep it in the foreground, don't restart it if it exits.
   $ kubectl run -i -t busybox --image=busybox --restart=Never
  
   -- Start the nginx pod using the default command, but use custom arguments (arg1 .. argN) for that command.
   $ kubectl run nginx --image=nginx -- <arg1> <arg2> ... <argN>
  
   -- Start the nginx pod using a different command and custom arguments.
   $ kubectl run nginx --image=nginx --command -- <cmd> <arg1> ... <argN>
   ```

   **Edit Pods**  
   * If you are given a pod definition file, edit that file and use it to create a new pod.  
   * If you are not given a pod definition file, you may extract the definition to a file using the below command:  
     ```$ kubectl get pod <pod-name> -o yaml > pod-definition.yaml```  
   * Then edit the file to make the necessary changes, delete and re-create the pod. Use below command to edit pod properties.  
   ```$ kubectl edit pod <pod-name>```
   
   #### Command References
   ```bash
   -- complete command
   $ kubectl run hazelcast --image hazelcast/hazelcast --port=5071 --labels="app=hazelcast,env=prod" --env="DNS_DOMAIN=cluster" --env="POD_NAMESPACE=default" --restart=Never --command -- start.sh start stop
   ```
  
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/workloads/pods/
   
   ## ReplicaSets
   
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/workloads/pods/
   
   ## Deployments
   
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/workloads/pods/
   
   ## Namespaces
   
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/workloads/pods/
   
   ## Resource Quota
   ```bash
   apiVersion: v1
kind: List
items:
- apiVersion: v1
  kind: ResourceQuota
  metadata:
    name: pods-high
  spec:
    hard:
      cpu: "1000"
      memory: 200Gi
      pods: "10"
    scopeSelector:
      matchExpressions:
      - operator : In
        scopeName: PriorityClass
        values: ["high"]
- apiVersion: v1
  kind: ResourceQuota
  metadata:
    name: pods-medium
  spec:
    hard:
      cpu: "10"
      memory: 20Gi
      pods: "10"
    scopeSelector:
      matchExpressions:
      - operator : In
        scopeName: PriorityClass
        values: ["medium"]
- apiVersion: v1
  kind: ResourceQuota
  metadata:
    name: pods-low
  spec:
    hard:
      cpu: "5"
      memory: 10Gi
      pods: "10"
    scopeSelector:
      matchExpressions:
      - operator : In
        scopeName: PriorityClass
        values: ["low"]   
```
   
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/policy/resource-quotas/
   
   ## Imperative Commands
   
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/workloads/pods/

# Chapter 2: Configuration (18%)
   ## Environment Variables    
   ## ConfigMaps
   ## Secrets
   ## Docker Security
   ## Security Contexts
   ## Service Account
   ## Resource Requirements
   ## Taints and Tolerations
   ## Node Selectors
   ## Node Affinity
   
# Chapter 3: Multi-Container Pods (10%)
   ## Multi-Container Pods


# Chapter 4: Observability (18%)
   ## Readiness Probes
   ## Liveness Probes
   ## Container Logging
   ## Monitor and Debug Application

# Chapter 5: Pod Design (20%)
   ## Labels, Selectors and Annotations
   ## Rolling Updates and Rollback in Deployments
   ## Update Deployments
   ## Jobs
   ##  CronJobs
   
# Chapter 6: Services & Networking (13%)
   ## Services
   ## Ingress Networking
   ## Network Policies
   
# Chapter 7: State Persistence (8%)
   ## Volumes
   ## Persistent Volumes
   ## Persistent Volume Claims
   ## Storage Classes
   ## Stateful Sets
   ## Headless Services

## Appendix:

* https://kubernetes.io/docs/reference/kubectl/overview/
* https://v1-17.docs.kubernetes.io/docs/reference/kubectl/conventions/#generators
* https://kubernetes.io/docs/reference/kubectl/cheatsheet/
* https://github.com/dennyzhang/cheatsheet-kubernetes-A4
* https://cheatsheet.dennyzhang.com/cheatsheet-kubernetes-A4
* https://cheatsheet.dennyzhang.com/kubernetes-yaml-templates

### Kubernetes Primary Commands
```
kubectl controls the Kubernetes cluster manager.

 Find more information at: https://kubernetes.io/docs/reference/kubectl/overview/

Basic Commands (Beginner):
  create         Create a resource from a file or from stdin.
  expose         Take a replication controller, service, deployment or pod and expose it as a new Kubernetes Service
  run            Run a particular image on the cluster
  set            Set specific features on objects

Basic Commands (Intermediate):
  explain        Documentation of resources
  get            Display one or many resources
  edit           Edit a resource on the server
  delete         Delete resources by filenames, stdin, resources and names, or by resources and label selector

Deploy Commands:
  rollout        Manage the rollout of a resource
  scale          Set a new size for a Deployment, ReplicaSet, Replication Controller, or Job
  autoscale      Auto-scale a Deployment, ReplicaSet, or ReplicationController

Cluster Management Commands:
  certificate    Modify certificate resources.
  cluster-info   Display cluster info
  top            Display Resource (CPU/Memory/Storage) usage.
  cordon         Mark node as unschedulable
  uncordon       Mark node as schedulable
  drain          Drain node in preparation for maintenance
  taint          Update the taints on one or more nodes

Troubleshooting and Debugging Commands:
  describe       Show details of a specific resource or group of resources
  logs           Print the logs for a container in a pod
  attach         Attach to a running container
  exec           Execute a command in a container
  port-forward   Forward one or more local ports to a pod
  proxy          Run a proxy to the Kubernetes API server
  cp             Copy files and directories to and from containers.
  auth           Inspect authorization

Advanced Commands:
  diff           Diff live version against would-be applied version
  apply          Apply a configuration to a resource by filename or stdin
  patch          Update field(s) of a resource using strategic merge patch
  replace        Replace a resource by filename or stdin
  wait           Experimental: Wait for a specific condition on one or many resources.
  convert        Convert config files between different API versions
  kustomize      Build a kustomization target from a directory or a remote url.

Settings Commands:
  label          Update the labels on a resource
  annotate       Update the annotations on a resource
  completion     Output shell completion code for the specified shell (bash or zsh)

Other Commands:
  api-resources  Print the supported API resources on the server
  api-versions   Print the supported API versions on the server, in the form of "group/version"
  config         Modify kubeconfig files
  plugin         Provides utilities for interacting with plugins.
  version        Print the client and server version information
```

### Kubectl Options
```
The following options can be passed to any command:

      --alsologtostderr=false: log to standard error as well as files
      --as='': Username to impersonate for the operation
      --as-group=[]: Group to impersonate for the operation, this flag can be repeated to specify multiple groups.
      --cache-dir='/Users/beast/.kube/http-cache': Default HTTP cache directory
      --certificate-authority='': Path to a cert file for the certificate authority
      --client-certificate='': Path to a client certificate file for TLS
      --client-key='': Path to a client key file for TLS
      --cluster='': The name of the kubeconfig cluster to use
      --context='': The name of the kubeconfig context to use
      --insecure-skip-tls-verify=false: If true, the server's certificate will not be checked for validity. This will
make your HTTPS connections insecure
      --kubeconfig='': Path to the kubeconfig file to use for CLI requests.
      --log-backtrace-at=:0: when logging hits line file:N, emit a stack trace
      --log-dir='': If non-empty, write log files in this directory
      --log-file='': If non-empty, use this log file
      --log-flush-frequency=5s: Maximum number of seconds between log flushes
      --logtostderr=true: log to standard error instead of files
      --match-server-version=false: Require server version to match client version
  -n, --namespace='': If present, the namespace scope for this CLI request
      --password='': Password for basic authentication to the API server
      --profile='none': Name of profile to capture. One of (none|cpu|heap|goroutine|threadcreate|block|mutex)
      --profile-output='profile.pprof': Name of the file to write the profile to
      --request-timeout='0': The length of time to wait before giving up on a single server request. Non-zero values
should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -s, --server='': The address and port of the Kubernetes API server
      --skip-headers=false: If true, avoid header prefixes in the log messages
      --stderrthreshold=2: logs at or above this threshold go to stderr
      --token='': Bearer token for authentication to the API server
      --user='': The name of the kubeconfig user to use
      --username='': Username for basic authentication to the API server
  -v, --v=0: number for the log level verbosity
      --vmodule=: comma-separated list of pattern=N settings for file-filtered logging
```

### ETCD Server Commands

```bash
$ kubectl exec etcd-kube-master -n kube-system etcdctl
NAME:
	etcdctl - A simple command line client for etcd3.

USAGE:
	etcdctl [flags]

VERSION:
	3.4.3

API VERSION:
	3.4


COMMANDS:
	alarm disarm		Disarms all alarms
	alarm list		Lists all alarms
	auth disable		Disables authentication
	auth enable		Enables authentication
	check datascale		Check the memory usage of holding data for different workloads on a given server endpoint.
	check perf		Check the performance of the etcd cluster
	compaction		Compacts the event history in etcd
	defrag			Defragments the storage of the etcd members with given endpoints
	del			Removes the specified key or range of keys [key, range_end)
	elect			Observes and participates in leader election
	endpoint hashkv		Prints the KV history hash for each endpoint in --endpoints
	endpoint health		Checks the healthiness of endpoints specified in `--endpoints` flag
	endpoint status		Prints out the status of endpoints specified in `--endpoints` flag
	get			Gets the key or a range of keys
	help			Help about any command
	lease grant		Creates leases
	lease keep-alive	Keeps leases alive (renew)
	lease list		List all active leases
	lease revoke		Revokes leases
	lease timetolive	Get lease information
	lock			Acquires a named lock
	make-mirror		Makes a mirror at the destination etcd cluster
	member add		Adds a member into the cluster
	member list		Lists all members in the cluster
	member promote		Promotes a non-voting member in the cluster
	member remove		Removes a member from the cluster
	member update		Updates a member in the cluster
	migrate			Migrates keys in a v2 store to a mvcc store
	move-leader		Transfers leadership to another etcd cluster member.
	put			Puts the given key into the store
	role add		Adds a new role
	role delete		Deletes a role
	role get		Gets detailed information of a role
	role grant-permission	Grants a key to a role
	role list		Lists all roles
	role revoke-permission	Revokes a key from a role
	snapshot restore	Restores an etcd member snapshot to an etcd directory
	snapshot save		Stores an etcd node backend snapshot to a given file
	snapshot status		Gets backend snapshot status of a given file
	txn			Txn processes all the requests in one transaction
	user add		Adds a new user
	user delete		Deletes a user
	user get		Gets detailed information of a user
	user grant-role		Grants a role to a user
	user list		Lists all users
	user passwd		Changes password of user
	user revoke-role	Revokes a role from a user
	version			Prints the version of etcdctl
	watch			Watches events stream on keys or prefixes

OPTIONS:
      --cacert=""				verify certificates of TLS-enabled secure servers using this CA bundle
      --cert=""					identify secure client using this TLS certificate file
      --command-timeout=5s			timeout for short running command (excluding dial timeout)
      --debug[=false]				enable client-side debug logging
      --dial-timeout=2s				dial timeout for client connections
  -d, --discovery-srv=""			domain name to query for SRV records describing cluster endpoints
      --discovery-srv-name=""			service name to query when using DNS discovery
      --endpoints=[127.0.0.1:2379]		gRPC endpoints
  -h, --help[=false]				help for etcdctl
      --hex[=false]				print byte strings as hex encoded strings
      --insecure-discovery[=true]		accept insecure SRV records describing cluster endpoints
      --insecure-skip-tls-verify[=false]	skip server certificate verification
      --insecure-transport[=true]		disable transport security for client connections
      --keepalive-time=2s			keepalive time for client connections
      --keepalive-timeout=6s			keepalive timeout for client connections
      --key=""					identify secure client using this TLS key file
      --password=""				password for authentication (if this option is used, --user option shouldn't include password)
      --user=""					username[:password] for authentication (prompt if password is not supplied)
  -w, --write-out="simple"			set the output format (fields, json, protobuf, simple, table)
```

### Firewall Related Commands

```bash
$ sudo iptables -t nat -L
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  anywhere             anywhere             ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  anywhere            !localhost/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
MASQUERADE  all  --  172.17.0.0/16        anywhere            
MASQUERADE  all  --  172.21.0.0/16        anywhere            
MASQUERADE  all  --  10.80.95.0/24        anywhere            
MASQUERADE  all  --  172.18.0.0/16        anywhere            
RETURN     all  --  192.168.122.0/24     base-address.mcast.net/24 
RETURN     all  --  192.168.122.0/24     255.255.255.255     
MASQUERADE  tcp  --  192.168.122.0/24    !192.168.122.0/24     masq ports: 1024-65535
MASQUERADE  udp  --  192.168.122.0/24    !192.168.122.0/24     masq ports: 1024-65535
MASQUERADE  all  --  192.168.122.0/24    !192.168.122.0/24    
MASQUERADE  all  --  192.168.56.0/24      anywhere            

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  anywhere             anywhere            
RETURN     all  --  anywhere             anywhere            
RETURN     all  --  anywhere             anywhere            
RETURN     all  --  anywhere             anywhere            

```

```bash
$ sysctl -p
$ firewall-cmd --get-default-zone
public

$ firewall-cmd --get-active-zones
public
  interfaces: eno2 wlo1

$ firewall-cmd --get-zones
block dmz drop external home internal public trusted work

--enable masquerade
$ firewall-cmd --zone=public --add-masquerade
$ firewall-cmd --add-masquerade --zone=public --permanent
$ firewall-cmd --zone=external --query-masquerade


firewall-cmd --zone=external --add-forward-port=port=22:proto=tcp:toport=3753
firewall-cmd --permanent --zone=external --add-forward-port=port=22:proto=tcp:toport=3753:toaddr=10.0.0.1
firewall-cmd --reload
```

### Kubernetes Imperative Commands 
Run and Create

```bash
-- create pods
$ kubectl run --generator=run-pod/v1 nginx --image=nginx
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --dry-run -o yaml

-- create deployments 
$ kubectl create deployment --image=nginx nginx
$ kubectl create deployment --image=nginx nginx --dry-run -o yaml
$ kubectl create deployment --image=nginx nginx --replicas=4 --dry-run -o yaml

-- create services for pod and deployment
$ kubectl expose po nginx --name=nginx --type=NodePort --port=80 --target-port=80 --protocol=TCP
$ kubectl expose deploy nginx --name=nginx --type=NodePort --port=80 --target-port=80 --protocol=TCP

-- create a configmap 
$ kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2
$ kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt

-- create secret 
$ kubectl create secret generic my-secret --from-literal=key1=config1 --from-literal=key2=config2
$ kubectl create secret generic my-secret --from-file=path/to/bar

-- create namespaces
$ kubectl create namespace my-namespace

-- create role 
$ kubectl create role foo --verb=get,list,watch --resource=rs.extensions

-- create roleBindings
$ kubectl create rolebinding admin --clusterrole=admin --user=user1 --user=user2 --group=group1

-- create cluster role 
$ kubectl create clusterrole foo --verb=get,list,watch --resource=rs.extensions

-- create cluster role bindings 
$ kubectl create clusterrolebinding <choose-a-name> --clusterrole=cluster-admin --user=<your-cloud-email-account>

-- create serviceAccount
$ kubectl create serviceaccount my-service-account
```
#### References
* https://kubectl.docs.kubernetes.io/pages/imperative_porcelain/creating_resources.html
* https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
### Namespace

```bash
$ kubectl create namespace dev
$ kubectl config current-context
$ kubectl config set-context $(kubectl config current-context) --namespace dev

$ kubectl config current-context
kubernetes-admin@kubernetes
```
### Kubernetes Configuration Directory Architecture
```
    /etc/kubernetes/
    ????????? admin.conf
    ????????? controller-manager.conf
    ????????? kubelet.conf
    ????????? manifests
    ???   ????????? etcd.yaml
    ???   ????????? kube-apiserver.yaml
    ???   ????????? kube-controller-manager.yaml
    ???   ????????? kube-scheduler.yaml
    ????????? pki
    ???   ????????? apiserver.crt
    ???   ????????? apiserver-etcd-client.crt
    ???   ????????? apiserver-etcd-client.key
    ???   ????????? apiserver.key
    ???   ????????? apiserver-kubelet-client.crt
    ???   ????????? apiserver-kubelet-client.key
    ???   ????????? ca.crt
    ???   ????????? ca.key
    ???   ????????? etcd
    ???   ???   ????????? ca.crt
    ???   ???   ????????? ca.key
    ???   ???   ????????? healthcheck-client.crt
    ???   ???   ????????? healthcheck-client.key
    ???   ???   ????????? peer.crt
    ???   ???   ????????? peer.key
    ???   ???   ????????? server.crt
    ???   ???   ????????? server.key
    ???   ????????? front-proxy-ca.crt
    ???   ????????? front-proxy-ca.key
    ???   ????????? front-proxy-client.crt
    ???   ????????? front-proxy-client.key
    ???   ????????? sa.key
    ???   ????????? sa.pub
    ????????? scheduler.conf
   ```

### Kubectl Run
```
swapon-2:~ beast$ k run -h
Create and run a particular image, possibly replicated.

 Creates a deployment or job to manage the created container(s).

Examples:
  # Start a single instance of nginx.
  kubectl run nginx --image=nginx
  
  # Start a single instance of hazelcast and let the container expose port 5701 .
  kubectl run hazelcast --image=hazelcast --port=5701
  
  # Start a single instance of hazelcast and set environment variables "DNS_DOMAIN=cluster" and "POD_NAMESPACE=default"
in the container.
  kubectl run hazelcast --image=hazelcast --env="DNS_DOMAIN=cluster" --env="POD_NAMESPACE=default"
  
  # Start a single instance of hazelcast and set labels "app=hazelcast" and "env=prod" in the container.
  kubectl run hazelcast --image=hazelcast --labels="app=hazelcast,env=prod"
  
  # Start a replicated instance of nginx.
  kubectl run nginx --image=nginx --replicas=5
  
  # Dry run. Print the corresponding API objects without creating them.
  kubectl run nginx --image=nginx --dry-run
  
  # Start a single instance of nginx, but overload the spec of the deployment with a partial set of values parsed from
JSON.
  kubectl run nginx --image=nginx --overrides='{ "apiVersion": "v1", "spec": { ... } }'
  
  # Start a pod of busybox and keep it in the foreground, don't restart it if it exits.
  kubectl run -i -t busybox --image=busybox --restart=Never
  
  # Start the nginx container using the default command, but use custom arguments (arg1 .. argN) for that command.
  kubectl run nginx --image=nginx -- <arg1> <arg2> ... <argN>
  
  # Start the nginx container using a different command and custom arguments.
  kubectl run nginx --image=nginx --command -- <cmd> <arg1> ... <argN>
  
  # Start the perl container to compute ?? to 2000 places and print it out.
  kubectl run pi --image=perl --restart=OnFailure -- perl -Mbignum=bpi -wle 'print bpi(2000)'
  
  # Start the cron job to compute ?? to 2000 places and print it out every 5 minutes.
  kubectl run pi --schedule="0/5 * * * ?" --image=perl --restart=OnFailure -- perl -Mbignum=bpi -wle 'print bpi(2000)'

Options:
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or map key is missing in
the template. Only applies to golang and jsonpath output formats.
      --attach=false: If true, wait for the Pod to start running, and then attach to the Pod as if 'kubectl attach ...'
were called.  Default false, unless '-i/--stdin' is set, in which case the default is true. With '--restart=Never' the
exit code of the container process is returned.
      --cascade=true: If true, cascade the deletion of the resources managed by this resource (e.g. Pods created by a
ReplicationController).  Default true.
      --command=false: If true and extra arguments are present, use them as the 'command' field in the container, rather
than the 'args' field which is the default.
      --dry-run=false: If true, only print the object that would be sent, without sending it.
      --env=[]: Environment variables to set in the container
      --expose=false: If true, a public, external service is created for the container(s) which are run
  -f, --filename=[]: to use to replace the resource.
      --force=false: Only used when grace-period=0. If true, immediately remove resources from API and bypass graceful
deletion. Note that immediate deletion of some resources may result in inconsistency or data loss and requires
confirmation.
      --generator='': The name of the API generator to use, see
http://kubernetes.io/docs/user-guide/kubectl-conventions/#generators for a list.
      --grace-period=-1: Period of time in seconds given to the resource to terminate gracefully. Ignored if negative.
Set to 1 for immediate shutdown. Can only be set to 0 when --force is true (force deletion).
      --hostport=-1: The host port mapping for the container port. To demonstrate a single-machine container.
      --image='': The image for the container to run.
      --image-pull-policy='': The image pull policy for the container. If left empty, this value will not be specified
by the client and defaulted by the server
  -k, --kustomize='': Process a kustomization directory. This flag can't be used together with -f or -R.
  -l, --labels='': Comma separated labels to apply to the pod(s). Will override previous values.
      --leave-stdin-open=false: If the pod is started in interactive mode or with stdin, leave stdin open after the
first attach completes. By default, stdin will be closed after the first attach completes.
      --limits='': The resource requirement limits for this container.  For example, 'cpu=200m,memory=512Mi'.  Note that
server side components may assign limits depending on the server configuration, such as limit ranges.
  -o, --output='': Output format. One of:
json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-file.
      --overrides='': An inline JSON override for the generated object. If this is non-empty, it is used to override the
generated object. Requires that the object supply a valid apiVersion field.
      --pod-running-timeout=1m0s: The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one
pod is running
      --port='': The port that this container exposes.  If --expose is true, this is also the port used by the service
that is created.
      --quiet=false: If true, suppress prompt messages.
      --record=false: Record current kubectl command in the resource annotation. If set to false, do not record the
command. If set to true, record the command. If not set, default to updating the existing annotation value only if one
already exists.
  -R, --recursive=false: Process the directory used in -f, --filename recursively. Useful when you want to manage
related manifests organized within the same directory.
  -r, --replicas=1: Number of replicas to create for this container. Default is 1.
      --requests='': The resource requirement requests for this container.  For example, 'cpu=100m,memory=256Mi'.  Note
that server side components may assign requests depending on the server configuration, such as limit ranges.
      --restart='Always': The restart policy for this Pod.  Legal values [Always, OnFailure, Never].  If set to 'Always'
a deployment is created, if set to 'OnFailure' a job is created, if set to 'Never', a regular pod is created. For the
latter two --replicas must be 1.  Default 'Always', for CronJobs `Never`.
      --rm=false: If true, delete resources created in this command for attached containers.
      --save-config=false: If true, the configuration of current object will be saved in its annotation. Otherwise, the
annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.
      --schedule='': A schedule in the Cron format the job should be run with.
      --service-generator='service/v2': The name of the generator to use for creating a service.  Only used if --expose
is true
      --service-overrides='': An inline JSON override for the generated service object. If this is non-empty, it is used
to override the generated object. Requires that the object supply a valid apiVersion field.  Only used if --expose is
true.
      --serviceaccount='': Service account to set in the pod spec
  -i, --stdin=false: Keep stdin open on the container(s) in the pod, even if nothing is attached.
      --template='': Template string or path to template file to use when -o=go-template, -o=go-template-file. The
template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].
      --timeout=0s: The length of time to wait before giving up on a delete, zero means determine a timeout from the
size of the object
  -t, --tty=false: Allocated a TTY for each container in the pod.
      --wait=false: If true, wait for resources to be gone before returning. This waits for finalizers.
```
## Questions ans Preparation

#### Dumps
* https://medium.com/@sensri108/practice-examples-dumps-tips-for-cka-ckad-certified-kubernetes-administrator-exam-by-cncf-4826233ccc27
* https://killer.sh/course/preview/052229bd-1062-44a4-8aae-f50d0770165a
* https://github.com/dgkanatsios/CKAD-exercises/blob/master/a.core_concepts.md

## Tips

### JSON Path
* [JSON PATH](pages/jsonpath.md)

### Create Alias
```
$ alias k="kubectl"
$ alias kn="kubectl get nodes -o wide"
$ alias kp="kubectl get pods -o wide"
$ alias kd="kubectl get deployment -o wide"
$ alias ks="kubectl get svc -o wide"


$ alias ke="kubectl explain --recursive"
$ alias kdp="kubectl describe pod"
$ alias kdd="kubectl describe deployment"
$ alias kds="kubectl describe service"
$ alias kdn="kubectl describe node"
$ alias kcr="kubectl run --dry-run=client -o yaml --generator=run-pod/v1"
$ alias kcc="kubectl create --dry-run=client -o yaml"

$ alias k="kubectl" kg="kubectl get -o wide" kd="kubectl describe" kdl="kubectl delete" krd="kubectl run --dry-run=client -o yaml" kcd="kubectl create --dry-run=client -o yaml" kc="kubectl create" kx="kubectl explain --recursive" kr="kubectl run" krd="kubectl run --dry-run -o yaml"
```
* https://medium.com/faun/certified-kubernetes-administrator-cka-tips-and-tricks-part-1-2e98e9b31de4
