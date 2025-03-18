# Làm việc với bucket thông qua vStorage Portal

Bên dưới là các tính năng cơ bản khi bạn làm việc với bucket

## Khởi tạo bucket

Trước khi có thể lưu trữ dữ liệu trong vStorage, bạn phải tạo 1 Bucket. Trên vStorage, Bucket là đối tượng chứa dữ liệu (Object). 

Để khởi tạo một project, vui lòng thực hiện theo các bước bên dưới:

1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list). Chọn **project** muốn thực hiện tạo **bucket.**
2. Chọn **Create a bucket**.
3. Nhập **Bucket name** theo quy định của chúng tôi.
4. Chọn **Enable Object Locked** nếu bạn muốn sử dụng tính năng **Object locked** cho bucket này. 

> **Chú ý:**
>
> * Để sử dụng tính năng **Object locked** cho một bucket trên vStorage, khi khởi tạo bucket, bạn bắt buộc phải lựa chọn **Enable Object Locked**.
> * Khi bạn chọn **Enable Object Locked**, chúng tôi sẽ tự động bật tính năng **Object version** cho bucket của bạn.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(12)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

***

## Xem thông tin bucket

Sau khi tạo bucket và tải lên object vào bucket đó. Bạn có thể xem chi tiết thông tin bucket và sử dụng các tính năng mà chúng tôi cung cấp cho bucket bao gồm: ACLs, Lifecycle, CORS,... 

Để xem chi tiết thông tin của một bucket, bạn có thể: 

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn xem chi tiết.

3\. Chọn **bucket** bạn muốn xem chi tiết và chọn **View detail**.

4\. Trên trang hiển thị thông tin chi tiết **bucket**, bạn có thể xem và sử dụng các tính năng mà chúng tôi cung cấp cho bucket bao gồm:

* **Thông tin chung**: Cung cấp các thông tin chung của bucket như Name, Owner, Created date, Versioning, Encryption, Object Lock.
* **ACLs**: Cung cấp thông tin quản lý truy cập Read/Write/Read+Write của một hay nhiều tài khoản Root đang có trên hệ thống được cấp phép truy cập trên bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại [Sử dụng tính năng ACLs](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/object-storage-hcm04/cac-tinh-nang-cua-object-storage/lam-viec-voi-bucket/lam-viec-voi-bucket-thong-qua-vstorage-portal/su-dung-tinh-nang-acls).
* **CORS**: Cung cấp thông tin các đường dẫn được phép truy cập vào tài nguyên của bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại [Sử dụng tính năng CORS.](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/object-storage-hcm04/cac-tinh-nang-cua-object-storage/lam-viec-voi-bucket/lam-viec-voi-bucket-thong-qua-vstorage-portal/su-dung-tinh-nang-cors)
* **Lifecycle**: Cung cấp thông tin các lifecycle được thiết lập cho bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại[ Sử dụng tính năng lifecycle.](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/object-storage-hcm04/cac-tinh-nang-cua-object-storage/lam-viec-voi-bucket/lam-viec-voi-bucket-thong-qua-vstorage-portal/su-dung-tinh-nang-lifecycle)
* **Event notification**: Cung cấp thông tin các event notification được thiết lập cho bucket. Để biết chi tiết cách sử dụng tính năng, hãy xem tại [Sử dụng tính năng Event notification.](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/object-storage-hcm04/cac-tinh-nang-cua-object-storage/lam-viec-voi-bucket/lam-viec-voi-bucket-thong-qua-vstorage-portal/su-dung-tinh-nang-event-notification)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(798).png?raw=true)

***

## Sử dụng tính năng Bucket encryption

**SSE-S3 (Server-Side Encryption with S3 Managed Keys)** là tính năng mã hóa dữ liệu phía máy chủ do Amazon S3 cung cấp. Với SSE-S3, dữ liệu của bạn được mã hóa tự động khi được tải lên S3 và được giải mã tự động khi bạn tải xuống.

Để sử dụng tính năng Bucket encryption, vui lòng thực hiện theo các bước bên dưới:

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** chứa **bucket** bạn muốn thiết lập encryption.

3\. Chọn biểu tượng **Action** và chọn **Configure encryption**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(799).png?raw=true)

4\. Trên trang xác nhận sử dụng encryption SSE-S3, vui lòng chọn **Enable ecryption.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(9)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

***

## Xóa bucket

Để xóa một bucket, vui lòng thực hiện theo các bước bên dưới:

1\. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).

2\. Chọn **project** và chọn **bucket** bạn muốn thực hiện xóa.

3\. Chọn biểu tượng **Action** và chọn **Delete**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(800).png?raw=true)

Sau khi chọn Xóa, hệ thống sẽ tự động chuyển ra màn hình chính, nếu bạn thấy bucket vừa thực hiện biến mất khỏi danh sách thì bạn đã xoá thành công. Bucket lúc này đã được xóa vĩnh viễn khỏi hệ thống và bạn không thể khôi phục bucket cũng như các object được lưu trữ trong bucket. Vì vậy hãy đảm bảo kiểm tra dữ liệu của bạn trước khi thực hiện thao tác này. 
