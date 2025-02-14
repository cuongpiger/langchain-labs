# 1. VKS là gì?
VKS (VNGCloud Kubernetes Service) là một dịch vụ được quản lý trên VNGCloud giúp bạn đơn giản hóa quá trình triển khai và quản lý các ứng dụng dựa trên container. Kubernetes là một nền tảng mã nguồn mở được phát triển bởi Google, được sử dụng rộng rãi để quản lý và triển khai các ứng dụng container trên môi trường phân tán.
  ![](https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252FDdjIxz6yNWoIeaPXHREV%252Fimage.png%3Falt%3Dmedia%26token%3Db32bd47d-452b-4d22-a9ec-91f37cf8bbd9&width=768&dpr=2&quality=100&sign=336f642&sv=2)

# 2. Những điểm nổi bật của VKS <a href="#whatisvks-nhungdiemnoibatcuavks" id="whatisvks-nhungdiemnoibatcuavks"></a>
Những điểm nổi bật của dịch vụ VKS có thể kể đến gồm:
  * **Quản lý Control Plane hoàn toàn tự động (Fully Managed control plane):** VKS sẽ giải phóng bạn khỏi gánh nặng quản lý Control Plane của Kubernetes, giúp bạn tập trung vào việc phát triển ứng dụng.
  * **Hỗ trợ các phiên bản Kubernetes mới nhất:** VKS luôn cập nhật những phiên bản Kubernetes mới nhất (minor version từ 1.27, 1.28, 1.29) để đảm bảo bạn luôn tận dụng được những tính năng tiên tiến nhất.
  * **Kubernetes Networking:** VKS tích hợp Calico CNI, mang lại tính hiệu quả và bảo mật cao.
  * **Upgrade seamlessly:** VKS hỗ trợ nâng cấp giữa các phiên bản Kubernetes một cách dễ dàng và nhanh chóng, giúp bạn luôn cập nhật những cải tiến mới nhất.
  * **Scaling & Healing Automatically:** VKS tự động mở rộng Node group khi cần thiết và tự động sửa lỗi khi node gặp vấn đề, giúp bạn tiết kiệm thời gian và công sức quản lý.
  * **Giảm chi phí và nâng cao độ tin cậy:** VKS triển khai Control Plane của Kubernetes ở chế độ sẵn sàng cao và hoàn toàn miễn phí, giúp bạn tiết kiệm chi phí và nâng cao độ tin cậy cho hệ thống.
  * **Tích hợp Blockstore Native (Container Storage Interface - CSI):** VKS cho phép bạn quản lý Blockstore thông qua YAML của Kubernetes, cung cấp lưu trữ bền vững cho container và hỗ trợ các tính năng quan trọng như thay đổi kích thước, thay đổi IOPS và snapshot volume.
  * **Tích hợp Load Balancer (Network Load Balancer, Application Load Balancer) thông qua các driver được tích hợp sẵn như VNGCloud Controller Mananger, VNGCloud Ingress Controller:** VKS cung cấp khả năng quản lý NLB/ALB thông qua YAML của Kubernetes, giúp bạn dễ dàng expose Service trong Kubernetes ra bên ngoài.
  * **Nâng cao bảo mật:** VKS cho phép bạn tạo Private Node Group với chỉ Private IP và kiểm soát quyền truy cập vào cluster thông qua tính năng Whitelist IP, đảm bảo an toàn cho hệ thống của bạn.

**Ngoài ra, VKS còn có các ưu điểm sau:**
  * Dễ sử dụng: VKS cung cấp giao diện đơn giản và dễ sử dụng.
  * Chi phí hợp lý: VKS cung cấp mức giá cạnh tranh cho các dịch vụ của mình.

# 3. VKS cung cấp dịch vụ trên các khu vực (region) nào?

Hiện tại, trên VKS, chúng tôi đang cung cấp cho bạn 2 cơ sở hạ tầng riêng biệt được đặt tại Hà Nội và Hồ Chí Minh. Bạn có thể lựa chọn sử dụng VKS trên mỗi region tùy thuộc vào vị trí và nhu cầu thực tế của bạn. Đối với 2 farm HCM03, HAN01, các thông số cụ thể cho mỗi region được chúng tôi cung cấp như sau:
  - Khu vực Hồ Chí Minh (HCM03): [https://vks.console.vngcloud.vn](https://vks.console.vngcloud.vn)
  - Khu vực Hà Nội (HAN01): [https://vks-han-1.console.vngcloud.vn](https://vks-han-1.console.vngcloud.vn)

# 4. Tài liệu tham khảo:
Bạn có thể tìm hiểu thêm về VKS tại đường dẫn [https://docs.vngcloud.vn/vng-cloud-document/vn/vks/vks-la-gi](https://docs.vngcloud.vn/vng-cloud-document/vn/vks/vks-la-gi)
