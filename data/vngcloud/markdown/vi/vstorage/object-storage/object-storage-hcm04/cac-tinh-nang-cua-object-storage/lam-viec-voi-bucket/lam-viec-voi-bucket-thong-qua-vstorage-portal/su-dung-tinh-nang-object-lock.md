# Sử dụng tính năng Object lock

**Object Lock** là tính năng giúp bảo vệ dữ liệu của bạn khỏi bị xóa hoặc ghi đè trong một khoảng thời gian cố định hoặc vô thời hạn. Tính năng này sử dụng model **WORM** (Write Once, Read Many), nghĩa là sau khi một object được tải lên S3 và được locked, object đó không thể bị xóa hoặc thay đổi bởi bất kỳ ai, kể cả người dùng root. Hiện tại, trên region HCM04, chúng tôi đã hỗ trợ bạn thiết lập Object Locked ở 2 mode Compliance, Legal Hold và ****chưa hỗ trợ mode Governance******.** Nếu bạn sử dụng 3rd party software để thiết lập Object Locked ở mode Governance này thì S3 key được tạo ra sẽ có full quyền xóa các object version trên bucket của bạn. Ý nghĩa các mode locked được mô tả bên dưới: 

* **Retention mode**: ngăn chặn việc xóa và ghi đè object version trong một khoảng thời gian nhất định. Trong Retention period sẽ có 2 mode:
  * **Compliance mode (đã hỗ trợ)**: bất kỳ người dùng hoặc admin,…nào cũng không thể ghi đè object version được locked. Khi hết thời gian được thiết lập trước, người dùng có thể thực hiện xóa hoặc ghi đè object bình thường.
  * **Governance mode (coming soon)**: chỉ những người dùng có quyền đặc biệt (có quyền ByPassGovernance), chẳng hạn như người dùng root hoặc S3 Key không bật Restriction by IAM mới có thể xóa hoặc ghi đè object.
* **Legal Hold:** ngăn chặn việc xóa và ghi đè object version vô thời hạn tới khi nào người dùng disable. Mode này hoạt động độc lập với Retention period. Người dùng có quyền PutObjectLegalHold có thể thực hiện thêm hoặc remove legal hold cho object.

Để thiết lập Object Locked cho một bucket bằng S3 Browser, khi khởi tạo một bucket mới, bạn cần chọn phương án **Enable S3 Objected Lock. ******Hãy nhớ rằng bạn sẽ không thể bật Object Lock cho bucket đã tồn tại.****

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(14)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

Sau khi bucket đã được tạo thành công, để cấu hình thông số cụ thể cho tính năng object lock, vui lòng làm theo các bước bên dưới: 

## Compliance Mode

Sau khi đã bật Object Lock cho bucket, bạn có thể thiết lập Object Lock cho bucket theo các bước sau: 

1\. Tại bucket cần thiết lập object lock, chọn **Action** và chọn **Configure object lock retention**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(802).png?raw=true)

2\. Tại màn hình Configure object lock retention, chọn **Enable Object Lock retention policy**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(803).png?raw=true)

3\. Tại mục **Retention Mode**: hiện tại chúng tôi chỉ hỗ trợ **Compliance Mode** (mode này sẽ bảo vệ object version đối với việc thay đổi hay xóa cho đến khi hết thời gian giữ).

4\. Tại mục **Retention Period**: bạn hãy chọn thời gian mong muốn giữ cho các object thuộc bucket của bạn. Ví dụ bạn chọn 30 ngày, 60 ngày, 1000 ngày,...

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(804).png?raw=true)

5\. Chọn **Update.**

5\. Bây giờ, bạn hãy tải lên các object của bạn. Tất cả các object được tải lên bây giờ sẽ được giữ trong Retention period mà bạn đã chọn. Trong khoảng thời gian này, không một ai có quyền xóa object của bạn.

Ví dụ: hình bên trên, tôi cấu hình giữ 60 ngày, 

* Nếu ngày tôi tải lên object là 25/10/2024. Như vậy, object này sẽ được giữ tới **25/10/2024 + 60 ngày = 24/12/2024**
* Nếu ngày tôi tải lên object là 01/11/2024. Như vậy, object này sẽ được giữ tới **25/10/2024 + 60 ngày = 31/12/2024**

***

## Governance Mode

* ****Hiện tại, chúng tôi chưa hỗ trợ mode Governance******.** Nếu bạn sử dụng 3rd party software để thiết lập Object Locked ở mode Governance này thì S3 key được tạo ra sẽ có full quyền xóa các object version trên bucket của bạn. 

***

## **Legal Hold**

Tính năng **Object Legal Hold** trên vStorage cho phép bạn giữ một version của object không bị xóa hoặc ghi đè. Khi tính năng này được bật, bất kỳ ai, kể cả Root User Account, đều không thể xóa hoặc chỉnh sửa object đó cho đến khi legal hold được tắt.

Sau khi đã bật Object Lock cho bucket, bạn có thể thiết lập Object Lock loại **Legal Hold** cho từng object trong bucket theo các bước sau: 

1\. Tại object cần thiết lập object lock, chọn **Action** và chọn **Enable object legal hold**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(805).png?raw=true)

2\. Tại màn hình Enable object legal hold, chọn **Enable**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(806).png?raw=true)

> **Chú ý:**
>
> * Legal hold chỉ áp dụng cho từng version của object, nên nếu bật cho một version cụ thể, các version khác vẫn có thể bị chỉnh sửa hoặc xóa.
> * Tính năng này khác với **Retention Policy** vì chỉ dừng việc xóa hoặc chỉnh sửa object chứ không có thời gian kết thúc.

