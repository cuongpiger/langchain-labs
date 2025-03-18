# Quản lý truy cập tài nguyên vStorage

#### Tổng quan  

Để truy cập và làm việc được với các tài nguyên của dịch vụ vStorage, bạn cần phải:

1. Có tài khoản được cấp bởi dịch vụ vStorage (tài khoản vStorage).
2. Phân quyền truy cập và làm việc với các tài nguyên cho tài khoản vStorage.
3. Truy cập và làm việc với các tài nguyên vStorage sử dụng tài khoản vStorage.

#### Tài khoản vStorage 

Nếu bạn chưa có tài khoản vStorage, bạn vui lòng tham khảo [Quản lý tài khoản truy cập](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage) để biết về các loại tài khoản được hỗ trợ bởi dịch vụ vStorage cũng như cách thức cấp phát các loại tài khoản này.

#### Phân quyền truy cập và làm việc với các tài nguyên cho tài khoản vStorage 

Khi bạn tạo một container thuộc các project để lưu trữ dữ liệu trên vStorage, bạn nên kiểm soát ai có quyền truy cập vào các container và object của bạn cũng như các quyền truy cập mà họ nên có. Bên cạnh đó bạn nên quyết định xem bạn muốn áp dụng phân quyền truy cập bằng việc sử dụng các tính năng phân quyền riêng lẻ trên vStorage hoặc sử dụng tính năng phân quyền truy cập thống nhất thông qua hệ thống Quản lý danh tính và truy cập (vIAM).

* **Phân quyền truy cập và làm việc với các tài nguyên thông qua vStorage**: Tùy chọn sử dụng các tính năng Chuyển chế độ công khai container, Chuyển chế độ riêng tư container, Phân quyền truy cập ACLs container, Chia sẻ tài nguyên CORS container, Chia sẻ object,... để phân quyền truy cập tới từng container/ object. Khi sử dụng các tính năng này, bạn có thể chỉ định quyền truy cập và áp dụng quyền cho cấp độ container và object riêng lẻ tùy theo tính năng.
* **Phân quyền truy cập và làm việc với các tài nguyên thông qua vIAM**: Tùy chọn sử dụng hệ thống Quản lý danh tính và truy cập (vIAM) để phân quyền truy cập. vIAM phân quyền truy cập đồng thời cho tất cả các object có trong một container, các container có trong project hoặc nhóm object, container có tiền tố tên chung.

Bạn cũng có thể sử dụng đồng thời hai cơ chế phân quyền bên trên để phân quyền truy cập tới tài nguyên (container, object). Ví dụ: nếu policy vIAM của bạn chỉ cho phép một số người dùng đọc dữ liệu một số object trong container, nhưng container lại được công khai truy cập qua tính năng Make public trên vStorage, thì tất cả các object thuộc container đó sẽ được hiển thị công khai.

Nếu bạn sử dụng đồng thời hai cơ chế phân quyền đề cập ở trên để phân quyền truy cập đến tài nguyên (container, object) thì các thiết lập phân quyền truy cập thông qua vStorage sẽ có độ ưu tiên cao hơn các thiết lập phân quyền truy cập thông qua vIAM. Việc sử dụng hai cơ chế phân quyền đồng thời gây sự nhập nhằng, không rõ ràng trong quản lý quyền truy cập tài nguyên, qua đó gây ra nhiều rủi ro liên quan đến việc rò rỉ (leak) quyền. Do đó, chúng tôi khuyến khích bạn chỉ nên sử dụng một trong hai cơ chế phân quyền trên cho một đối tượng tài nguyên để tránh các rủi ro liên quan đến bảo mật tài nguyên.

Khi cấp quyền truy cập tới tài nguyên lưu trữ trên vStorage, bạn quyết định ai sẽ nhận quyền, họ sẽ nhận quyền đối với tài nguyên lưu trữ nào và các hành động cụ thể mà bạn muốn cho phép đối với những tài nguyên đó. Các phần sau đây cung cấp thông tin tổng quan về tài nguyên vStorage và cách xác định phương pháp tốt nhất để kiểm soát quyền truy cập tới chúng.

Chi tiết về cách thức phân quyền truy cập và làm việc với các tài nguyên vStorage, vui lòng xem các chủ đề bên dưới:

* [Phân quyền truy cập và làm việc thông qua vStorage](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/phan-quyen-truy-cap-va-lam-viec-thong-qua-vstorage)
* [Phân quyền truy cập và làm việc thông qua IAM](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/phan-quyen-truy-cap-va-lam-viec-thong-qua-iam)

#### Truy cập và làm việc với các tài nguyên vStorage sử dụng tài khoản vStorage 

Để truy cập tài nguyên (project, container, object, report, v.v.) của bạn trên dịch vụ lưu trữ vStorage, bạn có thể sử dụng các tài khoản vStorage bao gồm tài khoản người dùng Root (Root User Account), tài khoản người dùng IAM (IAM User Account) và tài khoản Service Account để truy cập tài nguyên qua các giao diện người dùng (kênh truy cập): vStorage Portal, vStorage API, Swift Rest API, S3 Rest API, 3rd party softwares. 

|  |  |  |  |
| --- | --- | --- | --- |
| STT | Tài khoản người dùng | Kênh truy cập | Ghi chú |
| 1 | Tài khoản người dùng Root (Root User Account) | vStorage Portal | Bạn không thể sử dụng tài khoản này để truy cập tài nguyên dịch vụ vStorage qua các kênh khác ngoài vStorage Portal. |
| 2 | Tài khoản người dùng IAM (IAM User Account) | vStorage Portal | Bạn không thể sử dụng tài khoản này để truy cập tài nguyên dịch vụ vStorage qua các kênh khác ngoài vStorage Portal. |
| 3 | Tài khoản Service Account | vStorage API, Swift/ s3 client tool, Swift Rest API, S3 Rest API | Bạn không thể dùng tài khoản này để truy cập tài nguyên qua kênh vStorage Portal. Ngoài ra, bạn có thể sử dụng tài khoản này để tích hợp với dịch vụ vStorage từ ứng dụng phần mềm (software application) của bạn. |
