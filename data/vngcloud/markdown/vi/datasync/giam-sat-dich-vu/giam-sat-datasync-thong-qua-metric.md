# Giám sát DataSync thông qua Metric

#### Metric là gì? 

Metric (hay được gọi là chỉ số) là các điểm dữ liệu chúng ta thu được nhờ vào việc đo lường, bằng cách thiết lập các phép đo đạc, theo dõi, đánh giá hoạt động nào đó trong ngữ cảnh.

***

#### Tại sao metric lại hữu ích? 

Metric cung cấp một bức tranh tổng thể về hệ thống của bạn. Bạn có thể sử dụng chúng để đánh giá tình trạng hệ thống của bạn ngay tại thời điểm hiện tại. Đối với DataSync, metric có thể giúp bạn điều chỉnh quy mô lưu trữ, khả năng đáp ứng từ đó bạn có thể điều chỉnh nhu cầu cùng như xác định chính xác lượng tài nguyên bạn cần tiêu thụ để có thể giúp bạn tiết kiệm tiền hoặc cải thiện hiệu suất.

***

#### Giám sát DataSync thông qua DataSync metric trên hệ thống vMonitor Platform 

Giám sát DataSync thông qua metric thật dễ dàng khi bạn sử dụng hệ thống vMonitor Platform. Chúng tôi đã chuyển các thông số metric từ DataSync qua vMonitor Platform đều đặn theo chu kỳ 5 phút. Hãy yên tâm là vMonitor Platform cũng là một sản phẩm thuộc hệ sinh thái của VNG Cloud. Bạn có thể sử dụng vMonitor Platform để cấu hình các tính năng giám sát dựa trên các thông số này. Dĩ nhiên để có thể thực hiện giám sát được thì bạn cần mua gói metric quota của dịch vụ vMonitor Platform. Chi tiết bạn có thể tham khảo tại [vMonitor Platform](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor). Dưới đây là danh sách DataSync metric mà chúng tôi đã cung cấp cho mục đích giám sát:

|  |  |  |  |
| --- | --- | --- | --- |
| STT | Metric | Mô tả | Interval |
| 1 | datasync_bytes_transferred_total | Tổng số byte transfer. | 1 phút |
| 2 | datasync_checked_files_total | Tổng số file được kiểm tra. | 1 phút |
| 3 | datasync_dirs_deleted_total | Tổng số thư mục bị xóa. | 1 phút |
| 4 | datasync_errors_total | Tổng số file error được ghi nhận. | 1 phút |
| 5 | datasync_fatal_error | Tổng số lỗi xảy ra. | 1 phút |
| 6 | datasync_files_deleted_total | Tổng số file bị xóa. | 1 phút |
| 7 | datasync_files_renamed_total | Tổng số file bị rename. | 1 phút |
| 8 | datasync_files_transferred_total | Tổng số file được transfer. | 1 phút |
| 9 | datasync_http_status_code | Số lượng trạng thái xảy ra của quá trình transfer dữ liệu. | 1 phút |
| 10 | datasync_retry_error | Tổng số lượng file bị lỗi trong quá trình retry. | 1 phút |
| 11 | datasync_speed | Tốc độ trung bình tính bằng byte trên giây kể từ khi bắt đầu quá trình transfer dữ liệu. | 1 phút |
