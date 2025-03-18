# Hạn mức tài nguyên

Tài khoản VNG Cloud của bạn có hạn mức mặc định, trước đây được gọi là giới hạn, cho từng dịch vụ của vServer. Trừ khi có ghi chú khác, mỗi hạn mức là dành riêng cho Khu vực. Bạn có thể yêu cầu tăng đối với một số hạn mức tài nguyên và các hạn mức tài nguyên khác không thể tăng.

Cùng với việc tra cứu các giá trị hạn mức, bạn cũng có thể yêu cầu tăng hạn mức từ bảng điều khiển Hạn mức dịch vụ. VNG Cloud có thể phê duyệt, từ chối hoặc phê duyệt một phần yêu cầu của bạn.

### **Xem hạn mức tài nguyên** 

Bạn có thể xem hạn mức tài nguyên bằng tùy chọn sau: Xem thông chi tiết tại trang hiện hữu, tuy nhiên cần lưu ý rằng chỉ có thể xem chi tiết thông tin các hạn mức cho từng tài nguyên chứ không thể xem mức sử dụng hiện hữu cho tài nguyên của bạn, để xem chi tiết về thông tin hạn mức và tình trạng sử dụng hạn mức tài nguyên, vui lòng truy cập vào đường dẫn [https://hcm-3.console.vngcloud.vn/vserver/limit](https://hcm-3.console.vngcloud.vn/vserver/limit), tại ô tìm kiếm có thể tìm theo tên dịch vụ mà bạn muốn để xem thông tin chi tiết về hạn mức.

### **Yêu cầu tăng hạn mức** 

Bạn có thể yêu cầu tăng hạn mức bằng Hạn ngạch dịch vụ, bằng cách sử dụng một trong các tùy chọn sau. Cần lưu ý rằng yêu cầu tăng sẽ không được cấp ngay lập tức. Có thể mất vài ngày để mức tăng của bạn có hiệu lực.

* Mở bảng điều khiển [https://hcm-3.console.vngcloud.vn/vserver/limit](https://hcm-3.console.vngcloud.vn/vserver/limit). Tại trang thông tin, nhấn vào **Yêu cầu tăng hạn mức,** giao diện sẽ chuyển hướng tới trang [https://support.vngcloud.vn/#/app/dashboard](https://support.vngcloud.vn/#/app/dashboard) để bạn có thể thực hiện yêu cầu tăng hạn mức tài nguyên
* Hoặc có thể truy cập trực tiếp vào trang tạo yêu cầu hỗ trợ của chúng tôi: [https://support.vngcloud.vn/#/app/request-ticket/undefined](https://support.vngcloud.vn/#/app/request-ticket/undefined)

Bảng sau đây liệt kê các giá trị tối đa cho tài nguyên thuộc dịch vụ vServer.

| STT | Tài nguyên | Loại dịch vụ | Mặc định | Điều chỉnh | Diễn giải |
| --- | --- | --- | --- | --- | --- |
| 1 | SSO User Account/ Email-SĐT | Account | 20 | Có thể | Số lượng SSO User Account tối đa được phép đăng ký cho 1 Email - SĐT thông qua VNG Cloud Portal |
| 2 | IAM User Account/ Root User Account | Account | 20 | Có thể | Số lượng IAM User Account được phép khởi tạo cho Root User Account thông qua IAM Portal |
| 3 | Service Account/ Root User Account | Account | 20 | Có thể | Số lượng Service Account được phép khởi tạo cho Root User Account thông qua IAM Portal |
| 4 | Acl_Policy | Server | 10 | Có thể | Số lượng Acl Policy tối đa trên 1 Root User Account |
| 5 | Acl_Policy_Rule | Server | 100 | Có thể | Số lượng Acl Policy Rule tối đa trên 1 Root User Account |
| 6 | Bandwidth | Server | 100 | Có thể | Số lượng loại Bandwidth tối đa trên 1 Root User Account |
| 7 | Cluster | Server | 10 | Có thể | Số lượng Cluster tối đa trên 1 Root User Account |
| 8 | Floating_Ip | Server | 50 | Có thể | Số lượng Floating IP tối đa trên 1 Root User Account |
| 9 | Image | Server | 50 | Có thể | Số lượng Image tối đa trên 1 Root User Account |
| 10 | Image_Size | Server | 1000 | Có thể | Dung lượng GB Image Size tối đa trên 1 Root User Account |
| 11 | Internet_Gateway | Server | 10 | Có thể | Số lượng Internet Gateway tối đa trên 1 Root User Account |
| 12 | Mem | Server | 500 | Có thể | Dung lượng GB Memory tối đa trên 1 Root User Account |
| 13 | Minion_Per_Node_Group | Server | 10 | Có thể | Số lượng Minion tối đa trên 1 Node Group cho 1 Root User Account |
| 14 | Network_Interface_Per_Server | Server | 10 | Có thể | Số lượng Network Interface tối đa trên 1 Server cho 1 Root User Account |
| 15 | Node_Group_Per_Cluster | Server | 5 | Có thể | Số lượng Node Group tối đa trên 1 Cluster cho 1 Root User Account |
| 16 | Route | Server | 100 | Có thể | Số lượng Route tối đa trên 1 Root User Account |
| 17 | Route_Table | Server | 20 | Có thể | Số lượng Route Table tối đa trên 1 Root User Account |
| 18 | Secgroup | Server | 10 | Có thể | Số lượng Security Group tối đa trên 1 Root User Account |
| 19 | Secgroup_Rule | Server | 100 | Có thể | Số lượng Security Group Rule tối đa trên 1 Root User Account |
| 20 | Server_Group | Server | 5 | Có thể | Số lượng Sever Group tối đa trên 1 Root User Account |
| 21 | Service_Endpoint | Server | 10 | Có thể | Số lượng Service Endpoint tối đa trên 1 Root User Account |
| 22 | Ssh_Key | Server | 20 | Có thể | Số lượng Ssh Key tối đa trên 1 Root User Account |
| 23 | Subnet | Server | 30 | Có thể | Số lượng Subnet tối đa trên 1 Root User Account |
| 24 | Vcpu | Server | 1000 | Có thể | Số lượng Vcpu tối đa trên 1 Root User Account |
| 25 | Virtual_Ip_Address | Server | 3 | Có thể | Số lượng Virtual_Ip_Address tối đa trên 1 Root User Account |
| 26 | Vm | Server | 150 | Có thể | Số lượng Server tối đa trên 1 Root User Account |
| 27 | Volume | Server | 200 | Có thể | Số lượng Volume tối đa trên 1 Root User Account |
| 28 | Volume_Maxsize | Server | 5000 | Có thể | Dung lượng GB tối đa cho Volume trên 1 Root User Account |
| 29 | Volume_Size | Server | 10000 | Có thể | Tổng dung lượng GB tối đa cho Volume trên 1 Root User Account |
| 30 | Vpc | Server | 10 | Có thể | Số lượng Vpc tối đa trên 1 Root User Account |
| 31 | Certificate_Per_Lb | Load balancer | 5 | Có thể | Số lượng Certificate tối đa trên Load Balancer cho 1 Root User Account |
| 32 | Listener_Per_Lb | Load balancer | 10 | Có thể | Số lượng Listener tối đa trên Load Balancer cho 1 Root User Account |
| 33 | Load_Balancer | Load balancer | 10 | Có thể | Số lượng Load Balancer tối đa trên 1 Root User Account |
| 34 | Member_Per_Pool | Load balancer | 20 | Có thể | Số lượng Member tối đa trên 1 Pool cho 1 Root User Account |
| 35 | Policy_Per_Lb | Load balancer | 10 | Có thể | Số lượng Policy tối đa cho 1 Load Balancer trên 1 Root User Account |
| 36 | Pool_Per_Lb | Load balancer | 10 | Có thể | Số lượng Pool tối đa cho 1 Load Balancer trên 1 Root User Account |
| 37 | As_Cluster | vAS | 5 | Có thể | Số lượng As_Cluster tối đa trên 1 Root User Account |
| 38 | As_Node | vAS | 10 | Có thể | Số lượng As_Node tối đa trên 1 Root User Account |
| 39 | As_Policy | vAS | 10 | Có thể | Số lượng As_Policy tối đa trên 1 Root User Account |
| 40 | As_Profile | vAS | 10 | Có thể | Số lượng As_Profile tối đa trên 1 Root User Account |
| 41 | As_Receiver | vAS | 20 | Có thể | Số lượng As_Receiver tối đa trên 1 Root User Account |
| 42 | As_Scheduler | vAS | 10 | Có thể | Số lượng As_Scheduler tối đa trên 1 Root User Account |

