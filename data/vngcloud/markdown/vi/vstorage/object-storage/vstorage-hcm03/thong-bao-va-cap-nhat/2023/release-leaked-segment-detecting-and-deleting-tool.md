# Release Leaked Segment Detecting & Deleting Tool

#### 1. Thông tin release 

| **Tên sản phẩm**      | vStorage                                   |
| --------------------- | ------------------------------------------ |
| **Tên release**       | Leaked segment detecting and deleting tool |
| **Ngày release**      | Nov 2022                                   |
| **Phiên bản release** | vos-leak-segment-v1.0.0                    |

#### 2. Tính năng release 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| STT | **Tính năng** | **Phạm vi & giới hạn** | **Loại** | **Giá trị mang lại** |
| 1 | - Xử lý segment rác trong module upload/ reupload file qua S3API, S3 Client Tool. | - Đối với module upload/ reupload qua Web Portal phải tự xử lý việc sinh ra các segment rác nên không xử lý trong tool này. <br> - Các tính năng container versioning, copy multipart bằng phương thức GET, xóa object thông qua xóa manifest file mà không xóa segment có thể sinh ra segment rác nhưng tool này không xử lý segment rác sinh ra (nếu có) cho các tính năng này. | New |  |

**Ghi chú:**

* New: tính năng mới
* Enhancement: nâng cấp tính năng đang có sẵn
* Fixed Bugs: sửa lỗi tính năng
