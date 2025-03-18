# Log search

### Tổng quan

Table chart với chỉ số tóm tắt là một loại biểu đồ thể hiện các số được tính toán từ một bộ dữ liệu, thay vì thể hiện các số gốc. Thông thường loại biểu đồ này nên được sử dụng khi bạn muốn nhóm dữ liệu theo thời gian sử dụng tính năng Group by.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(73).png?raw=true)

***

### Cấu hình biểu đồ

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(74).png?raw=true)

#### 1. Choose graph style 

Đối với biểu đồ dạng table, tại mục này bạn chọn Style là **Log search**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(75).png?raw=true)

#### 2. Graph your data

Chọn loại dữ liệu để vẽ Widget:

* **Metrics: không hỗ trợ.**
* Logs: xem [Log Query](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/dashboard/query/log-query) để cấu hình cho loại dữ liệu Logs.

**Mặc định dữ liệu logs được hiển thị ở dạng Full content**. Khi bạn chỉ muốn hiển thị một số lượng field logs nhất định trên biểu đồ, hãy chọn field logs tại 

<figure><img src="https://docs-admin.vngcloud.vn/download/attachments/59806976/image2023-8-1_13-27-58.png?version=1&#x26;modificationDate=1690871279000&#x26;api=v2" alt="" width="375"><figcaption></figcaption></figure>

Alias: Bạn có thể đặt Alias cho mỗi câu query, alias này sẽ được hiển thị trên graph và legend, điều này rất hữu ích cho những tên metric, logs hay những câu query có filter (bộ lọc) dài. 

#### 3. Fixed time range 

Khung thời gian cố định là một thuộc tính của Widget mà bạn có thể thiết lập để lọc dữ liệu trên Widget theo một khung thời gian cố định mà không phụ thuộc với khung thời gian (time range) của Dashboard. Mỗi Widget đều có thể thiết lập Fixed time range riêng biệt, bạn có thể chọn một trong các khung thời gian được mô tả ở bảng bên dưới. Ví dụ: nếu bạn chọn Global time thì khoảng thời gian lấy dữ liệu trên Widget được hiển thị sẽ được bằng khoảng thời gian mà bạn chọn trên Dashboard. Tức là khi thay đổi thời gian lấy dữ liệu trên Dashboard thì thời gian lấy dữ liệu của Widget sẽ thay đổi theo. Khuyến khích sử dụng lựa chọn này. Nếu bạn chọn Pass N minutes (N = 5,10,...) thì khoảng thời gian lấy dữ liệu trên Widget cố định (không thay đổi) luôn là 5, 10,...phút trước. 

Chọn **Create** để tạo Widget, nếu có nhu cầu thay đổi tên widget thì bạn có thể thực hiện chỉnh sửa tại **Widget name**.
