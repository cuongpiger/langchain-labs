# Object storage (HCM03, HAN01)

**Lưu trữ đối tượng** (hay còn gọi là **Object Storage**, **Cloud Storage**) là một hình thức lưu trữ dữ liệu dưới dạng các đơn vị riêng biệt gọi là **đối tượng (object)**. Mỗi đối tượng bao gồm dữ liệu thực tế (như hình ảnh, video, tệp) cùng với metadata cung cấp thông tin về đối tượng đó.

#### Lợi ích của Object Storage:

* **Hiệu quả về chi phí**:
  * Thường cung cấp chi phí thấp hơn so với các giải pháp lưu trữ truyền thống, đặc biệt đối với nhu cầu lưu trữ dữ liệu lớn.
* **Khả năng mở rộng**:
  * Dễ dàng mở rộng mà không cần cấu hình lại phức tạp hoặc ngừng hoạt động.
* **Metadata linh hoạt**:
  * Khả năng metadata phong phú tăng cường quản lý và truy xuất dữ liệu.
* **Độ bền cao**:
  * Độ bền và khả năng sẵn sàng cao nhờ vào các tính năng sao lưu và dự phòng dữ liệu.

***

## **Farm**

Farm là một thuật ngữ dùng riêng cho vStorage, farm được chúng tôi định nghĩa là một hệ thống bao gồm cơ sở hạ tầng, dịch vụ, v.v. được triển khai tại một vị trí cụ thể thuộc 2 region Hà Nội và Hồ Chí Minh với mục đích cung cấp dịch vụ lưu trữ vStorage. Đối với 2 farm HCM03, HAN01, các thông số cụ thể cho mỗi farm được chúng tôi cung cấp như sau: 

| Farm | Farm ID | Authentication endpoint | vStorage endpoint | Mục đích sử dụng |
| --- | --- | --- | --- | --- |
| HAN01 | 5d10c8ba-7187-4acc-b8c5-2d67d71c9233 | https://han.auth.vstorage.vngcloud.vn/v3 | https://han01.vstorage.vngcloud.vn | Farm phục vụ đa mục đích và được dùng chung cho dữ liệu khởi tạo project tại Region Hà Nội. |
| HCM03 | 8b1e9c9b-7123-54a5-ua8f-2d67d71c9212 | https://hcm03.auth.vstorage.vngcloud.vn/v3 | https://hcm03.vstorage.vngcloud.vn | Farm phục vụ đa mục đích và được dùng chung cho dữ liệu khởi tạo project tại Region Hồ Chí Minh. |
| HCM03 | 8b1e9c9b-7123-54a5-ua8f-2d67d71c9212 | https://hcm03.auth.vstorage.vngcloud.vn/v3 | https://hcm03-encrypt.vstorage.vngcloud.vn | Khi sử dụng encryption endpoint này, dữ liệu của bạn sẽ được tự động mã hóa khi tải tệp tin lên vStorage theo đúng chuẩn mã hóa AES-256. |

Để biết thông tin cụ thể, vui lòng tham khảo tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/vstorage-la-gi/farm-la-gi).

***

## Hạn mức tài nguyên

Các bảng sau đây liệt kê các giá trị tối đa cho tài nguyên lưu trữ trên vStorage của bạn.

### Bandwidth

| Farm | Download BW Domestic | Download BW International | Upload BW Domestic | Upload BW International |
| --- | --- | --- | --- | --- |
| HAN01 | 10Gbps shared | TBA | 10Gbps shared | TBA |
| HCM03 | 10Gbps shared | TBA | 10Gbps shared | TBA |

### Request per limit

* Per IP

| Storage Class | Request all types | Put request | Get request |
| --- | --- | --- | --- |
| Gold | 2500 request/s/IP | 1000 request/s/IP | 1500 request/s/IP |
| Silver | 2500 request/s/IP | 1000 request/s/IP | 1500 request/s/IP |
| Archive | 2500 request/s/IP | 1000 request/s/IP | 1500 request/s/IP |

* Per path

| Storage Class | Request all types | Put request | Get request |
| --- | --- | --- | --- |
| Gold | 2500 request/s/path | 1000 request/s/path | 1500 request/s/path |
| Silver | 2500 request/s/path | 1000 request/s/path | 1500 request/s/path |
| Archive | 2500 request/s/path | 1000 request/s/path | 1500 request/s/path |

### Các hạn mức khác

| Item | Limit |
| --- | --- |
| Số lượng object tối đa được lưu trữ trên một container | 600 triệu objects |
| Số lượng container/ bucket tối đa có thể tạo trên một project | Không giới hạn |
