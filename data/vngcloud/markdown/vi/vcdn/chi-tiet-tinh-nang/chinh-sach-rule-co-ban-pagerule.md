# Page Rule

## Tổng quan

**Page Rule** là một công cụ mạnh mẽ trong hệ thống vCDN cho phép bạn tùy chỉnh cách CDN xử lý các yêu cầu đến website dựa trên các quy tắc được định nghĩa trước. Với Page Rule, bạn có thể áp dụng các thiết lập cụ thể cho một hoặc nhiều URL, giúp tối ưu hóa hiệu suất, tăng cường bảo mật, hoặc cải thiện trải nghiệm người dùng.

## Chi tiết

Khi khởi tạo Live Stream, Object Download,...bạn có thể khởi tạo Page Rule bằng cách chọn **Create Page Rule**. Một Rules sẽ được thực thi khi mà có URI request đúng với điều kiện đã được định nghĩa trong Rule.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(18)%20(1)%20(1)%20(1).png?raw=true)

Sau khi bạn chọn Create Page Rule, màn hình hiển thị như sau:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(19)%20(1)%20(1).png?raw=true)

Trong đó: 

* **URL Pattern:** nhập URL pattern cần áp dụng Page Rule, vCDN hỗ trợ kiểu khai báo “\*” đại diện cho một chuỗi nhiều ký tự. Ví dụ: /trang\_landing\_cu.html
* **Các hành động khi thỏa điều kiện:** Mỗi Rules khi thỏa điệu kiện đúng URI được request sẽ có thể tùy chọn thực thi một trong khác hành động sau:
  * Always Use HTTPS 
  * Auto Minify 
  * Automatic HTTPS Rewrites 
  * Server Cache TTL 
  * Browser Cache TTL 
  * Bypass Cache by Cookie 
  * Bypass Cache By Device Type
  * Forwarding URL 
  * Add Response Header 
  * Brotli 
  * Gzip
  * Origin Override

Cụ thể, vui lòng tham khảo bảng bên dưới.

Mỗi Page Rule sẽ có các hành động action khác nhau được thể hiện ở bảng dưới đây. “Order” nhằm sắp xếp vị trí các rule, số càng nhỏ, ưu tiên thực hiện càng lớn.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(20)%20(1)%20(1).png?raw=true)

Sau khi tạo xong, chọn **Save changes** để cập nhật thay đổi.

***

Bảng mô tả các loại hành động:

| Rule | Action | Mô tả |
| --- | --- | --- |
| **Always Use HTTPS** | ON/OFF | Bật/Tắt tùy chọn “Luôn sử dụng giao thức HTTPS” trên trang chỉ định. |
| **Auto Minify** | Javascript / CSS / HTML | Tùy chọn ghi đè chức năng minify trên trang chỉ định. |
| **Automatic HTTPS Rewrites** | ON/OFF | Bật tắt tính năng tự động replace các URL HTTP thành HTTPS trong trang chỉ định. |
| **Server Cache TTL** |  | Tùy chọn lại thời gian lưu cache trên các Edge Servers hoặc “Bypass Cache” trên trang chỉ định. |
| **Browser Cache TTL** |  | Tương tự “Server Cache TTL”, nhưng là quy định thời gian cache trên trình duyệt End-user. |
| **Bypass Cache By Cookie** | Nhập giá trị “cookie_name” và “cookie_value” | Nếu có cookie được chỉ định từ end-user gửi lên, hệ thống sẽ thực hiện lệnh bypass cache trên trang chỉ định. Nếu giá trị “cookie_value” là rỗng, hệ thống chỉ xét nếu tồn tại “cookie_name” và không quan tâm giá trị của “cookie_value” |
| **Bypass Cache By Device Type** | Nhập các giá trị “Agent Text”, hỗ trợ nhiều giá trị, phân cách bởi dấu “Tab” hoặc “Enter” | Nếu trình duyệt end-user sử dụng có thông tin giống một trong các Agent Text, hệ thống sẽ tự bypass cache trên trang chỉ định. |
| **Forwarding URL** | Mã chuyển hướng (301/302) và URL đích. | Tự chuyển hướng URL được chỉ định về URL đích mới. |
| **Host Header Override** | Header_name và header_value | Tự động add thêm header trả về cho trình duyệt end-user trên trang được chỉ định. |
| **Brotli** | ON/OFF | Tùy chọn bật/tắt Brotli trên trang được chỉ định. |
| **Gzip** | ON/OFF | Tùy chọn bật/tắt Gzip trên trang được chỉ định. |
| **Resolve Origin Override** | IP New Origin | Tùy chọn thay đổi IP Server Origin ở trang chỉ định.* |
