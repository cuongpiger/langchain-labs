# Tạo Cross Connect

**Thực hiện các bước sau để thực hiện việc tạo một kết nối Cross Connect:**

**Bước 1:** Truy cập thành công vào VNG Cloud, tại màn hình Console chọn đến dịch vụ vNetwork;

**Bước 2:** Tại thanh menu bên trái của giao diện vNetwork, chọn mục Cross Connect;

**Bước 3:** Màn hình được điều hướng tới màn hình Danh sách Cross Connect;

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(4)%20(3).png?raw=true)

**Bước 4:** Tại màn hình danh sách các Cross Connect, nhấn chọn "****Tạo Cross Connect****";

**Bước 5:** Tại màn hình Create a Cross Connect, điền các thông tin khởi tạo như sau:

* ****Tên Cross Connect****: Điền tên của Cross Connect được tạo;
* Mô tả: (tùy chọn) Điền mô tả về Cross Connect được tạo;
* ****Cấu hình Cross Connect****: Chọn Requester (mặc định theo vùng đang cấu hình) và Accepter là hai region cần kết nối giao tiếp với nhau;
* ****Cấu hình Băng thông:**** Chọn gói băng thông phù hợp với nhu cầu.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(3).png?raw=true)

**Bước 6:** Tại bên phải màn hình, xem tổng chi phí gói Băng thông đã chọn, sau đó nhấn chọn "****Tạo****" đề xác nhận và tiến hành thanh toán;

**Bước 7:** Sau khi thanh toán thành công, hệ thống sẽ xử lý kết nối thành công tuyến Cross Connect vừa tạo.

> **Lưu ý:**
>
> * Tại màn hình danh sách Cross Connect, có thể thấy Cross Connect vừa tạo với trạng thái "****Provisioning****" (là trạng thái hệ thống đang thiết lập kết nối);
> * Quá trình thiết lập tuyến Cross Connect này, hệ thống cần nhiều thời gian để thực hiện xác thực giữa hai vùng, do đó có thể ****mất tối đa 20 phút để xử lý****, sau khi hệ thống xử lý xong thì trạng thái sẽ tự động chuyển thành "****Active****".
> * Lúc này người dùng có thể thực hiện thiết lập [Tạo kết nối VPC giữa hai vùng](https://docs.vngcloud.vn/vng-cloud-document/vn/vnetwork/cross-connect/tao-ket-noi-vpc).

