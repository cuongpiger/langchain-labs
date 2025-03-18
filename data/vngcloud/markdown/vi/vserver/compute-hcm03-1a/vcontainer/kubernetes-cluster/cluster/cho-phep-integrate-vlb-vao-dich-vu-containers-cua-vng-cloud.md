# Cho phép integrate vLB vào dịch vụ Containers của VNG CLOUD

**Nhu cầu:**  Khách hàng có nhu cầu triển khai 2 website: [**httpd.app.com**](http://httpd.app.com/) và [**nginx.app.com**](http://nginx.app.com/) theo kiến trúc microservice trên hạ tầng VNG Cloud.

**Giải pháp:**  Sử dụng dịch vụ vLB(Load Balancer) kết hợp với dịch vụ vContainer trên VNG Cloud.

### **Kiến trúc giải pháp:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(473).png?raw=true)

***

### **Triển khai:** 

#### **1. Khởi tạo vLB và vContainer** 

1.1 Tạo Network LoadBalancer(Layer 4)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(474).png?raw=true)

_Note: Như ở trên, chúng ta sẽ tạo 1 Listener trên Port 80. Nếu muốn sử dụng TLS cho website, có thể tạo thêm Listener trên Port 443 và cấu hình TLS ở LoadBalancer Controller. Bài này sẽ chỉ triển khai với Listener Port 80._

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(476).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(477).png?raw=true)

1.2 Nhấn **Create Load Balancer** để tạo vLB

1.3 Sau đó truy cập vào bảng điều khiển **tạo K8S** tại đường link: [https://hcm-3.console.vngcloud.vn/vserver/container/cluster](https://hcm-3.console.vngcloud.vn/vserver/container/cluster): 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(478).png?raw=true)

_Note: Khi tạo vContainer, chúng ta có thể chọn Enable LoadBalancer Controller để tạo cluster với LoadBalancer Controller đã được triển khai sẵn. Để sử dụng LoadBalancer Controller với những tính năng phù hợp theo nhu cầu của ứng dụng, trong bài viết này sẽ không chọn Enable LoadBalancer Controller mà sẽ tự triển khai Nginx LoadBalancer Controller, vì thế bạn cần tắt Ingress Control khi khởi tạo K8S._

1.4 Kiểm tra việc khởi tạo cluster và tải config file để access cluster:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(480).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(481).png?raw=true)

#### 2. Triển khai Nginx LoadBalancer Controller 

2.1 Truy cập [https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters](https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(483).png?raw=true)

2.2 Copy và chạy command trên để triển khai Nginx LoadBalancer Controller:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(485).png?raw=true)

2.3 Kiểm tra:\
→ Như vậy chúng ta đã triển khai thành công Nginx LoadBalancer Controller.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(486).png?raw=true)

2.4 Service ingress-nginx-controller được khởi tạo với _Type: NodePort_ và lắng nghe trên Port: 30398, 31873 của các Minion Node.

#### 3. Attach vLB với vContainer 

_Note: Mặc định vLB không thể kết nối tới vContainer Cluster dù nằm trong cùng VPC/Subnet. Do đó cần tạo mới một Security Group và attach cho Minion Node._

3.1 Tạo Security Group: Do chỉ có 1 Listener Port 80 trên vLB do đó chỉ cần 1 Inbound rule. Trong trường hợp có Listener Port 443, vui lòng tạo thêm Inbound rule.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(487).png?raw=true)

3.2 Update Security Group cho Minion Node:\


![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(488).png?raw=true)

3.3 Điền 30398. Khi đó Listener sẽ forward traffic tới Backend Pool với port 30398.\
vLB sẽ định kỳ health check các Pool Member thông qua Monitor Port, traffic sẽ không được gửi tới những member không health check thành công.:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(489).png?raw=true)

3.4 Nhấn **Lưu** để hoàn tất attach vLB với vContainer

#### 4. Triển khai ứng dụng 

4.1 Chuẩn bị YAML file: service.yaml, deployment.yaml và app-ingress.yaml

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(491).png?raw=true)

4.2 Triển khai:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(492).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(494).png?raw=true)

4.3 Kiểm tra\
Review the vLB status:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(495).png?raw=true)

4.4 Edit file host trên laptop cá nhân để kiểm tra: _**C:\Windows\System32\drivers\etc\hosts:**_

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(496).png?raw=true)

4.5 Mở trình duyệt web và kiểm tra:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(497).png?raw=true)
