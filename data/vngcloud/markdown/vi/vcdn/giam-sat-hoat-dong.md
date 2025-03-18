# Giám sát hoạt động

## **Tổng quan**

Hệ thống vCDN hỗ trợ khách hàng giám sát và theo dõi toàn bộ hoạt động của dịch vụ CDN qua **Portal** hoặc **API**, cung cấp thông tin chi tiết, trực quan về hiệu suất và trạng thái dịch vụ.

Các chỉ số sẽ được cung cấp trực quan thành các Dashboard và biểu đồ với: 

* Dữ liệu được cập nhật với tần suất **từng phút**.
* Độ trễ tối đa là **5 phút** (cận realtime), giúp khách hàng nắm bắt kịp thời các thay đổi trong hệ thống.

## Chi tiết

Các loại biểu đồ/ báo cáo chúng tôi cung cấp cho bạn bao gồm: 

* **Traffic Consuming:** tổng lượng băng thông được sử dụng trên hệ thống CDN trong một tháng.
* **Origin Request/s**: số lượng yêu cầu (requests) gửi từ CDN tới Origin theo từng giây.
* **Origin Traffic Consuming/s (GB/s)**: lưu lượng tiêu thụ từ Origin, đo bằng GB mỗi giây.
* **Unique IPs:** Hiển thị số lượng IP duy nhất gửi yêu cầu tới hệ thống CDN.
* **Origin Speed/s:** tốc độ tải và phục vụ từ Origin theo thời gian thực.
* **Average User Speed:** Tốc độ tải trung bình từ Origin tới CDN trong một khoảng thời gian.
* **Hit Cache Ratio:** Tỷ lệ yêu cầu được phục vụ từ bộ nhớ đệm (cache) của CDN thay vì Origin.
* **Request Content Type:** Phân loại các loại nội dung yêu cầu (ví dụ: HTML, CSS, JS, hình ảnh, video).
* **CDN HTTP Codes, Origin HTTP Codes:** Theo dõi trạng thái kết nối giữa CDN và Origin (thành công, lỗi 4xx, lỗi 5xx...).
* **Quản lý và theo dõi tín hiệu được đẩy đến hệ thống Live Entry point**

## **Các bước thực hiện**

**Bước 1:** Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)

**Bước 2:** Chọn mục **Dashboard.** Tại đây, bạn có thể thấy các biểu đồ, báo cáo được chúng tôi đề cập bên trên. Ví dụ: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(856).png?raw=true)

* **Traffic Consuming:**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(846)%20(1).png?raw=true)

* **Origin Request/s**: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(847)%20(1).png?raw=true)

* **Origin Traffic Consuming/s (GB/s)**:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(848).png?raw=true)

* **Unique IPs:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(849).png?raw=true)

* **Origin Speed/s:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(850).png?raw=true)

* **Average User Speed:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(851).png?raw=true)

* **Hit Cache Ratio:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(852).png?raw=true)

* **Request Content Type:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(853).png?raw=true)

* **CDN HTTP Codes, Origin HTTP Codes:** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(854).png?raw=true)

* **Quản lý và theo dõi tín hiệu được đẩy đến hệ thống Live Entry point:**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(855).png?raw=true)
