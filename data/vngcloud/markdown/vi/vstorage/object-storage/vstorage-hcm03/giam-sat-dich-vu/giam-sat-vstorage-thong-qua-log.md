# Giám sát vStorage thông qua log

#### Log là gì? 

Log là các sự kiện được thu thập tại nhiều thời điểm khác nhau. Các sự kiện này thường được tạo ra bởi các application hoặc các service và chứa đầy đủ các thông tin về ngữ cảnh tại thời điểm sự kiện xảy ra.

***

#### Tại sao log lại hữu ích? 

Log là một yếu tố quan trọng của an ninh mạng. Khi được thực thi đúng cách, ghi log có thể cung cấp cho chúng ta cái nhìn rõ ràng về những gì đang xảy ra hoặc đã xảy ra trong hệ thống của chúng ta, cho phép chúng ta chứng thực các sự kiện với độ chính xác cao hơn và thực hiện các điều chỉnh khi cần thiết.

***

#### Giám sát vStorage thông qua vStorage log trên hệ thống vMonitor Platform 

Giám sát vStorage thông qua log thật dễ dàng khi bạn sử dụng hệ thống vMonitor Platform. Chúng tôi đã chuyển logs từ vStorage qua vMonitor Platform đều đặn theo chu kỳ 5 phút. Hãy yên tâm là vMonitor Platform cũng là một sản phẩm thuộc hệ sinh thái của VNG Cloud. Bạn có thể sử dụng vMonitor Platform để cấu hình các tính năng giám sát dựa trên logs của vStorage. Dĩ nhiên để có thể thực hiện giám sát được thì bạn cần mua gói log quota của dịch vụ vMonitor Platform. Chi tiết bạn có thể tham khảo tại [vMonitor Platform](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor). 

Nội dung logs được đẩy về hệ thống gồm các thông tin như sau:

|  |  |
| --- | --- |
| **Fields** | **Ý nghĩa** |
| @timestamp | Thời gian sự kiện bắt đầu tương tự nội dung field "request_start_time" |
| account | Account ID của tài khoản vStorage, có định dạng AUTH_<ID> |
| bytes_per_second | Vận tốc tải lên hoặc tải xuống tùy ngữ cảnh của request, số được tính toán dựa trên dữ liệu máy chủ gửi, nhận và thời gian để hoàn thành |
| bytes_recvd | Tổng số bytes dữ liệu máy chủ nhận được , tương đương với chiều người dùng tải lên dữ liệu |
| bytes_sent | Tổng số bytes dữ liệu máy chủ đã gửi tới ngươi dùng, tương đương với chiều người dùng tải xuống dữ liệu |
| bytes_sum | Tổng số bytes cả hai chiều tải lên và tải xuống |
| client_country | Quốc gia của địa chỉ IP đã tương tác |
| client_ip | Địa chỉ IP của thiết bị đã tương tác |
| cls_service | Đại diện dịch vụ đã sinh ra dòng Log. Ví dụ: vStorage |
| container | Tên của container |
| host | VNGCLOUD |
| lag_seconds |  |
| object | Tên của object |
| policy_index | ID của gói lưu trữ: Gold/Silver/Archive theo thứ tự là 0,1,2 |
| project_id | ID của project |
| received_at | Thời gian nhận request |
| referer | Thông tin địa chỉ website đã yêu cầu object trực tiếp từ browser người dùng trong trường hợp container được public hoặc qua vCDN |
| region | Khu vực lưu trữ trên vStorage. Ví dụ: HCM01, HAN01 |
| request_end_time | Thời gian request hoàn tất trên máy chủ lưu trữ |
| request_method | Method của request thường là GET/PUT/POST/DELETE/HEAD |
| request_path | Đường dẫn đầy đủ của request |
| request_start_time | Thời gian bắt đầu nhận request từ người dùng |
| request_time | Tổng thời gian hoàn tất yêu cầu theo đơn vị giây (seconds) |
| source | Nguồn xuất phát Request. Ví dụ: "S3" tức request khách hàng đang dùng S3 kết nối, "-" request đang dùng Swift, "SLO" request đang dùng Large Object và đang thực hiện segments/Multipart |
| status_int | Mã phản hồi từ máy chủ thể hiện thành công hoặc thất bại. Ví dụ: 200, 201, 401, 404... |
| storage_class | Storage class mà Container đã đăng ký (Gold/Silver/Archive) |
| transaction_id | ID của Request đã thực hiện dùng truy vết hoặc so sánh một Request cụ thể giữa máy chủ và khách hàng |
| user_agent | Thông tin User-Agent trong Request HTTP, thể hiện phiên bản Client/Browser/Application đang thực hiện kết nối đến máy chủ để thực thi Request |
