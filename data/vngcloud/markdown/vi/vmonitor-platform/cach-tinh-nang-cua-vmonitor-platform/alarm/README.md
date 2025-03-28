# Alarm

### Tổng quan

Trong việc giám sát hệ thống, Alarm có thể được thiết lập để giám sát các metrics hoặc logs. Chúng có thể được cấu hình để kích hoạt cảnh báo và bắn notification cho người dùng khi các ngưỡng nhất định bị vi phạm, chẳng hạn như sử dụng CPU vượt quá 100% hoặc thời gian phản hồi của một hệ thống vượt quá giới hạn đã chỉ định. Alarm được sử dụng để cảnh báo cho các nhà điều hành hoặc quản trị viên về các vấn đề trong hệ thống. Từ đó họ có thể thực hiện hành động sửa chữa trước khi mọi thứ trở nên nghiêm trọng hơn và gây ra thiệt hại đáng kể.

Alarm được khuyến khích sử dụng để báo động khi bạn muốn giám sát các thành phần quan trọng của hệ thống hoặc ứng dụng của mình và đảm bảo rằng bạn được cảnh báo khi các vấn đề xảy ra. Alarm giúp bạn nhận biết và giải quyết vấn đề một cách chủ động,  giảm thiểu ảnh hưởng đến người dùng cuối. Việc thiết lập các ngưỡng báo động phù hợp là rất quan trọng vì nó có thể giúp bạn tránh khỏi báo động giả, điều này có thể làm xao nhãng và giảm hiệu quả của hệ thống giám sát.

Hiện tại vMonitor Platform hỗ trợ bạn thiết lập alarm cho 2 loại dữ liệu bao gồm: 

* Metric Alarm: cảnh báo dựa trên các thông số metric của bạn. Bạn sẽ nhận được cảnh báo khi điều kiện thiết lập vượt ngưỡng cho phép.
* Log Alarm: cảnh báo dựa trên dữ liệu log của bạn. Bạn sẽ nhận được cảnh báo khi điều kiện thiết lập vượt ngưỡng cho phép.

***

### Phạm vi giới hạn Alarm

Để có thể thiết lập một alarm, bạn phải đảm bảo đã thiết lập thành công Metric Agent hoặc Log Agent trên Server, đảm bảo dữ liệu metrics hoặc logs đã được đẩy về hệ thống vMonitor Platform. 

#### Quy tắc đặt tên Alarm

Các quy tắc sau áp dụng cho việc đặt tên Alarm trong vMonitor Platform:

* Tên Alarm phải dài từ 5 (tối thiểu) đến 50 (tối đa) ký tự.
* Tên Alarm chỉ có thể bao gồm các chữ cái viết hoa, viết thườ
* ng (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Tên Alarm phải bắt đầu bằng một chữ cái viết hoa, viết thường (a-z, A-Z) và kết thúc bởi một chữ cái viết hoa, viết thường (a-z, A-Z) hoặc một chữ số.
* Tên Alarm không nên chứa các thông tin nhạy cảm (ví dụ địa chỉ IP, tên tài khoản, mật khẩu đăng nhập,...). 
* Tên Alarm phải là duy nhất trong một tài khoản VNG Cloud cho đến khi Alarm đó bị xóa. 

#### Ví dụ minh họa

* Các tên Alarm ví dụ sau đây hợp lệ và tuân theo các nguyên tắc đặt tên được đề xuất:
  * Alarm\_email\_group1
  * Alarm\_80@sms
  * ...
* Các tên Alarm ví dụ sau đây hợp lệ nhưng chúng tôi không khuyến khích bạn sử dụng:
  * [docexamplewebsite.com](http://docexamplewebsite.com/)
  * 1.1.1.2
  * ...
* Các tên Alarm ví dụ sau không hợp lệ:
  * Report\_usage\_80\_% (chứa ký tự %)
  * Alarm\&Report (chứa ký tự &)
  * ...

***

### Khởi tạo Alarm

Mỗi Alarm **chỉ có thể chứa một loại cảnh báo được thiết lập trên dữ liệu metrics hoặc dữ liệu logs**. Để tạo Alarm, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Alarm.**
3. Chọn **Create an Alarm**.
4. Trong mục **Select an alarm type**, chọn **Metric** nếu bạn muốn thiết lập cảnh báo dựa trên dữ liệu metric hoặc chọn **Log** nếu bạn muốn thiết lập cảnh báo dựa trên dữ liệu log. 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(105).png?raw=true)

5\. Trong mục **Set alarm conditions**, làm theo hướng dẫn bên dưới nếu bạn muốn thiết lập Alarm cho metric hay log:

* [Metric Alarm](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/alarm/metric-alarm)
* [Log Alarm](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/alarm/log-alarm)

6\. Chọn **Next**.

7\. Trong mục **Actions**, bạn cần thiết lập điều kiện hệ thống sẽ thông báo đến đâu (Notification). Kết quả **Alarm** khi chạy sẽ bao gồm 3 trạng thái: 

* **In-alarm**: gửi cảnh báo tới nhóm người nhận khi kết quả alarm nằm ngoài ngưỡng đã xác định.
* **OK**: gửi cảnh báo tới nhóm người nhận khi kết quả alarm nằm trong ngưỡng đã xác định.
* **Undetermined**: gửi cảnh báo tới nhóm người nhận khi alarm vừa bắt đầu hoặc không có đủ dữ liệu để xác định. 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(106).png?raw=true)

**Ở mỗi trạng thái của alarm (In-alarm, OK, Undetermined), bạn có thể chọn một hoặc nhiều notification đã thiết lập tại** [_****Notification****_](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/notification)**. Một người nhận thông báo cũng có thể nhận cảnh báo cho alarm ở tất cả các trạng thái. Chúng tôi không giới hạn số lượng người nhận mà bạn có thể tạo tại notification cũng như số lượng người nhận mà bạn thiết lập trên alarm nhưng số lượng thông báo gửi đi qua các kênh sẽ phụ thuộc vào cấu hình gói metric quota, log project hay SMS notification quota, Email notification quota.**

8\. Chọn **Next.**

9\. Nhập **Alarm name**. Hãy nhập tên tuân thủ theo quy định của chúng tôi cho Alarm của bạn. Sau khi tạo Alarm, bạn có thể thay đổi tên cho Alarm của bạn. 

10\. Nhập **Alarm Description** nếu có. Mô tả alarm có thể dài từ 0 (tối thiểu) đến 255 (tối đa) ký tự. Mô tả Alarm có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.

11\. Chọn **Severity** của Alarm. Có 3 mức độ nghiêm trọng được chúng tôi định nghĩa bao gồm: **Thấp, Trung Bình, Cao**. Bạn hãy chọn 1 mức độ theo đánh giá cá nhân của bạn với cảnh báo.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(107).png?raw=true)

12\. Chọn **Create**.

13\. Sau khi bạn thiết lập xong một alarm, ban đầu alarm sẽ ở trạng thái: **Undertermine.** Tới lần đánh giá tiếp theo Alarm sẽ chuyển trạng thái tương ứng là **OK** hoặc **In-alarm**. Từ đó gửi cảnh báo theo điều kiện được thiết lập tương ứng. 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(108).png?raw=true)

14\. Cảnh báo được gửi và bạn có thể xem chi tiết **Alarm** bằng cách nhấn vô tên của **Alarm** tương ứng.

***

### Chỉnh sửa Alarm

Để chỉnh sửa Alarm, hãy làm theo hướng dẫn bên dưới: 

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **Alarm.**
3. Tại **Alarm** mà bạn muốn chỉnh sửa, chọn **Edit.**
4. Chỉnh sửa các thông số cho **Alarm** mà bạn mong muốn. Bạn không thể thay đổi thông tin trong mục Select an **alarm type** mà chỉ có thể chỉnh sửa các thông số alarm trong các mục: **Set alarm conditions, Configure actions, Add alarm description.** Việc chỉnh sửa này tương tự như khi bạn thực hiện tạo mới một Alarm theo hướng dẫn bên trên.
5. Chọn **Save.**

***

### Xóa Alarm

Khi bạn không có nhu cầu sử dụng một alarm nữa, bạn có thể thực hiện xóa alarm khỏi hệ thống theo hướng dẫn bên dưới: 

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/vmonitor](https://hcm-3.console.vngcloud.vn/vmonitor). Nếu bạn chưa có tài khoản, đăng ký miễn phí tại [tại đây](https://register.vngcloud.vn/signup).
2. Chọn thư mục **alarm.**
3. Tại **alarm** mà bạn muốn xóa, chọn **Checkbox Chọn.** Bạn có thể chọn một hoặc nhiều alarm để thực hiện xóa ở bước này.
4. Chọn **Delete**.
5. Tại màn hình xác nhận xóa alarm, chọn **Delete**.

**Sau khi bạn thực hiện xóa thành công thì alarm của bạn sẽ bị xóa hoàn toàn khỏi hệ thống của chúng tôi. Bạn không thể khôi phục lại alarm đã xóa nên hãy lưu ý cẩn thận khi sử dụng tính năng này.** 
