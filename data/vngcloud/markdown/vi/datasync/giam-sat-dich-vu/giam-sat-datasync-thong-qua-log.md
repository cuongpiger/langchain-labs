# Giám sát DataSync thông qua Log

#### Log là gì? 

Log là các sự kiện được thu thập tại nhiều thời điểm khác nhau. Các sự kiện này thường được tạo ra bởi các application hoặc các service và chứa đầy đủ các thông tin về ngữ cảnh tại thời điểm sự kiện xảy ra.

***

#### Tại sao log lại hữu ích? 

Log là một yếu tố quan trọng của an ninh mạng. Khi được thực thi đúng cách, ghi log có thể cung cấp cho chúng ta cái nhìn rõ ràng về những gì đang xảy ra hoặc đã xảy ra trong hệ thống của chúng ta, cho phép chúng ta chứng thực các sự kiện với độ chính xác cao hơn và thực hiện các điều chỉnh khi cần thiết.

***

#### Giám sát DataSync thông qua DataSync log trên hệ thống vMonitor Platform 

Giám sát DataSync thông qua log thật dễ dàng khi bạn sử dụng hệ thống vMonitor Platform. Hãy yên tâm là vMonitor Platform cũng là một sản phẩm thuộc hệ sinh thái của VNG Cloud. Bạn có thể sử dụng vMonitor Platform để cấu hình các tính năng giám sát dựa trên logs của DataSync. Dĩ nhiên để có thể thực hiện giám sát được thì bạn cần mua gói log quota của dịch vụ vMonitor Platform. Chi tiết bạn có thể tham khảo tại [vMonitor Platform](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor). 

Nội dung logs được đẩy về hệ thống gồm các thông tin như sau:

|  |  |  |
| --- | --- | --- |
| STT | Fields | Ý nghĩa |
| STT | Fields | Ý nghĩa |
| 1 | @timestamp | Thời gian sự kiện bắt đầu tương tự nội dung field "time" |
| 2 | rootUserAccountID | Account ID của tài khoản DataSync. |
| 3 | size | Kích cỡ file được transfer, đơn vị byte. |
| 4 | object | Tên file được transfer. |
| 5 | sourceObject |  |
| 6 | bucket | Tên bucket nguồn. |
| 7 | region | Region nguồn. |
| 8 | endpoint | Endpoint nguồn. |
| 9 | labels |  |
| 10 | taskid | Mã Task ID: được sinh ra trong mỗi chạy chạy một Transfer Job. |
| 11 | jobid | Mã Transfer Job ID: mã transfer job id mà bạn tạo từ DataSync Portal. |
| 12 | statusCode | Mã trạng thái transfer thành công hay thất bại. |
| 13 | source | Mặc định "datasync/access_log". |
| 14 | level | Mặc định "info". |
| 15 | host | Mặc định "VNGCLOUD" |
| 16 | time |  |
| 17 | objectType | Mặc định "*s3.Object". |
| 18 | destinationObject |  |
| 19 | bucket | Tên container đích nhận dữ liệu trên vStorage. |
| 20 | region | Region nhận dữ liệu |
