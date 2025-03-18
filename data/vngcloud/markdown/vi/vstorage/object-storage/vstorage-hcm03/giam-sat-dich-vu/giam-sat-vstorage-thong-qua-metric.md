# Giám sát vStorage thông qua metric

#### Metric là gì? 

Metric (hay được gọi là chỉ số) là các điểm dữ liệu chúng ta thu được nhờ vào việc đo lường, bằng cách thiết lập các phép đo đạc, theo dõi, đánh giá hoạt động nào đó trong ngữ cảnh.

***

#### Tại sao metric lại hữu ích? 

Metric cung cấp một bức tranh tổng thể về hệ thống của bạn. Bạn có thể sử dụng chúng để đánh giá tình trạng hệ thống của bạn ngay tại thời điểm hiện tại. Đối với vStorage, metric có thể giúp bạn điều chỉnh quy mô lưu trữ, khả năng đáp ứng từ đó bạn có thể điều chỉnh nhu cầu cùng như xác định chính xác lượng tài nguyên bạn cần tiêu thụ để có thể giúp bạn tiết kiệm tiền hoặc cải thiện hiệu suất.

***

#### Giám sát vStorage thông qua vStorage metric trên hệ thống vMonitor Platform 

Giám sát vStorage thông qua metric thật dễ dàng khi bạn sử dụng hệ thống vMonitor Platform. Chúng tôi đã chuyển các thông số metric từ vStorage qua vMonitor Platform đều đặn theo chu kỳ 5 phút. Hãy yên tâm là vMonitor Platform cũng là một sản phẩm thuộc hệ sinh thái của VNG Cloud. Bạn có thể sử dụng vMonitor Platform để cấu hình các tính năng giám sát dựa trên các thông số này. Dĩ nhiên để có thể thực hiện giám sát được thì bạn cần mua gói metric quota của dịch vụ vMonitor Platform. Chi tiết bạn có thể tham khảo tại [vMonitor Platform](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor). Dưới đây là danh sách vStorage metric mà chúng tôi đã cung cấp cho mục đích giám sát:

| Account  metric | Type | Fields - Field | Fields - Unit | Fields - Description | Interval |
| --- | --- | --- | --- | --- | --- |
| account_stats | gauge | bytes_used | byte | Lượng data sử dụng | 5 phút |
|  |  | container_count | number | Lượng container đang tồn tại |  |
|  |  | object_count | number | Số object đang có |  |
|  |  | quota_bytes | byte | Tổng quota mua theo bytes |  |
|  |  | used_percent | % | Phần trăm sử dụng theo thời gian (bytes_used/ quota_bytes *100) |  |
|  | diff | bytes_used_diff | byte |  |  |
|  |  | container_count_diff | number | Số lượng container sinh ra hoặc giảm xuống theo chu kỳ 5 phút |  |
|  |  | object_count_diff | number | Số lượng object sinh ra hoặc giảm xuống theo chu kỳ 5 phút |  |
| account_net | counter | bytes_recvd | byte | Lưu lượng data proxy nhận với action upload theo chu kỳ 1 phút | 1 phút |
|  |  | bytes_sent | byte | Lưu lượng data proxy truyền đi với action download theo chu kỳ 1 phút |  |
|  |  | bytes_sum | byte | Tổng lưu lượng data 2 chiều (bytes_recvd+ bytes_sent) theo chu kỳ 1 phút |  |
|  | rate | bytes_recvd_rate | pcs | Tốc độ dữ liệu tải lên tính theo vận tốc trên giây (bytes/s) |  |
|  |  | bytes_sent_rate | pcs | Tốc độ dữ liệu tải xuống tính theo vận tốc trên giây (bytes/s) |  |
|  |  | bytes_sum_rate | pcs | Tốc độ dữ liệu tải lên + tải xuống tính theo vận tốc trên giây (bytes/s) |  |
| account_net_country | counter | bytes_recvd | byte | Lưu lượng data proxy nhận với action upload trong chu kỳ 1 phút | 1 phút |
|  |  | bytes_sent | byte | Lưu lượng data proxy truyền đi với action download trong chu kỳ 1 phút |  |
|  |  | bytes_sum | byte | Tổng lưu lượng data 2 chiều (bytes_recvd+ bytes_sent) trong chu kỳ 1 phút |  |
|  | rate | bytes_recvd_rate | pcs | Tốc độ tải lên dữ liệu tính theo vận tốc trên giây (bytes/s) theo từng quốc gia |  |
|  |  | bytes_sent_rate | pcs | Tốc độ tải xuống dữ liệu tính theo vận tốc trên giây (bytes/s) theo từng quốc gia |  |
|  |  | bytes_sum_rate | pcs | Tốc độ tải lên + tải xuống dữ liệu tính theo vận tốc trên giây (bytes/s) theo từng quốc gia |  |
| account_net_vngcloud | counter | bytes_recvd | byte | Lưu lượng data hệ thống nhận với action upload trong chu kỳ 1 phút | 1 phút |
|  |  | bytes_sent | byte | Lưu lượng data hệ thống truyền đi với action download trong chu kỳ 1 phút |  |
|  |  | bytes_sum | byte | Tổng lưu lượng data 2 chiều (bytes_recvd +  bytes_sent) trong chu kỳ 1 phút |  |
|  | rate | bytes_recvd_rate | pcs | Tốc độ tải lên dữ liệu tính theo vận tốc trên giây (bytes/s) với nguồn xuất phát từ VNG Cloud |  |
|  |  | bytes_sent_rate | pcs | Tốc độ tải xuống dữ liệu tính theo vận tốc trên giây (bytes/s) với nguồn xuất phát từ VNG Cloud |  |
|  |  | bytes_sum_rate | pcs | Tốc độ  tải lên, tải xuống dữ liệu tính theo vận tốc trên giây (bytes/s) với nguồn xuất phát từ VNG Cloud |  |
| account_net_user | counter | bytes_recvd | byte | Lưu lượng data hệ thống nhận với action upload trong chu kỳ 1 phút | 1 phút |
|  |  | bytes_sent | byte | Lưu lượng data hệ thống truyền đi với action download trong chu kỳ 1 phút |  |
|  |  | bytes_sum | byte | Tổng lưu lượng data 2 chiều (bytes_recvd + bytes_sent) trong chu kỳ 1 phút |  |
|  | rate | bytes_recvd_rate | pcs | Tốc độ tải lên dữ liệu tính theo vận tốc trên giây (bytes/s) với nguồn xuất phát từ bên ngoài internet |  |
|  |  | bytes_sent_rate | pcs | Tốc độ tải xuống dữ liệu tính theo vận tốc trên giây (bytes/s) với nguồn xuất phát từ bên ngoài internet |  |
|  |  | bytes_sum_rate | pcs | Tốc độ tải lên tải xuống dữ liệu tính theo vận tốc trên giây (bytes/s) với nguồn xuất phát từ bên ngoài internet |  |
| account_requests.request_total | counter | value | number | Số lượng request xử lý tính theo chu kỳ 1 phút | 1 phút |
|  | rate | value_rate | psc | Tổng số request/s trên từng project tính theo chu kỳ 1 phút |  |
| account_requests.status | counter | value | number | Số lượng request xử lý tính theo chu kỳ 1 phút | 1 phút |
|  | rate | value_rate | psc | Tổng số request/s trên từng project được phân nhóm theo trạng thái trả về của request và được tính theo chu kỳ 1 phút |  |
| account_requests.method | counter | value | number | Số lượng request xử lý tính theo chu kỳ 1 phút | 1 phút |
|  | rate | value_rate | psc | Tổng số request/s trên từng project được phân nhóm theo loại request (GET, PUT, POST, DELETE) và được tính theo chu kỳ 1 phút |  |
| account_requests.features | counter | value | number | Số lượng request xử lý theo chu kỳ 1 phút | 1 phút |
|  | rate | value_rate | psc | Tổng số request/s trên từng project được nhóm theo tính năng người dùng sử dụng và tính theo chu kỳ 1 phút |  |
| account_requests.request_time | timing | count | number | Số lượng request trong interval | 1 phút |
|  |  | lower | second | Giá trị thấp nhất trong dãy value nhận được |  |
|  |  | mean | second | Giá trị bình quân trong dãy value nhận được |  |
|  |  | stddev | second | Biên độ giao động trong dãy value nhận được |  |
|  |  | sum | second | Tổng thời gian xử lý của các request |  |
|  |  | upper | second | Giá trị cao nhất trong dãy value nhận được |  |
|  |  | 90_percentile | second | Mức giá trị chiếm 90% trong dãy value nhận được |  |
|  |  | 99_percentile | second | Mức giá trị chiếm 99% trong dãy value nhận được |  |
| account_requests.bytes_per_second | timing | count | number | Số lượng request trong interval | 1 phút |
|  |  | lower | byte/s | Giá trị thấp nhất trong dãy value nhận được |  |
|  |  | mean | byte/s | Giá trị bình quân trong dãy value nhận được |  |
|  |  | stddev | byte/s | Biên độ giao động trong dãy value nhận được |  |
|  |  | sum | byte/s | Tổng thời gian xử lý của các request |  |
|  |  | upper | byte/s | Giá trị cao nhất trong dãy value nhận được |  |
|  |  | 90_percentile | byte/s | Mức giá trị chiếm 90% trong dãy value nhận được |  |
|  |  | 99_percentile | byte/s | Mức giá trị chiếm 99% trong dãy value nhận được | 57 |
| container_stats | gauge | bytes_used | byte | Lượng data sử dụng | 5 phút |
|  |  | object_count | number | Số object đang có |  |
|  |  | quota_bytes | byte | Quota mua theo bytes |  |
|  | diff | bytes_used_diff | byte | Tổng số bytes dữ liệu tăng thêm hoặc giảm đi trên từng container theo chu kỳ 5 phút |  |
|  |  | object_count_diff | number | Tổng số object tăng thêm hoặc giảm đi trên từng container theo chu kỳ 5 phút |  |
