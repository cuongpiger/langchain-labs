# Bước 3: Sử dụng Kubeclt để access vào Container đã khởi tạo

Sau khi khởi tạo thành công Kubernetes Cluster, bạn cần sử dụng Kubectl để access vào Container đã tạo theo các bước sau đây:

### **Bước 1. Download file Config Container trên VNG CLOUD portal**  

1. Truy cập vào bảng điều khiển Kubernetes Cluster tại: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster)
2. Sau đó chỉ định Cluster và chọn **Action**
3. Chọn **Lấy file config**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(468).png?raw=true)

***

### **Bước 2. Copy file Configure vào file configure của Kubectl trên PC/Laptop hệ điều hành MacOS** 

1. Đầu tiên, bạn cần mở Terminal trên máy tính của bạn.
2.  Chuyển đến thư mục gốc của tài khoản người dùng:\


    | `cd ~/` |
    | ------- |
3.  Tạo một thư mục có tên .kube trong thư mục gốc của tài khoản người dùng. Thư mục này sẽ chứa tệp cấu hình của Kubernetes

    | `mkdir .kube` |
    | ------------- |
4.  Chuyển đến thư mục .kube mà bạn vừa tạo

    | `cd .kube` |
    | ---------- |
5.  Mở tệp với tên config bằng trình soạn thảo văn bản Vim. Tệp config chính là tệp cấu hình của kubectl để thực hiện các lệnh truy vấn và quản lý Kubernetes.\


    | `vim config` |
    | ------------ |
6. Copy File Config trên Portal download về vào file config trên MAC OS: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(467).png?raw=true)

***

### **Bước 2. Copy file Configure vào file configure của Kubectl trên PC/Laptop hệ điều hành Window** 

1. cd \~/
2. mkdir .kube
3. cp \~/Downloads/config.txt \~/.kube/config
4. cd. kube

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(470).png?raw=true)

***

### **Bước 3. Kiểm tra kết nối từ Kubectl lên VNG CLOUD Containter:** 

1.  Sau đó dùng lệnh sau để liệt kê tất cả các node trong cluster Kubernetes của bạn:\


    | `kubectl get nodes` |
    | ------------------- |
2. Giao diện sẽ trả về kết quả như sau:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(471).png?raw=true)

Như vậy đã hoàn thành việc khởi tạo Containers và kết nối lên Container đó ngay tại PC hoặc Laptop của mình.
