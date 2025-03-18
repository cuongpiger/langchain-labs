# Làm việc với S3 Keys

## **Tổng quan**

Trên hệ thống vStorage, S3 key là cặp key bao gồm access key và secret key được vStorage tích hợp và tương thích với các client tool của S3 như s3cmd, s3 SDK,...

***

## Root User Account khởi tạo S3 keys

Để khởi tạo S3 key, làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list) với tài khoản **Root User Account**.
2. Chọn **Region HCM04.**
3. Chọn biểu tượng  <img src="../../../../.gitbook/assets/image (581).png" alt="" data-size="line"> tại project mà bạn vừa khởi tạo sau đó chọn mục **Identity and Access Management.**
4. Tại mục **List of S3 keys of this project**, chọn **Generate S3 key**.
5. Chọn **Copy** hoặc **Download** để tải xuống thông tin Access Key/Secret Key mà bạn vừa khởi tạo.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(18)%20(1).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(19)%20(1).png?raw=true)

> **Chú ý:**
>
> * Sau khi nhấn tạo S3 key, bạn cần **lưu lại cặp Access Key/Secret Key** để sử dụng, nếu bạn không lưu trữ ngay lúc này thì sau đó không thể lấy được Secret Key của Access Key này.
> * **S3 key được khởi tạo bởi** ********Root User Account**** ******sẽ có toàn quyền truy cập/ thao tác trên các bucket thuộc project này.**

***

## IAM User Account khởi tạo S3 keys

Để khởi tạo S3 key, làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list) với tài khoản **IAM User Account**.
2. Chọn **Region HCM04.**
3. Chọn biểu tượng  <img src="../../../../.gitbook/assets/image (581).png" alt="" data-size="line"> tại project mà bạn vừa khởi tạo sau đó chọn mục **Identity and Access Management.**
4. Tại mục **List of S3 keys of this project**, chọn **Generate S3 key**.
5. Chọn **Copy** hoặc **Download** để tải xuống thông tin Access Key/Secret Key mà bạn vừa khởi tạo.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(20)%20(1).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(21)%20(1).png?raw=true)

> **Chú ý:**
>
> * Sau khi nhấn tạo S3 key, bạn cần **lưu lại cặp Access Key/Secret Key** để sử dụng, nếu bạn không lưu trữ ngay lúc này thì sau đó không thể lấy được Secret Key của Access Key này.
> * **S3 key được khởi tạo bởi** ********IAM User Account**** ******sẽ có toàn quyền truy cập/ thao tác trên các bucket/object theo quyền hạn của IAM User Account đó. Ví dụ, nếu IAM User Account của bạn chỉ có quyền Read Object thì S3 keys tạo bởi IAM User Account này cũng chỉ có quyền Read Object.**

***

## Thực hiện làm việc với S3 API (hoặc 3rd party software) thông qua S3 keys

### Kết nối 3rd party softwares với vStorage

Sau khi bạn đã thực hiện khởi tạo project và khởi tạo S3 key thành công, lúc này bạn có thể sử dụng các 3rd party softwares để kết nối và làm việc với project của bạn. Các công cụ 3rd party softwares bạn có thể lựa chọn sử dụng có thể là S3cmd, Cyberduck, Rclone, S3 Browser, MinIO Client,...Trong phạm vi tài liệu này, chúng tôi sẽ hướng dẫn bạn kết nối S3 Browser với vStorage. S3 Browser là công cụ được tối ưu hóa cho phép bạn chia sẻ và tải lên tệp tin của mình. Công cụ này có giao diện tương đối đơn giản, dễ sử dụng và đã tương thích với API của dịch vụ lưu trữ vStorage. 

Để tích hợp công cụ S3 Browser với vStorage, bạn có thể thực hiện theo hướng dẫn bên dưới:

1. Tải công cụ người dùng S3 Browser tại đây [https://s3browser.com/download.aspx](https://s3browser.com/download.aspx).
2. Mở ứng dụng **S3 Browser.** Chọn thư mục **Account, sau đó chọn Add new account**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(585).png?raw=true)



3. Màn hình Add New Account hiển thị, lúc này bạn nhập các thông tin như sau:

* **Display name:** Tên hiển thị của account. Ví dụ: Demo\_HCM04
* **Account type**: Chọn **S3 Compatible Storage.**
* **REST Endpoint**: Đường dẫn đến vstorage, đối với Region HCM04 thì đường dẫn là [hcm04.vstorage.vngcloud.vn](http://hcm01.vstorage.vngcloud.vn/)
* **Access Key ID & Secret Access Key:** Là cặp S3 key bạn đã thực hiện generate tại bước 2 trước đó.

4. Chọn option **Use Secure transfer (SSL/TLS)** vì vStorage chỉ hỗ trợ kênh truyền đã được mã hoá (HTTPS, port 443) để đảm bảo an toàn dữ liệu, vStorage hiện tại không hỗ trợ kênh truyền không mã hoá (HTTP, port 80).
5. Chọn **Add new account.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(587).png?raw=true)

6. Khi kết nối thành công, màn hình S3 Browser sẽ hiển thị như sau: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(588).png?raw=true)

### Sử dụng 3rd party softwares để thực hiện các tính năng trên vStorage

#### Các usecase cơ bản

Bên dưới là hướng dẫn cho một số use case thông thường bạn có thể thực hiện trên S3 Browser:

**Tạo / Xóa bucket**

* Thực hiện tạo xóa bucket bằng cách chọn nút **New bucket**, lúc này bạn thực hiện nhập **Bucket name** và chọn **Create new bucket.**

**Upload / Download file**

* Sau khi đã tạo bucket, bạn chọn vào bucket cần tải file lên/ xuống. Tiếp theo, bạn chọn **Upload/ Download** tùy theo nhu cầu tải lên/ xuống của bạn.

**Tạo / Xóa Folder**

* Bạn cũng có thể tạo/ xóa folder bằng cách chọn **New Folder** hoặc **Delete**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(589).png?raw=true)

#### Các usecase nâng cao

Tiếp theo đây là các hướng dẫn cho các tính năng nâng cao bạn có thể thực hiện trên S3 Browser:

**ACL**

**ACL** là tính năng trên S3 cho phép bạn kiểm soát quyền truy cập cho từng object trong bucket S3 của bạn. Tính năng này sẽ xác định người dùng hoặc nhóm người dùng nào có thể truy cập object và các thao tác họ có thể thực hiện, chẳng hạn như tải xuống, tải lên, xóa hoặc ghi đè object.

Để thiết lập ACL cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn Edit Permission (ACL) . Trong phần permission, hãy check chọn quyền hạn bạn mong muốn cấp cho người dùng. Chi tiết tham khảo thêm tại [https://s3browser.com/share-s3-bucket-edit-acls.aspx](https://s3browser.com/share-s3-bucket-edit-acls.aspx)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(590).png?raw=true)

**SSE-S3**

SSE-S3 (Server-Side Encryption with S3 Managed Keys) là tính năng mã hóa dữ liệu phía máy chủ do Amazon S3 cung cấp. Với SSE-S3, dữ liệu của bạn được mã hóa tự động khi được tải lên S3 và được giải mã tự động khi bạn tải xuống. **Để thực hiện được tính năng này trên S3 Browser, bạn cần sử dụng S3 Browser phiên bản Pro. Nếu ứng dụng của bạn hiện không hỗ trợ cho việc thực hiện tính năng, vui lòng gửi yêu cầu sử dụng tính năng thông qua ticket tới VNGCloud.** Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-server-side-encryption.aspx](https://s3browser.com/amazon-s3-server-side-encryption.aspx)

**SSE-C**

**SSE-C** (Server-Side Encryption with Customer-Provided Keys) là tính năng mã hóa dữ liệu phía máy chủ do Amazon S3 cung cấp. Giống như SSE-S3, SSE-C mã hóa dữ liệu của bạn tự động khi được tải lên S3 và giải mã tự động khi bạn tải xuống. Tuy nhiên, với SSE-C, bạn cung cấp và quản lý khóa mã hóa của riêng mình, thay vì sử dụng khóa do AWS quản lý. **Để thực hiện được tính năng này trên S3 Browser, bạn cần sử dụng S3 Browser phiên bản Pro. Nếu ứng dụng của bạn hiện không hỗ trợ cho việc thực hiện tính năng, vui lòng gửi yêu cầu sử dụng tính năng thông qua ticket tới VNGCloud.** Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-server-side-encryption.aspx](https://s3browser.com/amazon-s3-server-side-encryption.aspx)

**Object Locked**

**Object Lock** là tính năng giúp bảo vệ dữ liệu của bạn khỏi bị xóa hoặc ghi đè trong một khoảng thời gian cố định hoặc vô thời hạn. Tính năng này sử dụng model **WORM** (Write Once, Read Many), nghĩa là sau khi một object được tải lên S3 và được locked, object đó không thể bị xóa hoặc thay đổi bởi bất kỳ ai, kể cả người dùng root.

Để thiết lập Object Locked cho một bucket bằng S3 Browser, khi khởi tạo một bucket mới, bạn cần chọn phương án **Enable S3 Objected Lock.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(623).png?raw=true)

Tiếp theo, khi bucket được tạo thành công, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Object Locked**. Bạn có thể thiết lập object locked ở cả 2 mode **Retention** và **Legal Hold** thông qua S3 Browser. Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-object-lock.aspx](https://s3browser.com/amazon-s3-object-lock.aspx)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(592).png?raw=true)

**Versioning**

Versioning là một tính năng hỗ trợ lưu trữ nhiều phiên bản quá khứ của các object được lưu trữ trong một bucket. Bạn có thể sử dụng tính năng versioning để lưu giữ, truy xuất và khôi phục mọi phiên bản của object được lưu trữ trong bucket của bạn. Khi bật tính năng Versioning, khi thực hiện tải lên/ xóa một object thì thay vì xóa hẳn object khỏi hệ thống, chúng tôi sẽ chuyển các object bị xóa hoặc bị ghi đè sang phiên bản versioning. Từ đó bạn có thể dễ dàng khôi phục lại các object bị xóa nhầm hoặc tải về các phiên bản cũ của dữ liệu khi có nhu cầu sử dụng.

Để thiết lập Versioning cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Edit Versioning Settings**. Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-versioning.aspx](https://s3browser.com/amazon-s3-versioning.aspx)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(594).png?raw=true)

**Lifecycle rotation**

**Lifecycle rotation** là một tính năng quản lý vòng đời của các đối tượng (objects) trong một bucket. Tính năng này cho phép bạn tự động hóa các hành động như xóa các đối tượng sau một khoảng thời gian nhất định.

Để thiết lập Lifecycle rotation cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Lifecycle Configuration**. Chi tiết tham khảo thêm tại [https://s3browser.com/bucket-lifecycle-configuration.aspx](https://s3browser.com/bucket-lifecycle-configuration.aspx)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(595).png?raw=true)

**Lifecycle transit**

Hiện tại trên region HCM04 chúng tôi chỉ hỗ trợ bạn tạo Project với Storage Class **Instant Archive Type**. Do chỉ có 1 storage class duy nhất nên hiện tại tính năng Lifecycle transit sẽ không hoạt động.

**CORS**

CORS (Cross-Origin Resource Sharing) là cơ chế bảo mật cho phép các trang web được lưu trữ trên một tên miền truy cập tài nguyên từ tên miền khác. Khi bạn sử dụng S3 để lưu trữ nội dung tĩnh và muốn truy cập nội dung đó từ trang web được lưu trữ trên tên miền khác, bạn cần cấu hình CORS cho bucket S3 của mình.

Để thiết lập CORS cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **CORS Configuration**. Chi tiết tham khảo thêm tại [https://s3browser.com/s3-bucket-cors-configuration.aspx](https://s3browser.com/s3-bucket-cors-configuration.aspx)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(596).png?raw=true)

**Public/ Private bucket**

**Public bucket** là tính năng cho phép người dùng chia sẻ công khai bucket trên môi trường điện toán đám mây. Người dùng từ ngoài internet có thể truy cập vào bucket thông qua đường dẫn URL mà không cần chứng thực quyền truy cập với hệ thống. Quyền truy cập công khai tiềm ẩn rủi ro bảo mật, vì vậy nếu kịch bản của bạn không yêu cầu quyền truy cập đó, chúng tôi khuyên bạn không nên cho phép quyền truy cập công khai đối với bucket. Tại bất kỳ thời điểm nào bạn không muốn công khai bucketđó nữa thì có thể chuyển chế độ riêng tư cho bucket.

Để thiết lập chế độ công khai cho một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Public Access block Configuration**. Chi tiết tham khảo thêm tại [https://s3browser.com/amazon-s3-public-access-block-configuration.aspx](https://s3browser.com/amazon-s3-public-access-block-configuration.aspx)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(597).png?raw=true)

**Bucket policy**

**Bucket Policy** là một loại chính sách truy cập được sử dụng để kiểm soát quyền truy cập vào một bucket S3 cụ thể. Nó cho phép bạn xác định người dùng hoặc nhóm nào có thể truy cập bucket và các thao tác họ có thể thực hiện, chẳng hạn như tải lên, tải xuống, xóa hoặc liệt kê các object trong bucket.

Để thiết lập policy một bucket bằng S3 Browser, bạn hãy nhấn chuột phải vào bucket, sau đó chọn **Edit Bucket Policy**. Chi tiết tham khảo thêm tại [https://s3browser.com/working-with-amazon-s3-bucket-policies.aspx?v=11.7.5\&fam=x64#amazon-s3-bucket-policies-examples](https://s3browser.com/working-with-amazon-s3-bucket-policies.aspx?v=11.7.5\&fam=x64#amazon-s3-bucket-policies-examples)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(598).png?raw=true)

***

## Xóa S3 keys

Để hủy (xóa) một hay nhiều S3 key đã tạo trước đó, hãy làm theo hướng dẫn bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list) với tài khoản **Root User Account** hoặc tài khoản **IAM User Account**.
2. họn **Region HCM04.**
3. Chọn biểu tượng  <img src="../../../../.gitbook/assets/image (581).png" alt="" data-size="line"> tại project mà bạn vừa khởi tạo sau đó chọn mục **Identity and Access Management.**
4. Tại mục **List of S3 keys of this project**, chọn **S3 key** mà bạn muốn xóa sau đó chọn **Delete.**

Kể từ thời điểm S3 key bị hủy thành công, bạn sẽ không thể sử dụng S3 key này để truy xuất vào vStorage. Hãy thận trọng khi thực hiện thao tác hủy (xóa) tài khoản S3 bởi bạn sẽ không thể khôi phục tài khoản đã xóa này.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(22)%20(1).png?raw=true)
