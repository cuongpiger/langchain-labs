# Khởi tạo policy cho Service Account

Về mặt tổng quan, việc khởi tạo policy có mối ràng buộc với IAM User Account hay Service Account, việc khởi tạo policy này là giống nhau cho cả 2 loại. Tuy nhiên chúng tôi vẫn sẽ nhắc lại các bước để bạn có thể dễ dàng quan sát và thực hiện. 

Để khởi tạo một policy sử dụng để truy cập vào tài nguyên vStorage, hãy làm theo các bước bên dưới: 

1. Đăng nhập vào [https://hcm-3.console.vngcloud.vn/iam/](https://hcm-3.console.vngcloud.vn/iam/) với tài khoản Root User Account.
2. Chọn thư mục **Policy**. 
3. Chọn **Create a Policy**.
4. Nhập **Name** và **Description** nếu cho cho Policy.
5. Chọn **Next step**.
6. Chọn **Product là vstorage**.
7. Chọn **Actions**:
   1. Chọn **Allow permissions**: mặc định hệ thống vIAM sẽ luôn bật tức là cho phép quyền hạn được áp dụng trên policy. Nếu bạn tắt mode này thì hệ thống sẽ từ chối (đảo chiều) quyền hạn tương ứng.
      1. **Allow permissions**: cho phép truy cập theo action đã chọn. 
      2. **Deny permissions**: từ chối truy cập theo action đã chọn.
   2. Chọn **All vstorage actions** nếu muốn tạo policy có quyền thực hiện tất cả các hành động trên vStorage. Chi tiết ý nghĩa của các action vui lòng tham khảo tại [Tính năng, tài nguyên vStorage và quyền truy cập](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/phan-quyen-truy-cap-va-lam-viec-thong-qua-iam/tinh-nang-tai-nguyen-vstorage-va-quyen-truy-cap).
8. Chọn **Resources**:
   1. Chọn **All resources** nếu muốn quyền truy cập đã chọn bên trên được phép truy cập vào mọi tài nguyên trên tài khoản SSO account của bạn. 
   2. Chọn **Specify resources**: chọn project, container, object cụ thể mà bạn muốn cho phép truy cập tới. Bạn có thể nhập thông tin cho mỗi loại resources này bằng 1 trong những cách sau: 
      1. **Nhập \*** nếu bạn muốn chọn tất cả tài nguyên.
      2. **Nhập cụ thể ID của project, tên của container, tên của object** nếu bạn muốn chỉ định tới chính xác project, container, object đó. 
      3. **Nhập tiền tố (prefix)** nếu bạn muốn chỉ định tới một tập project, container, object được bắt đầu bằng tiền tố đã khai báo. 
   3. Bạn cũng có thể chọn **Any** để cho phép truy cập tới mọi project, container, object trong tài khoản SSO account của bạn. 
   4. Chọn **Request conditions:** nhập điều kiện đặc biệt cho policy nếu có. 

Sau khi bạn thực hiện 8 bước bên trên, policy cho vStorage đã được khởi tạo. Tiếp theo, bạn hãy gán nó vào Service Account theo hướng dẫn tại [Liên kết tài khoản Service Account với policy tương ứng](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/lien-ket-tai-khoan-service-account-voi-policy-tuong-ung).

Ngoài các bước tạo policy đặc thù cho riêng bạn như trên, chúng tôi cũng cung cấp cho bạn một tập các policy mặc định với các quyền hạn đa dạng. Bạn có thể sử dụng tập policy này và liên kết trực tiếp chúng tới tài khoản Service Account. Để biết thêm thông tin về danh sách policy mặc định, tham khảo tại [Tính năng, tài nguyên vStorage và quyền truy cập](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-truy-cap-tai-nguyen-vstorage/phan-quyen-truy-cap-va-lam-viec-thong-qua-iam/tinh-nang-tai-nguyen-vstorage-va-quyen-truy-cap).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/Khoi_tao_policy.gif?raw=true)
