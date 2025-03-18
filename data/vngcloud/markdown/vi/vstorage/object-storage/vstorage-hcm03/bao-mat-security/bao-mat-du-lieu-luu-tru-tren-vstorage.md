# Bảo mật dữ liệu lưu trữ trên vStorage

Mã hóa nội dung các tệp tin (object) được lưu trữ là một giải pháp bảo mật dữ liệu hiệu quả. Bằng cách mã hóa dữ liệu khi lưu trữ, dữ liệu sẽ được biến đổi thành một dạng không thể đọc được đối với những người không có quyền truy cập. Điều này giúp bảo vệ dữ liệu khỏi bị truy cập trái phép, ngay cả khi kẻ tấn công có thể truy cập vào gateway storage của hệ thống.

VNG Cloud hiện tại cung cấp cơ chế mã hóa nội dung các tệp tin (object) được lưu trữ trên dịch vụ vStorage như sau:

* **Mã hóa tại người dùng (Client-side encryption):** Trong cơ chế này, người dùng sẽ chịu trách nhiệm quản lý key và workload của quá trình mã hóa. Dữ liệu sẽ được mã hóa tại máy của người dùng hoặc lớp ứng dụng của người dùng.
* **Mã hóa tại máy chủ (Server-side encryption):** VNGCloud cung cấp tính năng mã hóa nội dung tệp tin (object) được lưu trữ trên dịch vụ vStorage bằng cách sử dụng endpoint encrypt. Khi khách hàng tải lên tệp tin thông qua endpoint này, dữ liệu sẽ được tự động mã hóa trước khi lưu trữ. Cơ chế này mang lại lợi ích bảo mật cao cho dữ liệu nhạy cảm. Cụ thể, bạn có thể sử dụng vStorage endpoint với thông số như sau:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Farm** | **Farm ID** | **Authentication endpoint** | **vStorage endpoint** | **Mục đích sử dụng** |
| HCM03 | 8b1e9c9b-7123-54a5-ua8f-2d67d71c9212 | https://hcm03.auth.vstorage.vngcloud.vn/v3 | https://hcm03-encrypt-vstorage.vngcloud.vn | Khi sử dụng encryption endpoint này, dữ liệu của bạn sẽ được tự động mã hóa khi tải tệp tin lên vStorage theo đúng chuẩn mã hóa AES-256. |

> **Chú ý:**
>
> * Khi bạn tải lên tệp tin thông qua encryption endpoint, tệp tin sẽ được mã hóa trước khi được lưu trữ trên vStorage. Lúc này,để tải xuống tệp tin, bạn có thể sử dụng bất kỳ vStorage endpoint nào thuộc farm HCM03 và tệp tin khi tải xuống đã được giải mã. 
> * Tải lên tệp tin thông qua encrypption endpoint sẽ bảo mật tệp tin của bạn hơn nhưng có thể làm giảm tốc độ tải lên. Tốc độ tải lên trung bình khi sử dụng encryption enpoint có thể giảm từ 5% đến 10% so với việc tải lên sử dụng endpoint thông thường.
