# Cài đặt Sigma Media Server

Sử dụng hướng dẫn bên dưới để cài đặt Sigma Media Server:

### Khởi tạo Sigma Media Server trên vMarketplace

**Bước 1:** Truy cập vào [https://marketplace.console.vngcloud.vn/](https://marketplace.console.vngcloud.vn/)

**Bước 2:** Tại màn hình chính, thực hiện tìm kiếm **Sigma**, tại dịch vụ **Sigma Stream**, chọn **Launch**.

**Bước 3:** Lúc này, bạn cần thiết lập cấu hình cho **Sigma.** Cụ thể, bạn cần chọn:

* **Loại Instance (CPU, RAM, GPU).**
* **Loại và kích cỡ Volume, IOPS**
* **Network:**
  * **VPC**
  * **Security Group**

mà bạn mong muốn sử dụng cho server của bạn. Ngoài ra bạn cũng cần chọn Một Server Group đã tồn tại hoặc chọn **Dedicated SOFT ANTI AFFINITY group** để chúng tôi tự động tạo một server group mới.

**Bước 4:** Tiến hành **thanh toán** như các tài nguyên bình thường trên VNG Cloud.

Lúc này, hệ thống **vServer** sẽ khởi tạo một Server tương ứng với cấu hình mà bạn lựa chọn. Hãy chờ đợi tới khi việc tạo server hoàn thành và tiếp tục các bước sau đây.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(10)%20(2)%20(1).png?raw=true)

### Cấu hình thông số cho Sigma Media Server 

**Bước 1:** Sau khi khởi tạo Sigma từ **vMarketPlace** theo hướng dẫn bên trên, bạn có thể truy cập vào giao diện **vServer** tại [đây](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server) để kiểm tra server chạy Sigma đã được khởi tạo xong chưa. ****Tiếp theo, bạn cần mở các sau trên Security Group cho server Sigma vừa tạo.**** 

* 4000 (TCP): Portal
* 8080 (TCP): HTTP origin (nginx)
* 1935 (TCP): RTMP
* 10080 (UDP): optional cho SRT protocol

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(2)%20(1).png?raw=true)

**Bước 2:** Sau khi server chạy Sigma được khởi tạo thành công. Để vào GUI của Sigma, bạn cần sử dụng địa chỉ IP của External Interface và truy cập tại link: _**http://VM\_External\_IP:4000**_

**Bước 3:** Tại GUI của Sigma, bạn chọn nút **Register Server**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(6)%20(2)%20(1).png?raw=true)

**Bước 4:** Bạn nhập **Email/ Password** nếu có hoặc chọn **Đăng nhập nhanh** với **Github** hoặc **Google**. Ở đây, tôi lựa chọn đăng nhập với tài khoản Google

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(7)%20(2)%20(1).png?raw=true)

**Bước 5**: Sau khi hệ thống thực hiện **authentiation** thành công, bạn cần nhập các thông tin cơ bản cho Sigma bao gồm:

* **Name**
* **Phone Number**
* **Role**
* **Company**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(8)%20(2)%20(1).png?raw=true)



**Bước 6:** Nhập **server name**. Server name này bạn có thể lấy từ portal VNGCloud. Ví dụ bên dưới tôi dùng server Demo\_Sigma đã tạo trước đó.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(9)%20(2)%20(1).png?raw=true)

**Bước 7**: Bạn có thể điều chỉnh bật/ tắt các configuration bao gồm:

* Bật/ Tắt sử dụng **Ingest App** bằng cách chọn vào biểu tượng ON, OFF
* Bật/ Tắt sử dụng **Origin App** bằng cách chọn vào biểu tượng ON, OFF
* Cài đặt **Data Dir** bằng cách chọn vào nút Pick
* Chọn **Submit**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(2).png?raw=true)

**Bước 8**: Tại màn hình cảnh báo việc deploy server, bạn chọn **Yes**

**Bước 9:** Tiếp tục chọn **Done**, lúc này màn hình sẽ hiển thị như sau, bạn hãy tiếp tục bấm chọn **App Editor.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(2)%20(1).png?raw=true)

Sau khi truy cập vào **Portal Sigma Media**, bạn sẽ thấy thông tin server đã tạo trước đó từ **vMarketplace** và thông tin **License** tương ứng.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(2)%20(1).png?raw=true)
