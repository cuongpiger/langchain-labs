# Quản lý truy cập

Trên region HCM04, bạn có thể sử dụng 4 loại tài khoản để truy cập vào vStorage. Chi tiết 4 loại này bao gồm:

* **Root User Account:** Là tài khoản [khởi tạo đầu tiên](https://register.vngcloud.vn/signup) để truy cập vào VNG Cloud với đầy đủ quyền truy cập vào tất cả dịch vụ tài nguyên trên VNG Cloud.
* **IAM User Account, Service Account:** Là tài khoản được tạo ra từ tài khoản Root user account duy nhất với những quyền truy cập phụ thuộc vào chính sách cho phép truy cập được thiết lập từ Root user account. 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(864).png?raw=true)

* **S3 keys:** Là cặp s3 key có access key và secret key được vStorage tích hợp để có tính tương thích với các client tool của S3 như s3cmd, s3 SDK,...

Tham khảo bảng bên dưới để nắm được cách hoạt động tổng quan của các tài khoản trên vStorage: 

| Loại tài khoản | Kênh truy cập | Nơi khởi tạo | Quyền hạn mặc định | Làm việc với project | Làm việc với bucket |
| --- | --- | --- | --- | --- | --- |
| Root User Account | vStorage Portal | Khởi tạo lần đầu khi sử dụng dịch vụ trên VNG Cloud | Full quyền trên project và bucket | Có | Có |
| IAM User Account | vStorage Portal | IAM Portal | Chưa có quyền hạn truy cập vào bất kỳ tài nguyên nào | Có, phân quyền thông qua IAM Policy | Có, phân quyền thông qua Bucket Policy |
| Service Account | vStorage API | IAM Portal | Chưa có quyền hạn truy cập vào bất kỳ tài nguyên nào | Có, phân quyền thông qua IAM Policy | Có, phân quyền thông qua Bucket Policy |
| S3 keys | 3rd party software | vStorage Portal | Tùy thuộc vào tài khoản khởi tạo | Không | Có, quyền hạn tùy thuộc vào loại user khởi tạo S3 key |
