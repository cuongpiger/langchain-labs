# Metric Alarm

Khi bạn tạo **Alarm** cho dữ liệu **metric**, trong phần **Set Alarm Conditions.** Các thành phần tạo nên câu lệnh truy vấn đối với dữ liệu metric bao gồm: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(109).png?raw=true)

Trong đó

### 1. Metric name

**Metric**: lựa chọn **metric** bằng cách tìm kiếm và chọn từ danh sách metric. Danh sách **metric** này bạn có thể xem tại mục **Metric Information**, chi tiết tham khảo tại [Làm việc với Metric Information.](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/lam-viec-voi-metruc-information)

### 2. Filter

**Filter**: metric mà bạn lựa chọn có thể được filter bởi các **dimensions** (ví dụ host,device,...) từ danh sách **dimensions** được hiển thị, bạn có thể chọn nhiều **dimensions** tại đây. Ngoài việc chọn các dimensions có giá trị cố định của metric, tại đây bạn có thể sử dụng các **variable** để filter linh động hơn. Các **variable** này đã được bạn định nghĩa tại **Dashboard** mà bạn đang muốn tạo **Widget**. Để tìm hiểu thêm về **variable**, vui lòng tham khảo tại [Variable, Save Querying and View](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/dashboard/variable-save-querying-and-view). Ví dụ như ảnh bên dưới, chúng tôi chọn metric win\_swap.Percent\_Usage và chọn điều kiện lọc theo 2 dimension bao gồm: host = ThuyVT2-PC và objectname = Paging\_File. 

### 3. Alias

**Alias**: tên gợi nhớ dễ hiểu widget hơn. Nếu bạn không nhập Alias, chúng tôi tự động sinh ra tên query là **Statistic:metricname(dimension)**. Khi có thêm timeshift 5 phút thì Alias sẽ là **timeshift(statistic:metricname{dimension}, 5 minutes)**. Khi bạn có chọn group by thì Alias chỉ hiện thị dimension thôi, ví dụ bạn có một query với điều kiện group by cpu, thì Alias sẽ là cpu0, cpu1,...

### 4. Statistics

**Statistics**: phép toán để tổng hợp dữ liệu. Hệ thống vMonitor Platform lưu trữ một lượng lớn điểm dữ liệu và trong hầu hết các trường hợp đều không thể hiển thị tất cả chúng trên biểu đồ do đó chúng tôi sử dụng tính năng tổng hợp dữ liệu theo thời gian để giải quyết vấn đề này bằng cách kết hợp các điểm dữ liệu vào các nhóm thời gian, gọi là độ mịn dữ liệu. Độ mịn dữ liệu được chúng tôi tự động tính toán dựa trên time range mà bạn chọn, quy tắt tự động tính toán như bên dưới ( hoặc page). Có 5 cách tổng hợp mà bạn có thể sử dụng để kết hợp dữ liệu của mình trong mỗi nhóm thời gian: avg, count, max, min, sum được mô tả ở bảng bên dưới: 

|  |  |  |
| --- | --- | --- |
| **Phép toán** | **Ý nghĩa** | **Ví dụ minh họa** |
| avg | Giá trị trung bình của kết quả metric sinh ra. | - 01-01-2023 07:00:00 value = 1 <br> - 01-01-2023 07:00:30 value = 2 <br> - 01-01-2023 07:01:00 value = 1 <br> - 01-01-2023 07:01:30 value = 3 <br> - 01-01-2023 07:01:00 value = 1.5 <br> - 01-01-2023 07:02:00 value = 2 <br> Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới: Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán avg là: |
| count | Đếm số lượng kết quả metric sinh ra. | - 01-01-2023 07:00:00 value = 1 <br> - 01-01-2023 07:00:30 value = 2 <br> - 01-01-2023 07:01:00 value = 1 <br> - 01-01-2023 07:01:30 value = 3 <br> - 01-01-2023 07:01:00 value = 2 <br> - 01-01-2023 07:02:00 value = 2 <br> Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới: Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán count là: |
| max | Giá trị lớn nhất của kết quả metric sinh ra. | - 01-01-2023 07:00:00 value = 1 <br> - 01-01-2023 07:00:30 value = 2 <br> - 01-01-2023 07:01:00 value = 1 <br> - 01-01-2023 07:01:30 value = 3 <br> - 01-01-2023 07:01:00 value = 2 <br> - 01-01-2023 07:02:00 value = 3 <br> Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới: Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán max là: |
| min | Giá trị nhỏ nhất của kết quả metric sinh ra. | - 01-01-2023 07:00:00 value = 1 <br> - 01-01-2023 07:00:30 value = 2 <br> - 01-01-2023 07:01:00 value = 1 <br> - 01-01-2023 07:01:30 value = 3 <br> - 01-01-2023 07:01:00 value = 1 <br> - 01-01-2023 07:02:00 value = 1 <br> Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới: Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán min là: |
| sum | Tổng các giá trị của kết quả metric sinh ra. | - 01-01-2023 07:00:00 value = 1 <br> - 01-01-2023 07:00:30 value = 2 <br> - 01-01-2023 07:01:00 value = 1 <br> - 01-01-2023 07:01:30 value = 3 <br> - 01-01-2023 07:01:00 value = 3 <br> - 01-01-2023 07:02:00 value = 4 <br> Metric A mỗi 30s lại sinh ra 1 điểm dữ liệu như bên dưới: Nếu độ mịn dữ liệu được tự động tính toán khi hiển thị dữ liệu là 60s cho một điểm ,thì điểm dữ liệu trả về cho metric A này theo phép toán sum là: |

### 5. Group by

**Group by**: bạn có thể nhóm dữ liệu theo các dimension tương ứng của metric. 

### 6. Threshold method: 

**Threshold method**: đối với metric thì chúng tôi mặc định cung cấp cho bạn phương thức thiết lập ngưỡng là Tĩnh (Static). Tức là bạn có thể thiết lập một giá trị như là một ngưỡng cảnh báo.

### 7. Alarm condition

**Alarm condition:** điều kiện phép toán. Bạn có thể chọn 1 trong 4 giá trị bao gồm: Greater (> ngưỡng), Greater/Equal (>= ngưỡng), Lower/Equal (<= ngưỡng), Lower (< ngưỡng).

### 8. Threshold value

**Threshold value**: giá trị ngưỡng mà bạn muốn đặt cảnh báo. 

### 9. Check times

**Check times**: số lần kiểm tra liên tiếp trước khi chuyển trạng thái và cảnh báo.

### 10. Interval

**Interval**: khoảng thời gian mỗi lần hệ thống Alarm đánh giá dữ liệu 

Ví dụ ở đây chúng ta cần Alarm trên metric cpu.usage\_idle của host appserver, cứ 5p Alarm sẽ chạy đánh giá một lần, nếu CPU usage idle của host: appserver < 20%, hệ thống sẽ chuyển trạng thái và gửi cảnh báo. 
