# Tính năng, tài nguyên File Storage và quyền truy cập

**Tài nguyên File Storage được hỗ trợ phân quyền truy cập:**

* File Storage

***

**Tính năng File Storage và quyền cần để thực hiện tính năng:**

Chúng tôi cung cấp cho bạn 3 nhóm quyền chính (List, Read, Write) với ý nghĩa được mô tả ở bảng bên dưới:

| Action | Mục đích sử dụng | Resource |
| --- | --- | --- |
| ListFileStorage | Lấy danh sách các file storage | N/A |
| ListTag | Lấy danh sách tag trên từng file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| GetFileStorage | Lấy thông tin chi tiết một file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| GetMountGuide | Lấy thông tin mount target | - All resource hoặc theo từng resource file-storage-id cụ thể |
| CreateFileStorage | Tạo mới một file storage | N/A |
| CreateFileStorageTag | Tạo mới một tag cho file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| ResizeFileStorage | Thay đổi kích thước max quota của một File Storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| EditFileStorage | Chỉnh sửa một file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| EditFileStorageTag | Chỉnh sửa tag của một file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| DeleteFileStorage | Xóa một file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
| DeleteFileStorageTag | Xóa tag của một file storage | - All resource hoặc theo từng resource file-storage-id cụ thể |
