# Add & Update a Pool

Sử dụng hướng dẫn này để thêm mới/cập nhật một Pool vào một Application Load Balancer có sẵn.

### 1. Cách thêm mới Pool 

* **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
* **Tại trang chủ Load Balancer, click chọn Load Balancer cần thêm mới Pool.**
* **Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.**
* **Nhấn chọn nút "Thêm mới Pool", một cửa sổ giao diện hiện lên cho phép bạn cấu hình thông tin Pool**
* **Tại cửa sổ thêm mới, cấu hình các thông tin như:**
  * **Tên Pool:** Lưu ý rằng tên Pool không thể thay đổi sau khi khởi tạo
  * **Giao thức HTTP**
  * **Chọn thuật toán cân bằng tải:** Tham khảo thêm các thuật toán cân bằng tải [Pool's algorithm](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/pools-algorithm)
  * **Enable/Bật Stick Session:** Tham khảo thêm tại [Enable sticky session](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/enable-sticky-session)
  * **Enable/Bật TLS Encryption:** Tham khảo thêm tại [Enable TLS encryption](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/enable-tls-encryption)
  * **Cài đặt Health Check:** Tham khảo hướng dẫn cài đặt Health Check giao thức TCP/HTTP tại [Config health check setting](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/config-health-check-setting)
  * **Thêm Pool Member:** Tham khảo hướng dẫn [Attach pool members](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/vlb-load-balancer-new-version/application-load-balancer/pool/pool-members/attach-pool-members)
* **Nhấn nút "Thêm" tại góc dưới bên phải của cửa sổ thêm mới để hoàn tất việc thêm Pool**

### 2. Cách cập nhật thông tin Pool 

* **Truy cập vào trang chủ Load Balancer tại đây:** [**https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb**](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb)
* **Tại trang chủ Load Balancer, click chọn Load Balancer cần cấu hình.**
* **Tại phần thông tin chi tiết Load Balancer, chọn tab Pool.**
* **Tại phần danh sách Pool, rê chuột vào Pool cần chỉnh sửa và nhấn vào biểu tượng Edit.**
* **Một cửa sổ bật lên cho phép chỉnh sửa Pool, các thông tin được phép cập nhật**
  * **Thuật toán cân bằng tải**
  * **Cấu hình health check nâng cao**
* **Nhấn nút "Lưu / Save" tại góc dưới bên phải của cửa sổ chỉnh sửa để hoàn tất việc cập nhập Pool**



\
