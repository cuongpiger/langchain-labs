# Thời Gian Cache

## **Tổng quan**

* **Server Cache Expiration (TTL)** là một cơ chế quan trọng dùng để xác định khoảng thời gian vCDN sẽ lưu trữ tài nguyên của bạn. Trong thời gian này, vCDN sẽ không truy cập vào máy chủ gốc của bạn và phản hồi kết quả từ bộ đệm của vCDN. Lợi ích của việc sử dụng Server Cache Expiration có thể kể đến là: 
  * Cải thiện hiệu suất
  * Giảm băng thông sử dụng
  * Nâng cao trải nghiệm người dùng. 
* **Browser Cache Expiration** là thời gian vCDN hướng dẫn trình duyệt của khách truy cập lưu vào bộ nhớ đệm các tệp. Trong khoảng thời gian này, trình duyệt tải các tệp từ bộ đệm cục bộ, tăng tốc độ tải trang.

## Chi tiết

* **Server Cache Expiration (TTL):** Trên vCDN, bạn có thể thiết lập Server Cache Expiration (TTL) từ mức giá trị tối thiểu là 30 phút tới mức giá trị tối đa là 1 năm mà chúng tôi hỗ trợ.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(235).png?raw=true)

* **Browser Cache Expiration:** Trên vCDN, bạn có thể thiết lập Browser Cache Expiration từ mức giá trị tối thiểu là 30 phút tới mức giá trị tối đa là 1 năm mà chúng tôi hỗ trợ.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(236).png?raw=true)
