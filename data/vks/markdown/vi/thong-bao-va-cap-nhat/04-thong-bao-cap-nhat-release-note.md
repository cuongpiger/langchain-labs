# 4. Thông báo cập nhật (release notes)

**Ngày 05 tháng 12 năm 2024**
- VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng mới cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:
  - Tính năng mới:
    - Force-Upgrade, Auto-Upgrade: Tự động nâng cấp phiên bản Kubernetes cho cluster/ node group theo lịch trình hoặc khi phiên bản hiện tại sắp hết hạn.

**Ngày 23 tháng 10 năm 2024**
- VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều cải tiến cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:
- Cải tiến:
  - Hỗ trợ POC/ Stop POC cho Cluster: Người dùng giờ đây có thể thực hiện POC/ Stop POC cho các tài nguyên trên VKS như Server, Volume, Load Balancer, Endpoint. Tính năng này mang đến sự linh hoạt cao cho người dùng khi muốn trải nghiệm với VKS. Chi tiết tham khảo thêm tại đây.
  - Nâng cấp Plugin VNGCloud BlockStorage CSI Driver: Các lỗi đã được phát hiện trong các phiên bản trước đã được khắc phục, giúp hệ thống hoạt động mượt mà và tin cậy hơn.
  - Tự do lựa chọn/ chỉnh sửa cấu hình có/ không sử dụng plugin VNGCloud LoadBalancer Controller, Plugin VNGCloud Ingress Controller trên cụm VKS hiện có: Khả năng tùy chỉnh cấu hình plugin cho phép người dùng tối ưu hóa cụm VKS theo nhu cầu cụ thể của mình. Điều này giúp tăng tính linh hoạt và đáp ứng các yêu cầu đặc biệt của từng ứng dụng.
  - Ngoài ra, trong bản cập nhật này, chúng tôi cũng đã khắc phục một số lỗi nhỏ để mang đến trải nghiệm người dùng tốt hơn.

**Ngày 03 tháng 10 năm 2024**
- VKS (VNGCloud Kubernetes Service) vừa ra mắt bản cập nhật mới nhất, mang đến nhiều tính năng và cải tiến cho người dùng. Dưới đây là những điểm nổi bật của bản cập nhật:
- Triển khai Region mới:
  - Bên cạnh Region HCM03, VKS hiện đã hỗ trợ thêm Region HAN01. Việc bổ sung này giúp khách hàng có thêm lựa chọn trong việc triển khai ứng dụng, đặc biệt hữu ích cho các doanh nghiệp có yêu cầu về vị trí đặt dữ liệu.
- Tính năng mới:
  - Network Type: Cilium Overlay, Cilium VPC Native Routing: Ngoài Calico Overlay, bản phát hành lần này chúng tôi đã bổ sung hai loại mạng mới: Cilium Overlay và Cilium VPC Native Routing. Cilium Overlay cho phép bạn xây dựng mạng overlay linh hoạt, trong khi Cilium VPC Native Routing tích hợp chặt chẽ với VPC của VNG Cloud, giúp tối ưu hiệu suất và bảo mật cho ứng dụng của bạn. Chi tiết tham khảo thêm tại đây.
- Cải tiến:
  - Multiple Subnet cho Cluster trên VKS: VKS giờ đây hỗ trợ sử dụng nhiều subnet cho một cluster. Điều này cho phép bạn cấu hình từng node group trong cluster nằm ở các subnet khác nhau trong cùng một VPC, tối ưu hóa việc phân bổ tài nguyên và quản lý mạng.
  - Chỉnh sửa Labels/Taints trên cụm VKS hiện có: Với khả năng chỉnh sửa trực tiếp Labels/Taints trên cụm VKS đã triển khai, bạn có thể điều khiển việc lên lịch Pod, áp dụng các chính sách khác nhau cho các Node Group, và tùy chỉnh quy tắc lựa chọn node cho các ứng dụng. Điều này giúp quản lý và phân loại tài nguyên hiệu quả hơn.
  - Enable/Disable lựa chọn sử dụng Private Service Endpoint: Trước đây, khi tạo private cluster trên VKS, việc tạo private service endpoint là bắt buộc. Giờ đây, bạn có thể dễ dàng bật/tắt tính năng này, cho phép các dịch vụ trong cụm VKS giao tiếp qua địa chỉ IP nội bộ, tăng cường bảo mật và giảm thiểu rủi ro tấn công từ bên ngoài.
  - Enable/Disable lựa chọn mã hóa Volume: Tính năng mã hóa Volume cho phép bạn bảo vệ dữ liệu nhạy cảm được lưu trữ trong các Persistent Volume của cụm VKS. Việc này đảm bảo an toàn dữ liệu và tuân thủ các quy định về bảo vệ thông tin. Giờ đây, bạn có thể bật/tắt tính năng mã hóa cho từng Volume theo nhu cầu.

**Ngày 28 tháng 8 năm 2024**
- VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều tính năng mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:
- Tính năng mới:
  - Private Cluster: Trước đây, các public cluster trên VKS đang sử dụng địa chỉ Public IP để giao tiếp giữa nodes và control plane. Để nâng cao bảo mật cho cluster của bạn, chúng tôi đã cho ra mắt mô hình private cluster. Tính năng Private Cluster giúp cho cụm K8S của bạn được bảo mật nhất có thể, mọi kết nối hoàn toàn là private từ kết nối giữa nodes tới control plane, kết nối từ client tới control plane, hay kết nối từ nodes tới các sản phẩm dịch vụ khác trong VNG Cloud như: vStorage, vCR, vMonitor, VNGCloud APIs,...Private Cluster là lựa chọn lý tưởng cho các dịch vụ yêu cầu kiểm soát truy cập chặt chẽ, đảm bảo tuân thủ các quy định về bảo mật và quyền riêng tư dữ liệu.

**Ngày 26 tháng 8 năm 2024**
- VKS (VNGCloud Kubernetes Service) giới thiệu bản cập nhật mới nhất cho VKS đã có sẵn, mang đến nhiều cải tiến mới cho người dùng. Dưới đây là chi tiết về bản cập nhật:
- Cải tiến:
  - Kubernetes Version: VKS đã bổ sung các image mới nhằm tối ưu hóa size, feature, network,...so với các image cũ. Việc xây dựng các image này cũng nhằm phục vụ cho cả hai loại cluster là Public và Private mà VKS sắp ra mắt. Cụ thể, trong bản phát hành này, chúng tôi đã bổ sung thêm các image sau:
    - Ubuntu-22.kube_v1.27.12-vks.1724605200
    - Ubuntu-22.kube_v1.28.8-vks.1724605200
    - Ubuntu-22.kube_v1.29.1-vks.1724605200
  - Lưu ý: Để khởi tạo một Private Cluster, bạn cần chọn sử dụng một trong 3 image mới này. Đối với Public Cluster, bạn có thể chọn sử dụng bất kỳ image cũ hoặc mới tùy theo nhu cầu của bạn.