Table of Contents
==================

# Chapter 5: Scheduling (5%)
   * [Kubernetes Labels and Selectors to Schedule Pods](#kubernetes-labels-and-selectors-to-schedule-pods)
   * [Role of DaemonSets](#role-of-daemonsets)
   * [Resource Limits and Labels in Pods Scheduling](#resource-limits-and-labels-in-pods-scheduling)
   * [Multiple Schedulers to Run and Configure Pods](#multiple-schedulers-to-run-and-configure-pods)
   * [Manually Schedule a Pods](#manually-schedule-a-pods)
   * [Scheduler Events](#scheduler-events)
   * [Configure Kubernetes Scheduler](#configure-kubernetes-scheduler)

   
## Scheduling
   The default scheduler goes through a series of steps to determine the right node for the pod. 
   1. Is the node running out of resources?
   2. Does the pods request a specific node?
   3. Does the node have a matching label?
   4. If the pod request a port, is it available?
   5. If the pod request a volume, can it be mounted?
   6. Does the pod tolerate the taints of the node?
   7. Does the pod specify node or pod affinity?
   
   Schdueling automatically schedule pod on the right node if kube-scheduler run on the cluster. If a kube-scheduler is not available on the system or has some issue then set an property on pod manifest file called ```nodeName```, it will automatically runs pod in that node.
   
   Schedule pod on node ```node01```.
   ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
         app: application
    spec:
      containers:
      - name: nginx
        image: nginx
      nodeName: node01
   ``` 
   Assign an existing pod into another node using pod binding
   ```
    apiVersion: v1
    kind: Binding
    metadata:
      name: nginx
    target:
      apiVersion: v1
      kind: Node
      name: node02
   ``` 
   **Tips:** Pod binding always request using curl where pod binding definition file converted to json object.
   
   ### Kubernetes Labels and Selectors to Schedule Pods
   Kubernetes uses Labels and Selector internally to group object and connect objection together.
   
   #### Labels
   Lebels used in kubernetes to label an object under the metadata section
   
   ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
         app: application
    spec:
      containers:
      - name: nginx
        image: nginx
   ``` 
   #### Selector
   Kubernetes uses selector to select labels which is defined under metadata section.
   selector can used in selecting labels like ```kubectl get pods -selector app=application```.  
   Selector definition file:
   
   ```bash
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      selector:
        app: application
      ports:
        - protocol: TCP
          port: 80
          targetPort: 9376
   ``` 
   #### Annotations
   Annotations is used to record additional information about a object like build,version,email,phone_no etc under metadata section.
   ```bash
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
         app: application
      annotations:
         build: 12.01.01
         phone: +011 001 0001
    spec:
      containers:
      - name: nginx
        image: nginx
   ``` 

   #### Taints, Toleration, Node Selector and Node Affinity
   ##### Taints
   Taints are applied on a node to repel a set of pods. 
   Add a taints on a node using ```kubectl taint node node_name key:value:taint-effect```
   There are 3 taint-effect
   1. **NoSchedule:** Pods will not be scheduled on the node.
   2. **PreferSchedule:** The system will try to avoid a pod to schedule but no guarantee. 
   3. **NoExecute:** New pod will not schedule and existing pod will evict if they do not tolerate the taint.
   
   ```
   -- add taints on a node
   $ kubectl taint nodes node01 app=blue:NoSchedule
   ```
   This means that no pod will be able to schedule onto ```node01``` unless it has a matching toleration.
   
   ```
   -- remove taints from a node
   $ kubeclt taint nodes node01 app:NoSchedule-
   ```
   
   ##### Toleration
   Tolerations are applied to pods, and allow (but do not require) the pods to schedule onto nodes with matching taints.
   Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. One or more taints are applied to a node; this marks that the node should not accept any pods that do not tolerate the taints.
   You specify a toleration for a pod in the PodSpec. Both of the following tolerations ???match??? the taint created by the kubectl taint line above, and thus a pod with either toleration would be able to schedule onto node1:
   
   ```
   tolerations:
   - key: "app"
     operator: "Equal"
     value: "blue"
     effect: "NoSchedule"

   tolerations:
   - key: "app"
     operator: "Exists"
     effect: "NoSchedule"
   ```
   Tolerations uses in POD
   
   ```
   apiVersion: v1
   kind: Pod
   metadata:
      name: nginx
      labels:
        env: test
   spec:
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
      tolerations:
      - key: "example-key"
        operator: "Exists"
        effect: "NoSchedule"
   ```

   
   ##### Node Selector
   You can constrain a Pod to only be able to run on particular Node(s) , or to prefer to run on particular nodes.
   Labels a node using 
   NodeSelector can perform in two steps:  
   
   **Step 1:**  Attach label to the node
   ```
   -- label a node 
   $ kubectl label nodes <node-name> <label-name>=<label-value>
   $ kubectl label nodes node01 size=Large
   ```
   
   **Step 2:** Add a nodeSelector field to pod configuration
   ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
        env: test
    spec:
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
      nodeSelector:
        side: Large
   ```
   **Limitation:** Complex node selection rule is not possible using nodeSelector.
   
   ##### Node Affinity
   Node affinity, is a property of Pods that attracts them to a set of nodes (either as a preference or a hard requirement).  
   
   Node Affinity Types  
   
   **Available**  
   * requiredDuringSchedulingIgnoredDuringExecution
   * preferredDuringSchedulingIgnoredDuringExecution  
   
   **Planned**  
   * requiredDuringSchedulingRequiredDuringExecution
   
   
   |           | DuringScheduling | DuringExecution |
   |---------- | ---------------- | --------------- | 
   |  Type 1   | Required         | Ignored         |
   |  Type 2   | Preferred        | Ignored         |
   |  Type 3   | Required         | Required        | 
   
   Node Affinity created in a file.
   ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: with-node-affinity
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/e2e-az-name
                operator: In
                values:
                - e2e-az1
                - e2e-az2
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: another-node-label-key
                operator: In
                values:
                - another-node-label-value
      containers:
      - name: with-node-affinity
        image: k8s.gcr.io/pause:2.0
   ```
   ##### Resource Requirements and Limits
   In kubernetes cluster, each node has 3 resource available.  
   1. CPU
   2. Memory
   3. Disk
   
   Every Pod consumes resources available from that node. If a node does not have a available resources for a pod in the 
   cluster, then pod will be in pending state.  
  
   Default Resource Required by a Pod:  
   1. CPU: 0.5 Core
   2. Memory: 256 Mi
   3. Disk
   
   If application or pod needed more resources than default requirement then specify expected resource requirement under containerSpec.
   ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-resource-requirement
    spec:
      containers:
      - name: pod-resource-requirement
        image: k8s.gcr.io/pause:2.0
        ports:
          - containerPort: 8080
        resources:
          requests:
            cpu: 1
            memory: "1Gi"
          limits:
            cpu: 2
            memory: "2Gi"
   ```
   Limits and Requests are set on the each container on the Pod. If a pod tries to consumes more memory than CPU then cluster terminate the pod from cluster.
   
   It is possible to set default limit range of resources using kubernetes object
   ```
   -- set default memory value in container
   apiVersion: v1
   kind: LimitRange
   metadata:
      name: mem-limit-range
   spec:
      limits:
      - default:
          memory: 512Mi
        defaultRequest:
          memory: 256Mi
        type: Container

   -- set default cpu value in container
   apiVersion: v1
   kind: LimitRange
   metadata:
      name: mem-limit-range
   spec:
      limits:
      - default:
          cpu: 1
        defaultRequest:
          memory: 0.5
        type: Container
   
   ```
   
   #### References and Further Study
   * https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
   * https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
   * https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
   * https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
   * https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
   * https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
   
   ### Role of DaemonSets
   DaemonSet ensures one copy of pod always present in every node in the cluster. DaemonSet is almost identical to replicaSet 
   but it only deploy one copy of pod in each node. Whenever a new node added 
   in the cluster a new pod deploy in the new node automatically and when a node remove from cluster then pod is removed 
   automatically.  
   
   Example of DaemonSet:  
   * Monitoring Solution
   * Logs Viewer
   * kube-proxy
   * weave-net
   
   create a deamonSet from a manifest file
   ```bash
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: fluentd-elasticsearch
    spec:
      selector:
        matchLabels:
          name: fluentd-elasticsearch
      template:
        metadata:
          labels:
            name: fluentd-elasticsearch
        spec:
          containers:
          - name: fluentd-elasticsearch
            image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
   ``` 
   #### Command References
   ```
   -- create daemonSet from filename ds.yaml
   $ kubectl create -f ds.yaml

   -- get daemonSet 
   $ kubectl get ds
   ```

   #### References and Further Study
   * https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
   
   
   ### Multiple Schedulers to Run and Configure Pods
   #### Static Pods
   Static Pod is regular pod but created by kubelet server with placing pod definition file in kubelet manifest location.
   Kubelet manifest location can be get using it service name ```kubelet.service```
   
   * Static pod can't be edited like normal pod.
   * Static pod has always it's node name after pod name.
   * Default static path can be changed by changing kubelet config path.
   
   
   #### Multiple Scheduler Configure
   Multiple kube-scheduler can work together with proper configuration. To configure multiple scheduler with different algorithm, following step are necessary 
   * Deploy scheduler binary in proper location.
   * Create new scheduler service like default ```kube-scheduler.service``` and names as any ```my-custom-scheduler.service```
   * Configure options in kube-scheduler named ```--scheduler-name=my-custom-scheduler``` and ```--lock-object-name=my-custom-scheduler```   
   * Add new key name in pod definition file in containerSpec ```schedulerName: my-custom-scheduler```.
   * See event and logs for pod is running and pod is scheduled by proper scheduler.
   
   
   #### References and Further Study
   * https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/
   * https://kubernetes.io/docs/tasks/administer-cluster/configure-multiple-schedulers/
   
  
   ### Scheduler Events
   Problem with scheduler events can be identified in the following ways
   1. At the POD level
   1. At the Event level
   1. At the Log level
   
   #### Command References
   ```
    -- get the scheduler pod name
    $ kubectl get pods -n kube-system

    -- get events for default namespaces
    $ kubectl get events

    -- get events for kube-system namespaces
    $ kubectl get events -n kube-system

    -- watch the events in real time
    $ kubectl get events -w

    -- delete all pods in default namespaces
    $ kubectl delete pod --all

    -- view the log output from scheduler pod
    $ kubectl log <scheduler_pod_name> -n kube-system

   ``` 

   #### References and Further Study
   * https://kubernetes.io/docs/tasks/debug-application-cluster/

   
[Table of Contents](https://github.com/gitmehedi/cloudtuts/tree/develop/kubernetes)  
**Prev Chapter:** [Chapter 4: Networking (11%)](chapter-4-networking-11.md)  
**Next Chapter:** [Chapter 6: Application Lifecycle (8%)](chapter-6-application-lifecycle-8.md)  