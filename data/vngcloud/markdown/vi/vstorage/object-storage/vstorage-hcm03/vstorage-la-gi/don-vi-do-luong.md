# Đơn vị đo lường

Các đơn vị đo lường các tài nguyên trên hệ thống vStorage được chúng tôi mô tả ở bảng bên dưới:

| Tài nguyên | Định nghĩa | Đơn vị (Unit) | Tỉ lệ quy đổi | Chi tiết quy đổi |
| --- | --- | --- | --- | --- |
| Tài nguyên | Định nghĩa | Đơn vị (Unit) | Tỉ lệ quy đổi | Chi tiết quy đổi |
| Quota | Quota là một định mức dung lượng lưu trữ tối đa được thiết lập tại thời điểm khởi tạo Project. Mỗi gói lưu trữ , chúng tôi cung cấp một mức dung lượng tối thiểu và tối đa bạn có thể chọn lựa để thiết lập dựa trên nhu cầu thực tế. Việc thay đổi Quota diễn ra hoàn toàn trong suốt và không ảnh hưởng dịch vụ đang kết nối và lưu trữ trên Project bạn nâng cấp. | byte | 1024 | - 1 KB (Kilobyte) = 1024 byte <br> - 1 MB (Megabyte) = 1024^2 byte <br> - 1 GB (Gigabyte) = 1024^3 byte <br> - 1 TB (Terabyte) = 1024^4 byte <br> - 1 PB (Petabyte) = 1024^5 byte <br> - 1 EB (Exabyte) = 1024^6 byte <br> - 1 ZB (Zettabyte) = 1024^7 byte <br> - 1 YB (Yottabyte) = 1024^8 byte <br> - ... |
| Dung lượng sử dụng (Usage) | Usage là dung lượng dữ liệu thực tế được tải lên vStorage. | byte | 1024 | - 1 KB (Kilobyte) = 1024 byte <br> - 1 MB (Megabyte) = 1024^2 byte <br> - 1 GB (Gigabyte) = 1024^3 byte <br> - 1 TB (Terabyte) = 1024^4 byte <br> - 1 PB (Petabyte) = 1024^5 byte <br> - 1 EB (Exabyte) = 1024^6 byte <br> - 1 ZB (Zettabyte) = 1024^7 byte <br> - 1 YB (Yottabyte) = 1024^8 byte <br> - ... |
| Lưu lượng (Traffic) | Traffic là thông số tính dựa trên dung lượng (GB) mà object được lấy khỏi storage (Get /down) | byte | 1000 | - 1 KB (Kilobyte) = 1000 byte <br> - 1 MB (Megabyte) = 1000^2 byte <br> - 1 GB (Gigabyte) = 1000^3 byte <br> - 1 TB (Terabyte) = 1000^4 byte <br> - 1 PB (Petabyte) = 1000^5 byte <br> - 1 EB (Exabyte) = 1000^6 byte <br> - 1 ZB (Zettabyte) = 1000^7 byte <br> - 1 YB (Yottabyte) = 1000^8 byte <br> - ... |
| Request | Request là một yêu cầu gửi đến một server web hoặc máy chủ từ máy khách (thông thường là trình duyệt web) để nhận và xem những thông tin có sẵn. Request bao gồm các thông tin như URL, phương thức (GET hoặc POST), header, cookie và các dữ liệu đính kèm. | number | N/A | N/A |
