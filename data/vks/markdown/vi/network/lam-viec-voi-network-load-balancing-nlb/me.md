# 2. Tích hợp Network Load Balancer (NLB) trên VKS

## 2.1. Network Load Balancer (NLB) là gì?

* **Network Load Balancer** (tên viết tắt là **NLB**) là một bộ cân bằng tải được cung cấp bởi VNGCloud giúp phân phối lưu lượng truy cập mạng đến nhiều máy chủ back-end (backend servers) trong một nhóm máy tính (instance group). NLB hoạt động ở layer 4 của mô hình OSI, giúp cân bằng tải dựa trên địa chỉ IP và cổng TCP/UDP. Để biết thêm thông tin chi tiết về NLB, vui lòng tham khảo tại [https://docs.vngcloud.vn/vng-cloud-document/vn/vks/network/lam-viec-voi-network-load-balancing-nlb](https://docs.vngcloud.vn/vng-cloud-document/vn/vks/network/lam-viec-voi-network-load-balancing-nlb)

## 2.2. Mô hình triển khai
![](https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252FVYBtJjEoUNgDi1f5J9vL%252Fimage.png%3Falt%3Dmedia%26token%3D554a2d62-320e-48d1-a884-3c7cce589071&width=768&dpr=2&quality=100&sign=4336a109&sv=2)
* **VNGCloud LoadBalancer Controller**: là một bộ điều khiển (hay còn gọi là **controller**) chạy trên các cụm Kubernetes được triển khai trên VNGCloud. Controller này chịu trách nhiệm:
  * **Quản lý các Network Load Balancer (NLB)** cho các Service của Kubernetes có thuộc tính `serviceType` là `LoadBalancer`.
  * **Điều phối lưu lượng mạng** đến các `pod` trên worker node của bạn.

## 2.3. Cài đặt VNGCloud LoadBalancer Controller để sử dụng NLB
Để sử dụng NLB trên VKS, bạn cần cài đặt plugin **VNGCloud LoadBalancer Controller**. Plugin này đảm nhận vai trò quản lý và cấu hình NLB cho các tài nguyên `Service` có thuộc tính `serviceType` là `LoadBalancer`. Mặc định, một cụm Kubernetes trên VKS đã được **cài đặt sẵn** plugin **VNGCloud LoadBalancer Controller** này. Việc cài đặt sẵn này giúp bạn có thể sử dụng NLB mà không cần phải thực hiện thêm bất kỳ thao tác cấu hình nào khác và đảm bảo luôn được cập nhật phiên bản mới nhất. Tuy nhiên người dùng hoàn toàn có thể bật/tắt plugin này thông qua thiết lập **Enable vLB Native Integration Driver** trên **VKS Console**.

Ngoài ra, người dùng hoàn toàn có thể tự cài đặt plugin **VNGCloud LoadBalancer Controller** bằng cách thực hiện các bước sau:
- **Bước 1**: Tạo một Kubernetes cluster trên VKS, hoặc sử dụng một cluster đã có. Tải file `kubeconfig` của cluster về thiết bị của bạn. Ngoài ra, bạn nên kiểm tra file `kubeconfig` này đã có thể kết nối đến cluster thành công hay chưa thông qua `kubectl` CLI.
- **Bước 2**: Khởi tạo hoặc sử dụng một **IAM Service Account** đã có trên **IAM Console** và thiết lập hai policy `vLBFullAccess` và `vServerFullAccess` cho **Service Account** này. Bạn có thể tham khảo cách tạo **Service Account** tại [https://hcm-3.console.vngcloud.vn/iam/service-accounts](https://hcm-3.console.vngcloud.vn/iam/service-accounts). Sau đó, bạn cần lưu lại **Client ID** và **Client Secret** của **Service Account** này.
- **Bước 3**: Bạn cần cài đặt **Helm 3.0** trên thiết bị của bạn, bạn có thể tham khảo cách cài đặt Helm tại [https://helm.sh/docs/intro/install](https://helm.sh/docs/intro/install). Sau khi `helm` CLI đã được cài đặt thành công, bạn đã có thể dùng `helm` CLI để cài đặt plugin, lưu ý rằng bạn cần thay thế các giá trị **Client ID** và **Client Secret** của **Service Account** vào lệnh dưới đây:
  ```bash
  helm install vngcloud-load-balancer-controller oci://vcr.vngcloud.vn/81-vks-public/vks-helm-charts/vngcloud-load-balancer-controller --namespace kube-system --set mysecret.global.clientID=__PUT_YOUR_CLIENT_ID__ --set mysecret.global.clientSecret=__PUT_YOUR_CLIENT_SECRET__
  ```
- **Bước 4**: Sau khi Helm hoàn tất việc cài đặt **VNGCloud LoadBalancer Controller**, bạn có thể kiểm tra xem plugin đã hoạt động hay chưa bằng lệnh:
  ```bash
  kubectl -n kube-system get pod -l app.kubernetes.io/name=vngcloud-load-balancer-controller
  ```
  Dưới đây là ví dụ kết quả trả về khi plugin đã hoạt động:
  ```bash
  NAME                                                              READY   STATUS    RESTARTS   AGE
  vngcloud-load-balancer-controller-1736217866-manager-77599vrxpz   1/1     Running   0          4h24m
  ```
## 2.4. Sử dụng Network Load Balancer (NLB) trên VKS
Sau khi đã cài đặt plugin **VNGCloud LoadBalancer Controller** thành công, bạn đã có thể sử dụng NLB thông quà tài nguyên `Service` trên Kubernetes. Dưới đây là một vài tình huống sử dụng NLB trên VKS:

**Ví dụ 1**: Công khai một dịch vụ Nginx trên cổng 80 với NLB đến Internet:
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nginx-app
  spec:
    selector:
      matchLabels:
        app: nginx
    replicas: 1
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx:1.19.1
          ports:
          - containerPort: 80
  ---
  apiVersion: v1
  kind: Service
  metadata:
    name: nginx-service
  spec:
    selector:
      app: nginx
    type: LoadBalancer 
    ports:
      - protocol: TCP
        port: 80
        targetPort: 80
  ```

**Ví dụ 2**: Triển khai dịch vụ Apache HTTP và chỉ cho phép truy cập nội bộ qua port 8080:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: internal-http-apache2-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: apache2
  template:
    metadata:
      labels:
        app: apache2
    spec:
      containers:
        - name: apache2
          image: httpd
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: internal-http-apache2-service
  annotations:
    vks.vngcloud.vn/scheme: "internal"              # Thiệt lập annotation để tạo NLB nội bộ
spec:
  selector:
    app: apache2
  type: LoadBalancer
  ports:
    - name: http
      protocol: TCP
      port: 8080
      targetPort: 80
```

**Ví dụ 3**: Triển khai một dịch vụ sử dụng protocol UDP:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: udp-server-deployment
spec:
  selector:
    matchLabels:
      name: udp-server
  replicas: 5
  template:
    metadata:
      labels:
        name: udp-server
    spec:
      containers:
      - name: udp-server
        image: vcr.vngcloud.vn/udp-server
        imagePullPolicy: Always
        ports:
        - containerPort: 10001
          protocol: UDP
---
apiVersion: v1
kind: Service
metadata:
  name: udp-server-service
  annotations:
    vks.vngcloud.vn/pool-algorithm: "source-ip"   # Thiết lập annotation để chọn thuật toán cân bằng tải
  labels:
    app: udp-server
spec:
  type: LoadBalancer
  sessionAffinity: ClientIP
  ports:
  - port: 10001
    protocol: UDP
  selector:
    name: udp-server
```

**Ví dụ 4**: Sử dụng lại một NLB đã có trên hệ thống vLB. Để sử dụng lại một NLB đã có, bạn cần nhập thông tin **Load Balancer ID** vào annotation `vks.vngcloud.vn/load-balancer-id` của Service:
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: external-http-nginx-deployment
  spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
          ports:
          - containerPort: 80
  ---
  kind: Service
  apiVersion: v1
  metadata:
    name: external-http-nginx-service
    annotations:
      vks.vngcloud.vn/load-balancer-id: "__PUT_YOUR_LOAD_BALANCER_ID__"
  spec:
    selector:
      app: nginx
    type: LoadBalancer
    ports:
    - name: http
      port: 80
      targetPort: 80
  ```

Ngoài ra, bạn cũng có thể tìm hiểu thêm về các annotation khác mà bạn có thể sử dụng để tùy chỉnh NLB phù hợp với nhu cầu của bạn tại đường dẫn [https://docs.vngcloud.vn/vng-cloud-document/vn/vks/network/lam-viec-voi-network-load-balancing-nlb/cau-hinh-cho-mot-network-load-balancer](https://docs.vngcloud.vn/vng-cloud-document/vn/vks/network/lam-viec-voi-network-load-balancing-nlb/cau-hinh-cho-mot-network-load-balancer).

## 2.5. Cấu hình cho một Network Load Balancer
Bạn có thể tùy chỉnh hoặc cấu hình NLB phù hợp với nhu cầu của bạn thông qua các annotation dưới đây:
  - `vks.vngcloud.vn/load-balancer-id`:
    - Bắt buộc phải có trong spec của tài nguyên `Service`: Không bắt buộc
    - Ý nghĩa: Dùng để sử dụng lại một NLB sẵn có trên hệ thống vLB. Nếu annotation này không được thiết lập, một NLB mới sẽ được tạo tự động.
  - `vks.vngcloud.vn/load-balancer-name`:
    - Bắt buộc phải có trong spec của tài nguyên `Service`: Không bắt buộc
    - Ý nghĩa: Giá trị của annotation này sẽ dùng làm tên cho NLB của bạn. Nếu annotation này không được thiết lập, **VNGCloud LoadBalancer Controller** sẽ tự động tạo một tên cho NLB của bạn. Annotation này sẽ không có tác dụng nếu một trong các annotation sau được thiết lập: `vks.vngcloud.vn/load-balancer-id`.
  - `vks.vngcloud.vn/package-id`:
    - Bắt buộc phải có trong spec của tài nguyên `Service`: Không bắt buộc
    - Ý nghĩa: Dùng để thiết lập package của NLB. Nếu không được thiết lập, mặc định sẽ sử dụng cấu hình **NLB Small**. Ngoài ra, bạn cũng có thể dùng annotation này để cấu hình lại package của NLB hiện tại.

## 2.6. Những hạn chế của NLB trên VKS
* Một NLB có thể được sử dụng chung cho nhiều cluster nhưng phải đảm bảo các cluster này có chung một **VPC**.
* Một NLB sẽ bị giới hạn về số lượng pools, listeners, members. Chi tiết tại [https://docs.vngcloud.vn/pages/viewpage.action?pageId=59802094](https://docs.vngcloud.vn/pages/viewpage.action?pageId=59802094).

## 2.7. Tài liệu tham khảo
- Bạn có thể tham khảo tại liệu trên website của VNGCloud tại [https://docs.vngcloud.vn/vng-cloud-document/vn/vks/network/lam-viec-voi-network-load-balancing-nlb](https://docs.vngcloud.vn/vng-cloud-document/vn/vks/network/lam-viec-voi-network-load-balancing-nlb).