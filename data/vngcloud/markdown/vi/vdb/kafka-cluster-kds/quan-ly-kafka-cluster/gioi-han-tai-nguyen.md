# Giới hạn tài nguyên

Dưới đây là một số giới hạn về tài nguyên mà vDB Kafka Cluster áp dụng, cụ thể như sau:

| Giới hạn Tài Nguyên | Giá trị giới hạn | Lý do | Cách làm việc hiệu quả |
| --- | --- | --- | --- |
| Số lượng cluster / người dùng | 10 | Đảm bảo phân bổ tài nguyên hợp lý và tránh tình trạng người dùng tạo quá nhiều cụm không cần thiết, ảnh hưởng đến hiệu suất chung của hệ thống. | Lập kế hoạch cẩn thận và chỉ tạo các cụm Kafka thực sự cần thiết. Nếu cần nhiều cụm hơn giới hạn, liên hệ với bộ phận hỗ trợ. |
| Số lượng config group | 10 | Giúp quản lý cấu hình tập trung và tránh sự phức tạp khi có quá nhiều nhóm cấu hình. | Sử dụng các nhóm cấu hình một cách hiệu quả, gom nhóm các cấu hình tương tự nhau và tái sử dụng chúng cho nhiều cụm Kafka. |
| Số lượng topic / cluster | 50 | Quá nhiều topic có thể ảnh hưởng đến hiệu suất của cụm Kafka và làm phức tạp việc quản lý. | Thiết kế cấu trúc topic một cách cẩn thận, sử dụng các topic một cách hiệu quả và tránh tạo quá nhiều topic không cần thiết. |
| Số lương kafka user / cluster | 50 | Quá nhiều user có thể ảnh hưởng đến hiệu suất xác thực và ủy quyền, cũng như làm phức tạp việc quản lý. | Sử dụng các user một cách hiệu quả, gom nhóm các user có cùng quyền truy cập và sử dụng các tính năng quản lý user như nhóm và vai trò để đơn giản hóa việc quản lý quyền truy cập. |
