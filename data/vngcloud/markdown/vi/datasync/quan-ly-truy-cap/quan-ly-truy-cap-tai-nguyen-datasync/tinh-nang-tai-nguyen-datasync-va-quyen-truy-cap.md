# Tính năng, tài nguyên DataSync và quyền truy cập

#### Tài nguyên DataSync được hỗ trợ phân quyền truy cập: 

Chúng tôi cung cấp cho bạn loại tài nguyên được phép phân quyền truy cập là Transfer Job.

***

#### Tính năng DataSync và quyền cần để thực hiện tính năng: 

Chúng tôi cung cấp cho bạn 3 nhóm quyền chính (List, Read, Write) với ý nghĩa được mô tả ở bảng bên dưới:

| Tính năng DataSync | Danh sách quyền để thực hiện tính năng (Action) | Mô tả ý nghĩa | Danh sách tài nguyên DataSync (Resource) | Công cụ sử dụng | Loại tài khoản sử dụng |
| --- | --- | --- | --- | --- | --- |
| Nhóm quyền  **List** : |  |  |  |  |  |
| - ListTransferJob | - ListTransferJob | - Hỗ trợ để hiển thị danh sách transfer job. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - ListJobRunHistories | - ListTransferJob <br> - ListJobRunHistories | - Hỗ trợ để hiển thị danh sách lịch sử chạy transfer job. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| Nhóm quyền  **Read** : |  |  |  |  |  |
| - GetTransferJob | - ListTransferJob <br> - GetTransferJob | - Hỗ trợ để truy xuất thông tin transfer job. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - GetRunningJobStatics | - ListJobRunHistories <br> - GetRunningJobStatics | - Hỗ trợ để truy xuất thông tin chi tiết kết quả chạy transfer job (không bao gồm phần Monitoring). | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - GetMonitorJobStatics | - ListJobRunHistories <br> - GetMonitorJobStatics | - Hỗ trợ để truy xuất thông tin chi tiết kết quả chạy transfer job (Monitoring). | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| Nhóm quyền  **Write** |  |  |  |  |  |
| - CreateTransferJob | - ListTransferJob <br> - GetTransferJob <br> - CreateTransferJob <br> - vStorage: ListRegions ListProjects ListContainers ListDirectories GetRegions GetProjects GetContainers GetDirectories <br> - ListRegions <br> - ListProjects <br> - ListContainers <br> - ListDirectories <br> - GetRegions <br> - GetProjects <br> - GetContainers <br> - GetDirectories <br> - vMonitor Platform: ListLogProjects GetLogProjects <br> - ListLogProjects <br> - GetLogProjects | - Hỗ trợ để khởi tạo một transfer job. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - DeleteTransferJob | - ListTransferJob <br> - GetTransferJob <br> - DeleteTransferJob | - Hỗ trợ để xóa một transfer job. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - RunTransferJob | - ListTransferJob <br> - GetTransferJob <br> - RunTransferJob | - Hỗ trợ để run một transfer job. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - UpdateTransferJob | - ListTransferJob <br> - GetTransferJob <br> - UpdateTransferJob <br> - vStorage: ListRegions ListProjects ListContainers ListDirectories GetRegions GetProjects GetContainers GetDirectories <br> - ListRegions <br> - ListProjects <br> - ListContainers <br> - ListDirectories <br> - GetRegions <br> - GetProjects <br> - GetContainers <br> - GetDirectories <br> - vMonitor Platform: ListLogProjects GetLogProjects <br> - ListLogProjects <br> - GetLogProjects | - Hỗ trợ để cập nhật một transfer job đã tạo trước đó. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - CancelTransferJob | - ListTransferJob <br> - GetTransferJob <br> - CancelTransferJob | - Hỗ trợ để dừng chạy một transfer job đang chạy. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |
| - RetryTransferJob | - ListTransferJob <br> - GetTransferJob <br> - ListJobRunHistories <br> - GetRunningJobStatics <br> - GetMonitorJobStatics <br> - RetryTransferJob | - Hỗ trợ để chạy lại một transfer job trên kết quả của lần chạy trước đó. | - All resources <br> - Specific resource: transfer job id. | - DataSync Portal | - Root User Account <br> - IAM User Account |

#### Quyền hạn có sẵn mà DataSync cung cấp: 

Chúng tôi cung cấp cho bạn một tập các quyền hạn đã được cấu hình sẵn với ý nghĩa được mô tả ở bảng bên dưới. Bạn có thể trực tiếp sử dụng chúng để liên kết với các tài khoản IAM User Account để thực hiện phân quyền nhanh mà không cần tạo policy chi tiết theo hướng dẫn bên trên. 

| Predefined roles | Description |  |
| --- | --- | --- |
| **Predefined roles** | **Description** | **Resource** |
| DataSync Full Access | - ListTransferJob <br> - ListJobRunHistories <br> - GetTransferJob <br> - GetRunningJobStatics <br> - CreateTransferJob <br> - DeleteTransferJob <br> - RunTransferJob <br> - UpdateTransferJob <br> - CancelTransferJob <br> - RetryTransferJob | All resources |
| DataSync Read Only Access | - ListTransferJob <br> - ListJobRunHistories <br> - GetTransferJob <br> - GetRunningJobStatics | All resources |
| DataSync IAM User Full Access | - ListTransferJob <br> - ListJobRunHistories <br> - GetTransferJob <br> - GetRunningJobStatics <br> - CreateTransferJob <br> - DeleteTransferJob <br> - RunTransferJob <br> - UpdateTransferJob <br> - CancelTransferJob <br> - RetryTransferJob | All resources |
| DataSync IAM User Read Only Access | - ListTransferJob <br> - ListJobRunHistories <br> - GetTransferJob <br> - GetRunningJobStatics | All resources |
