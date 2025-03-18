# Chuyển đổi đơn vị lưu trữ từ storage base 1000 sang 1024

#### 1. Thông tin cập nhật 

| **Tên sản phẩm**       | vStorage                                                 |
| ---------------------- | -------------------------------------------------------- |
| Tên dịch vụ            | vStorage portal                                          |
| **Tên cập nhật**       | Chuyển đổi đơn vị lưu trữ từ storage base 1000 sang 1024 |
| **Ngày cập nhật**      | July, 01 2023                                            |
| **Phiên bản cập nhật** | Version 1.0.4                                            |

#### 2. Tính năng cập nhật 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **STT** | **Tính năng** | **Phạm vi & giới hạn** | **Loại** | **Giá trị mang lại** |
| 1 | - Tất cả các tính năng mua mới, resize, renew, recovery sẽ chuyển qua dùng đơn vị storage base = 1024 thay vì 1000 như trước đây. | - Áp dụng cho người dùng trả trước và trả sau. <br> - Áp dụng cho đơn vị billing Quota, Usage. <br> - Không áp dụng cho đơn vị billing Traffic. | Enhancement | - Việc chuyển đổi cách tính storage base từ 1000 lên 1024 nhằm đồng nhất cách tính storage base giữa VNG Cloud và hệ thống phía khách hàng. Hiện tại quy chuẩn chung của các hệ thống khác thuộc VNG Cloud đều quy đổi từ Bytes thành KB, MB, GB theo tỉ lệ 1024. |

**Ghi chú:**

* New: tính năng mới
* Enhancement: nâng cấp tính năng đang có sẵn
* Fixed Bugs: sửa lỗi tính năng
