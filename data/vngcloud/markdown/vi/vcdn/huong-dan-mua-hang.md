# Cách tính phí

## Tổng quan

Hệ thống **vCDN** hỗ trợ cả hai loại người dùng:

1. **Người dùng trả trước**: Khách hàng mua trước dung lượng **Traffic** và sử dụng theo lượng đã mua.
2. **Người dùng trả sau**: Khách hàng sử dụng dịch vụ trước và thanh toán dựa trên mức tiêu thụ vào cuối kỳ.

***

## Traffic Package 

### **Người dùng trả trước**

Khi mua **Traffic**, bạn có thể lựa chọn:

* **Group Type**: Chọn thời gian gói sử dụng (**3 tháng,** **6 tháng hoặc 12 tháng**).
* **Traffic Type**: Loại lưu lượng:
  * **Domestic**: Lưu lượng nội địa.
  * **International**: Lưu lượng quốc tế.
* **Package Traffic**: Dung lượng **Traffic** mong muốn.

> **Lưu ý:**
>
> * Nếu bạn chọn **Traffic type = Domestic**, tối đa **20% traffic** có thể được sử dụng cho **international**.
>   * Ví dụ: Gói Domestic 50000GB → 10000GB được phép dùng cho International.
> * **Khi bạn sử dụng hết Traffic**:
>   * **Domestic**: Có thể mua **Extra Domestic**, thời gian sử dụng phụ thuộc vào thời hạn của gói chính.
>   * **International**: Có thể mua **Extra International** với thời hạn tương tự.
> * Nếu bạn chọn **Traffic type =** **International**, traffic này có thể dùng cho cả **Domestic và International.**
> * Mỗi tài khoản chỉ được áp dụng **1 gói chính duy nhất tại một thời điểm nhưng có thể mua nhiều gói extra.**
> * Hệ thống có hỗ trợ **cộng dồn traffic** nếu bạn thay đổi gói.

### **Người dùng trả sau**

* Hệ thống sẽ thống kê **traffic tiêu thụ hàng tháng** và tính toán chi phí thanh toán vào cuối tháng.

## **Accelerator Package** 

Khách hàng có thể mua các gói theo tính năng như:

* **Basic**, **Standard**, **Pro**, và **Enterprise**.
* Những gói này chỉ áp dụng cho dịch vụ **Web Accelerator**.

**DANH SÁCH CÁC TÍNH NĂNG CỦA WEB ACCELERATOR**

| Tính năng | Mô tả | Cơ bản | Tiêu chuẩn | Cao cấp | Doanh Nghiệp |
| --- | --- | --- | --- | --- | --- |
| Enable HTTP2 | Bật/tắt hỗ trợ HTTP/2 | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| CDN | Số lượng CDN có thể được tạo | 1 | 3 | 5 | 20 |
| Multi CNAME | Hỗ trợ khách hàng điền nhiều domain để sử dụng dịch vụ trên mỗi CDN |  | 3 | 5 | 10 |
| SSL Cert | Hỗ trợ khách hàng upload SSL để sử dụng dịch vụ | 50 | 50 | 50 | 50 |
| Tối ưu hình ảnh | Tự động tối ưu hình ảnh trên website khách hàng:   - Nếu hình ảnh chất lượng cao, tự giảm về 1080p hoặc bằng kích thước chiều dọc của màn hình thiết bị (<1080);   - Chất lượng ảnh: Tự động nén ảnh còn 60% cho PC, Tablet là 50% và mobile còn 30%; **Với các trình duyệt hỗ trợ định dạng ảnh WebP => Tự động convert ảnh sang WebP để giảm dung lượng và tăng tốc độ load trang. |  |  | Có hỗ trợ | Có hỗ trợ |
| Tự động thu nhỏ | Tự động tối ưu các đoạn Javascript, CSS, HTMl trên website của khách hàng. | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Cân bằng tải | Hỗ trợ LB các Servers Origin trong pool để phân bố request hợp lý, các loại LB Algorithms hỗ trợ: Weight RoundRobin, Least Connected, IP Hashing. |  | 3 (ips) | 5 (ips) | 50 (ips) |
| Hỗ trợ HSTS | Hổ trợ HSTS | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Hỗ trợ HTTPS | Tự động rewrite trang chủ từ http -> https | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Automatic HTTPS Rewrites | Hỗ trợ rewrite các url http sang https tự động trong page content |  | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| TLS 1.3: Hỗ trợ TLS Version 1.3 | Hỗ trợ chọn version TLS thấp nhất có thể hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Brotli Compression | Tùy chọn nén trang giúp giảm dung lượng đối với các thiết bị hỗ trợ |  | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Cache | Tùy chọn cache kết quả phản hồi từ origin | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Development Mode | Bật chế độ không cache trên toàn dịch vụ |  | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Cache Browser | Thời gian Cache trên Browser | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |
| Cache Edge TTL | Thời gian Cache trên Edge | >3 ngày | >1 ngày | >12 giò | >30 phút |
| Purge Cache | Công cụ hỗ trợ xóa nội dung đã cache trên hệ thống CDN | 5 lần/ngày | 20 lần/ngày | 50 lần/ngày | 1000 lần/ngày |
| Page Rules | Tùy chọn page rule để điều chỉnh cache, chất lượng, kích thước, định dạng ảnh | 1 rule | 3 rule | 5 rule | 100 rule |
| Thống kê | Báo cáo thống kê | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ | Có hỗ trợ |

##  **Các bước thực hiện**

Hướng dẫn mua và sử dụng Traffic trên vCDN Portal

**Bước 1**: Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/).

**Bước 2**: Chọn **Package** hoặc **Buy More Traffic**. Màn hình **vCDN Billing** sẽ hiển thị.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(859).png?raw=true)

**Bước 3**: Chọn **Accelerator Package** và **Period** (thời hạn sử dụng) mà bạn mong muốn. Nhấn **Confirm** để tiếp tục.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(860).png?raw=true)

**Bước 4**: Tiếp tục thực hiện theo điều kiện:

* **Đối với khách hàng trả trước**: chọn thời gian sử dụng và gói **Traffic Package** mong muốn
* **Đối với khách hàng trả sau**: không cần chọn gói Traffic, có thể sử dụng ngay và thanh toán vào cuối tháng.
* Sau khi chọn gói (nếu có), nhấn **Confirm**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(861).png?raw=true)

**Bước 5**: Tại mục **Payment Details**, kiểm tra lại các gói dịch vụ đã chọn. Nếu thông tin chính xác, chọn **Payment Confirm** để hoàn tất.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(862).png?raw=true)

**Bước 6**: Tại màn hình **Payment Confirm**, chọn **Continue**. Thực hiện các bước thanh toán theo hướng dẫn.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(863).png?raw=true)

**Bước 7:** Sau khi hoàn tất, bạn có thể kiểm tra thông tin thanh toán và tiêu thụ tại mục **Pay/Consume History**.
