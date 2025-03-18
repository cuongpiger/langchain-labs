# Cải tiến tính năng, sửa lỗi vStorage trong tháng 09/2023

#### 1. Thông tin cập nhật 

| **Tên sản phẩm**       | vStorage                                         |
| ---------------------- | ------------------------------------------------ |
| Tên dịch vụ            | vStorage portal                                  |
| **Tên cập nhật**       | Cho phép thiết lập nhiều normal expiration rules |
| **Ngày cập nhật**      | Sep, 14th 2023                                   |
| **Phiên bản cập nhật** | Version 1.0.5                                    |

#### 2. Tính năng cập nhật 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **STT** | **Tính năng** | **Phạm vi & giới hạn** | **Loại** | **Giá trị mang lại** |
| 1 | - Cho phép người dùng sử dụng tính năng  **Container lifecycle**  có thể thiết lập nhiều  **Normal expiration rules**  trên một container thay vì chỉ một rule như trước đây. | - Áp dụng cho loại Normal expiration | Enhancement |  |
| 2 | - Cho phép tạo S3 presigned URL cho objects. |  | New |  |
| 3 | - Cho phép người dùng sử dụng tính năng  **Container lifecycle**  để thiết lập các expiration rules trên project loại  **Archive.** |  | New |  |
| 4 | - Cho phép người dùng lấy danh sách objects trong container hoặc directory có tên chứa ký tự đặc biệt. |  | Fixed Bugs |  |
| 5 | - Cho phép người dùng chuyển đổi ngôn ngữ trong các trang Integration. |  | Fixed Bugs |  |
| 6 | - Cho phép người dùng chọn default region. |  | Fixed Bugs |  |

**Ghi chú:**

* New: tính năng mới
* Enhancement: nâng cấp tính năng đang có sẵn
* Fixed Bugs: sửa lỗi tính năng

#### 3. Tài liệu cập nhật 

* Container lifecycle: [Sử dụng tính năng container lifecycle](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-container/su-dung-tinh-nang-container-lifecycle)
* S3 presigned URL: [Chia sẻ object](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-directory-va-object/chia-se-object)
