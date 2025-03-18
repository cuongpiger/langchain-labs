# Object storage (HCM04)

VNGCloud giới thiệu tới bạn **Region HCM04** mới cho dịch vụ vStorage. Những tính năng nổi bật tại region này bao gồm:

* **Hiệu suất cao**: Region HCM04 được thiết kế để đáp ứng nhu cầu xử lý khối lượng truy cập lớn tới 10.000 request/giây trên mỗi IP, điều này mang lại hiệu suất vượt trội, giúp tối ưu hóa hoạt động của các ứng dụng và dịch vụ của bạn.
* **Bảo mật nâng cao**: Region HCM04 cung cấp các cơ chế mã hóa như SSE-S3, SSE-C đảm bảo an toàn tuyệt đối cho dữ liệu của khách hàng.
* **Gói cước mới - Instant Archive:** Đặc biệt, tại region HCM04, chúng tôi giới thiệu gói cước mới Instant Archive với chi phí thấp hơn, giúp khách hàng tiết kiệm chi phí lưu trữ dữ liệu dài hạn mà không phát sinh chi phí ẩn và vẫn đáp ứng đầy đủ tiêu chí cho việc lưu trữ backup.

Bắt đầu với vStorage tại Region HCM04 theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/v/vn/vstorage/object-storage/object-storage-hcm04/bat-dau-voi-object-storage).

***

## **Farm**

Farm là một thuật ngữ dùng riêng cho vStorage, farm được chúng tôi định nghĩa là một hệ thống bao gồm cơ sở hạ tầng, dịch vụ, v.v. được triển khai tại một vị trí cụ thể thuộc 2 region Hà Nội và Hồ Chí Minh với mục đích cung cấp dịch vụ lưu trữ vStorage. Đối với 2 farm HCM03, HAN01, các thông số cụ thể cho mỗi farm được chúng tôi cung cấp như sau:

| Farm | Farm ID | vStorage endpoint | Mục đích sử dụng |
| --- | --- | --- | --- |
| HCM04 | 8b1e9c9b-7123-54a5-ua8f-2d67d71c9204 | https://hcm04.vstorage.vngcloud.vn | Farm phục vụ đa mục đích với hiệu suất cao và được dùng chung cho dữ liệu lưu trữ tại Region Hồ Chí Minh. |

***

## Hạn mức tài nguyên

Các bảng sau đây liệt kê các giá trị tối đa cho tài nguyên lưu trữ trên vStorage của bạn.

### Bandwidth

| Farm | Download BW Domestic | Download BW International | Upload BW Domestic | Upload BW International |
| --- | --- | --- | --- | --- |
| HCM04 | 10Gbps shared | TBA | 10Gbps shared | TBA |

### Request per limit

* Per IP

| Storage Class | Request all types | Put request | Get request |
| --- | --- | --- | --- |
| Instant Archive | 2500 request/s/IP | 1000 request/s/IP | 1500 request/s/IP |

* Per path

| Storage Class | Request all types | Put request | Get request |
| --- | --- | --- | --- |
| Instant Archive | 2500 request/s/path | 1000 request/s/path | 1500 request/s/path |

### Các hạn mức khác

| Item | Limit |
| --- | --- |
| Số lượng object tối đa được lưu trữ trên một bucket | 600 triệu objects |
| Số lượng container/ bucket tối đa có thể tạo trên một project | Không giới hạn |
