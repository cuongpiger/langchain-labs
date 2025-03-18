# Farm là gì?

Farm là một thuật ngữ dùng riêng cho vStorage, farm được chúng tôi định nghĩa là một hệ thống bao gồm cơ sở hạ tầng, dịch vụ, v.v. được triển khai tại một vị trí cụ thể thuộc 2 region Hà Nội và Hồ Chí Minh với mục đích cung cấp dịch vụ lưu trữ vStorage. Tương tự như region, bạn có thể chọn một farm làm nơi lưu trữ dữ liệu của bạn, việc chọn farm hợp lý sẽ giảm tải cho hệ thống cũng như tối ưu chi phí hoạt động lưu trữ cho doanh nghiệp của bạn. 

***

#### Danh sách các farm vStorage cung cấp 

* Hiện tại, chúng tôi cung cấp cho bạn 2 farm được mô tả ở bảng bên dưới:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Farm** | **Farm ID** | **Authentication endpoint** | **vStorage endpoint** | **Mục đích sử dụng** |
| HAN01 | 5d10c8ba-7187-4acc-b8c5-2d67d71c9233 | https://han.auth.vstorage.vngcloud.vn/v3 | https://han01.vstorage.vngcloud.vn | Farm phục vụ đa mục đích và được dùng chung cho dữ liệu khởi tạo project tại Region Hà Nội. |
| HCM03 | 8b1e9c9b-7123-54a5-ua8f-2d67d71c9212 | https://hcm03.auth.vstorage.vngcloud.vn/v3 | https://hcm03.vstorage.vngcloud.vn | Farm phục vụ đa mục đích và được dùng chung cho dữ liệu khởi tạo project tại Region Hồ Chí Minh. |

* VNGCloud cung cấp tính năng mã hóa nội dung tệp tin (object) được lưu trữ trên dịch vụ vStorage bằng cách sử dụng endpoint encrypt. Khi khách hàng tải lên tệp tin thông qua endpoint này, dữ liệu sẽ được tự động mã hóa trước khi lưu trữ. Cơ chế này mang lại lợi ích bảo mật cao cho dữ liệu nhạy cảm. Cụ thể, bạn có thể sử dụng vStorage endpoint với thông số như sau:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Farm** | **Farm ID** | **Authentication endpoint** | **vStorage endpoint** | **Mục đích sử dụng** |
| HCM03 | 8b1e9c9b-7123-54a5-ua8f-2d67d71c9212 | https://hcm03.auth.vstorage.vngcloud.vn/v3 | https://hcm03-encrypt.vstorage.vngcloud.vn | Khi sử dụng encryption endpoint này, dữ liệu của bạn sẽ được tự động mã hóa khi tải tệp tin lên vStorage theo đúng chuẩn mã hóa AES-256. |

> **Chú ý:**
>
> * Khi bạn tải lên tệp tin thông qua encryption endpoint, tệp tin sẽ được mã hóa trước khi được lưu trữ trên vStorage. Lúc này,để tải xuống tệp tin, bạn có thể sử dụng bất kỳ vStorage endpoint nào thuộc farm HCM03 và tệp tin khi tải xuống đã được giải mã. 
> * Tải lên tệp tin thông qua encrypption endpoint sẽ bảo mật tệp tin của bạn hơn nhưng có thể làm giảm tốc độ tải lên. Tốc độ tải lên trung bình khi sử dụng encryption enpoint có thể giảm từ 5% đến 10% so với việc tải lên sử dụng endpoint thông thường.

Đối với mỗi farm, ngoài các tính năng vStorage chung, sẽ có một số tính năng riêng biệt đặc trưng cho farm đó. Chi tiết sẽ được chúng tôi cập nhật sớm nhất tại đây.  Bạn cũng có thể yêu cầu chúng tôi cung cấp một farm đặc biệt nếu dữ liệu bạn cần lưu trữ đủ lớn và là dữ liệu đặc thù. Để liên hệ với chúng tôi, bạn có thể yêu cầu hỗ trợ hay liên hệ trực tiếp tới nhân viên VNG Clou đang hỗ trợ của bạn.
