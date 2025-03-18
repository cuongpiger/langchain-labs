# Tạo kết nối VPC

**Thực hiện các bước sau để thực hiện việc tạo một kết nối VPC giữa hai region:**

**Bước 1:** Truy cập thành công vào VNG Cloud, tại màn hình Console chọn đến dịch vụ vNetwork;

**Bước 2:** Tại thanh menu bên trái của giao diện vNetwork, chọn mục Cross Connect;

**Bước 3:** Màn hình được điều hướng tới màn hình Danh sách Cross Connect;

**Bước 4:** Tại màn hình danh sách các Cross Connect, nhấn chọn vào Cross Connect đã tạo trước;

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(783).png?raw=true)

**Bước 5:** Tại màn hình xem chi tiết Cross Connect, ở Tab Connections, nhấn chọn "****Thêm kết nối****" để thực hiện việc tạo kết nói VPC giữ hai vùng;

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(784).png?raw=true)

**Bước 6:** Tại màn hình Add VPC's Connections:

* Người dùng phải chọn trước ****"VPC của Requester Region"**** ;
* Hệ thống dựa vào VPC vừa chọn của Requester Region sẽ [kiểm tra điều kiện kết nối](https://docs.vngcloud.vn/vng-cloud-document/vn/vnetwork/cross-connect/kiem-tra-dieu-kien-ket-noi-vpc) và hiển thị các ****"VPC của Accepter Region"**** mà người dùng có thể tạo kết nối;

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(785).png?raw=true)

**Bước 7**: Sau khi chọn cặp VPC kết nối, hẫy nhấn "****Thêm****" để thêm mới cặp kết nối VPC. Sau đó, hệ thống thực hiện kết nối, nếu thành công thì trạng thái là 'Active'. Ngoài ra, số lượng kết nối VPC được tăng lên và thể hiện ở màn hình danh sách Cross Connect.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(786).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(787).png?raw=true)

> **Ghi chú:**
>
> * **Requester Region** và **Accepter Region** được hiểu là hai region độc lập để tạo thành một kết nối Cross Connect. (Requester Region được mặc định chọn theo region đang được chọn khi truy cập vào vServer)
> * VPC của mỗi Region phải được tạo từ trước tại vServer; ( xem [Tạo VPC](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc#virtualprivatecloud-vpc-taovpc)).

