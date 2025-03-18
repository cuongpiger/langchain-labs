# Origin

## Tổng quan

**Origin** trong CDN chính là máy chủ gốc chứa toàn bộ dữ liệu gốc của website. Đây là nơi lưu trữ bản gốc của các file như hình ảnh, video, HTML, CSS, JavaScript,... Mọi thay đổi trên website đều bắt nguồn từ Origin trước khi được phân phối đến các máy chủ (Edge server) của CDN.

## **Chi tiết**

Hiện tại, vCDN đang hỗ trợ 3 loại Origin: **HTTP Origin, S3 Origin và Host Origin**. Cụ thể, vui lòng tham khảo bảng bên dưới.

| Loại Origin | Mô tả | Ví dụ | Loại dịch vụ hỗ trợ |
| --- | --- | --- | --- |
| **HTTP Origin** | Lấy nội dung từ một máy chủ web hoặc ứng dụng thông qua giao thức HTTP/HTTPS. | Một website lưu trữ tại  `https://example.com` . | - Web Accelerator <br> - Object Download <br> - Video On Demand |
| **S3 Origin** | Lấy nội dung trực tiếp từ các dịch vụ lưu trữ đối tượng S3 - compatible. | Một bucket S3 có URL như  `https://bucket-name.s3.amazonaws.com` . | - Object Download <br> - Video On Demand |
| **Host Origin** | Dữ liệu được cung cấp từ một server hoặc IP cụ thể do người dùng chỉ định. | Server tại địa chỉ IP  `192.168.1.1`  hoặc domain  `cdn-origin.example.com` . | - Object Download <br> - Video On Demand |
