# Sử dụng tính năng ACLs

## **Tổng quan**

**Access Control List (ACL)** trên vStorage là một tính năng cho phép quản lý quyền truy cập vào bucket và các object bên trong bucket. ACL cung cấp các cấp độ truy cập cơ bản mà bạn có thể thiết lập cho người dùng Root user account khác trên vStorage. Dưới đây là hướng dẫn cơ bản để sử dụng tính năng ACLs:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn biểu tượng <img src="../../../../../../.gitbook/assets/image (7) (1) (1).png" alt="" data-size="line">tại **project** chứa **bucket** bạn muốn phân quyền.
3. Nếu bạn muốn phân quyền bucket cho một **Root User Account** hoặc **IAM User Account** hay **Service Account** khác, bạn cần biết thông tin **vStorage User ID** của người dùng mà bạn muốn phân quyền: 
   1. Đối với **Root User Account**: bạn có thể lấy thông tin **vStorage User ID** ngay tại trang thông tin **project** theo hình dưới.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(867).png?raw=true)

b. Đối với **IAM User Account** và **Service Account**: bạn có thể lấy thông tin **vStorage User ID** tại mục  **Identity and Access Management**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(8)%20(1)%20(1).png?raw=true)

4. Tiếp tục chọn **Bucket** bạn muốn thực hiện thiết lập ACLs.
5. Chọn biểu tượng **Action** và chọn **Set ACLs.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

6. Tại đây, bạn có thể lựa chọn tập người dùng và quyền truy cập tương ứng. Cụ thể: 

* **Các tập người dùng trong ACL:** ACL cho phép thiết lập quyền truy cập cho các kiểu người dùng sau:
  * **Bucket owner**: Người sở hữu bucket.
  * ****Everyone (Public Access)******: Tất cả người dùng, người dùng bất kỳ có thể truy cập tài nguyên mà không cần authenticated.**
  * **Authenticated users:** Tất cả người dùng trên hệ thống vStorage HCM04.
  * **Other accounts**: Người dùng có vStorage User ID cụ thể mới được phép truy cập vào tài nguyên. Bạn có thể xem thông tin vStorage User ID theo hướng dẫn tại đây.
* Các quyền có thể cấp:

| Quyền | Bucket ACLs | Object ACLs |
| --- | --- | --- |
| `READ` | - `ListObjects` : Người dùng có thể xem danh sách tất cả objects thuộc bucket. | - `ReadObject` : Người dùng có thể xem thông tin chi tiết một object (object's data and object's metadata) |
| `WRITE` | - `WriteObjects` : Người dùng có thể tải objects lên bucket. | - Không hỗ trợ |
| `READ + WRITE` | - `ListObjects`  +  `WriteObjects` : Người dùng có thể xem danh sách objects thuộc bucket và tải object lên bucket này. | - `ReadObject` : Người dùng có thể xem thông tin chi tiết một object (object's data and object's metadata) |

* **Ngoài ra, các quyền ReadBucketACL, WriteBucketACL, ReadObjectACL, WriteObjectACL:** Cho phép người dùng có thể xem thông tin/ cập nhật cấu hình ACLs của bucket hoặc object.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

7. Chọn **Update** để lưu lại cấu hình đã thiết lập cho ACLs.

***

## Ví dụ minh họa

### **Ví dụ 1: Cấp quyền ListObject cho tất cả mọi người (Public-Read)**

* Chọn **Everyone (public access)** trong phần **Access control list**.
* Chọn action **List** để cấp quyền liệt kê danh sách object thuộc bucket cho tất cả người dùng.
* Chọn **Save**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

### **Ví dụ 2: Cấp quyền FULL\_CONTROL cho một tài khoản vStorage khác**

> Chú ý: 
>
> * Để cấp quyền truy cập vào resource cho một tài khoản vStorage khác, bạn cần biết thông tin vStorage User ID của người dùng mà bạn muốn chia sẻ quyền truy cập. Bạn có thể xem thông tin vStorage User ID theo hướng dẫn tại đây.

* Trong **Other accounts**, nhập **vStorage User ID** của tài khoản mà bạn muốn cấp quyền.
* Chọn action **List, Write** để cấp quyền liệt kê danh sách object thuộc bucket và tải object lên bucket này.
* Chọn **Save**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Như hình bên trên, tôi đã phân quyền làm việc trên `bucket001` cho người dùng `vngclouddemo-123456`. Lúc này, người dùng `vngclouddemo-123456` có thể sử dụng tính năng `Add external bucket` để thêm bucket được chia sẻ này và danh sách bucket của bạn: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

> **Chú ý:**
>
> * **Kiểm soát quyền công khai (Everyone)**: Chỉ nên sử dụng quyền public khi cần thiết vì ACL có thể dẫn đến việc tiết lộ dữ liệu không mong muốn. Nếu bạn muốn quản lý quyền truy cập chi tiết, thì nên dùng **Bucket Policy** thay vì **ACL** công khai. Sử dụng Bucket Policy cho phép bạn chỉ định điều kiện truy cập chi tiết hơn, ví dụ như **giới hạn IP**, **yêu cầu xác thực**, hoặc các điều kiện bảo mật cụ thể.
> * **Kết hợp với Bucket Policy**: ACL có thể được dùng song song với Bucket Policy, nhưng cần chú ý để tránh xung đột trong việc cấp quyền. Ví dụ: Nếu ACL cho phép mọi người có thể ListObjects trong bucket, nhưng Bucket Policy lại từ chối truy cập từ các nguồn public, thì người dùng sẽ không thể truy cập object công khai.
> * **Giới hạn của ACL**: ACL không hỗ trợ điều kiện phức tạp như Bucket Policy, nên chỉ thích hợp cho các tình huống cấp quyền đơn giản. Khi bạn cần kiểm soát phức tạp hơn, hãy xem xét kết hợp với Bucket Policy.
