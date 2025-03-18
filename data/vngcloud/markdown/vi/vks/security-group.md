# Security Group

Security Group đóng vai trò như một firewall giúp bạn kiểm soát lưu lượng truy cập ra vào máy chủ (VM). Trên hệ thống VKS, để đảm bảo cluster hoạt động an toàn và hiệu quả, các Security Group mặc định được thiết lập để cho phép các truy cập cần thiết cho hoạt động nội bộ của cluster. Việc tự động tạo Security Group giúp đơn giản hóa quá trình triển khai cluster và đảm bảo rằng cluster được bảo vệ ngay từ đầu. Cụ thể, khi bạn thực hiện khởi tạo một Cluser, chúng tôi sẽ tự động khởi tạo một vài Security Group với các thông số như sau: 

### Security group mặc định được tạo tự động cho tất cả Cluster

Mỗi Cluster được tạo ra trong hệ thống VKS, chúng tôi sẽ tự động tạo một Security Group. Security group này sẽ bao gồm:

* Inbound:

| Protocol | Ether type | Port range | Source | Ý nghĩa |
| --- | --- | --- | --- | --- |
| TCP | IPv4 | 30000-32767 | CIDR của VPC mà bạn sử dụng cho Cluster. | Security group rule sử dụng cho TCP Node Port Services |
| UDP | IPv4 | 30000-32767 | CIDR của VPC mà bạn sử dụng cho Cluster. | Security group rule sử dụng cho UDP Node Port Services |
| TCP | IPv4 | 10250 | External IP của Load Balancer sử dụng cho Cluster. | Security group rule sử dụng cho Kubelet API control-plane |
| TCP | IPv4 | 10250 | CIDR của VPC mà bạn sử dụng cho Cluster. | Security group rule sử dụng cho Kubelet API control-plane |
| TCP | IPv4 | 179 | CIDR của VPC mà bạn sử dụng cho Cluster. | Security group rule sử dụng cho Kubelet API control-plane |
| 4 | IPv4 | 1-65535 | CIDR của VPC mà bạn sử dụng cho Cluster. | Security group rule sử dụng cho Calico IP-in-IP |
| TCP | IPv4 | 5473 | CIDR của VPC mà bạn sử dụng cho Cluster. | Security group rule sử dụng cho Calico Typha |

* Outbound

| Protocol | Ether type | Port range | Destination | Ý nghĩa |
| --- | --- | --- | --- | --- |
| ANY | IPv4 | 0-65535 | 0.0.0.0/0 | Rule mặc định của tất cả Security group |
| ANY | IPv6 | 0-65535 | ::/0 | Rule mặc định của tất cả Security group |

### Security group được tạo tự động bởi VNGCLOUD LoadBalancer Controller 

Khi bạn sử dụng VNGCloud LoadBalancer Controller để tích hợp Network Load Balancer với Cluster trên hệ thống VKS, chúng tôi sẽ tự động tạo một Security Group. Security group này sẽ bao gồm:

* Inbound:

| Protocol | Ether type | Port range | Source |
| --- | --- | --- | --- |
| TCP, UDP hoặc ICMP | IPv4 | Port của Service | Subnet Mask của Subnet mà bạn sử dụng cho Cluster. |

* Outbound:

| Protocol | Ether type | Port range | Destination | Ý nghĩa |
| --- | --- | --- | --- | --- |
| ANY | IPv4 | 0-65535 | 0.0.0.0/0 | Rule mặc định của tất cả Security group |
| ANY | IPv6 | 0-65535 | ::/0 | Rule mặc định của tất cả Security group |

### Security group được tạo tự động bởi VNGCLOUD Ingress Controller

Khi bạn sử dụng VNGCloud Ingress Controller để tích hợp Application Load Balancer với Cluster trên hệ thống VKS, chúng tôi sẽ tự động tạo một Security Group. Security group này sẽ bao gồm:

* Inbound:

| Protocol | Ether type | Port range | Source |
| --- | --- | --- | --- |
| TCP | IPv4 | Port của Service | Subnet Mask của Subnet mà bạn sử dụng cho Cluster. |

* Outbound:

| Protocol | Ether type | Port range | Destination | Ý nghĩa |
| --- | --- | --- | --- | --- |
| ANY | IPv4 | 0-65535 | 0.0.0.0/0 | Rule mặc định của tất cả Security group |
| ANY | IPv6 | 0-65535 | ::/0 | Rule mặc định của tất cả Security group |

> **Chú ý:**
>
> * Các Security Group mặc định được thiết lập để đáp ứng các nhu cầu bảo mật cơ bản của cluster. Nếu bạn sửa hoặc xóa các Security Group được tạo sẵn cho cluster, có thể dẫn đến các vấn đề về kết nối và truy cập giữa các node trong cluster hoặc cluster có thể không hoạt động chính xác hoặc thậm chí không thể khởi động được. Để đảm bảo tính ổn định và bảo mật của cluster, hệ thống sẽ tự động reset các Security Group về cài đặt mặc định sau mỗi khoảng thời gian cố định.
