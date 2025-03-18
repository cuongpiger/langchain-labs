# Khởi tạo Pfsense trên HCM03

## Khởi tạo Pfsense

Để khởi chạy ứng dụng, làm theo các bước sau:

**Bước 1: Chọn tên và phiên bản ứng dụng**

**Bước 2: Chọn loại máy ảo (Instance type)** (sự kết hợp giữa CPU x RAM x GPU)

**Bước 3: Chọn cài đặt ổ đĩa (Volume)**

**Bước 4: Chọn cài đặt mạng (Network)** bao gồm các hành động sau:

* Chọn VPC cho ứng dụng
* Chọn thứ tự ưu tiên cho các giao diện mạng Bên ngoài và Bên trong: Lưu ý rằng các giao diện này sẽ được sắp xếp chính xác theo thứ tự người dùng nhập vào
* Chọn cài đặt bảo mật (Security): Chọn **Tạo mới nhóm bảo mật (New security group rules)** để tạo một nhóm mới với các tham số cụ thể cho ứng dụng của bạn, hoặc chọn **Nhóm bảo mật hiện có (Existing security group)** để kế thừa các quy tắc từ nhóm hiện tại

**Bước 5: Chọn cài đặt nhóm máy chủ (Server Group)**

* Để kích hoạt tính năng sẵn sàng cao (HA) cho các máy chủ tường lửa của bạn, hãy chọn **Dedicated SOFT ANTI AFFINITY group** để tạo một nhóm máy chủ mới cho ứng dụng tường lửa của bạn, hoặc chọn **Existing server group** nếu nó đã tồn tại

Sau khi máy ảo đã được cấp phát, hãy sửa đổi **Nhóm Bảo mật** để mở các cổng sau cho máy ảo:

* Truy cập qua vServer Console (từ webportal), Theo mặc định, mật khẩu để trống. 
* Cấu hình truy cập SSH/Web (từ webportal) Theo mặc định, bạn sẽ đăng nhập bằng mật khẩu trống, sau đó ứng dụng sẽ chuyển hướng bạn đến trang thay đổi mật khẩu, vui lòng thay đổi mật khẩu ngay lập tức (Để Mật khẩu cũ trống). 

**Lưu ý: Ứng dụng Marketplace sẽ khởi tạo trong vài phút.**

## Cấu hình interface thông qua Console 

* Assign Interface

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(675).png?raw=true)

* Assigne WAN : vtnet0 ; LAN : vtnet1

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(676).png?raw=true)

* WAN : vtnet0

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(677).png?raw=true)

* LAN : vtnet1

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(678).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(679).png?raw=true)

* Gán IP vào mạng LAN

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(680).png?raw=true)

* Lấy IP được cấp trên Portal để gán vào LAN interface
* Gán IP vào interface

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(681).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(682).png?raw=true)

* IP Local Pfsense là https://LocalIP/

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(683).png?raw=true)

* Cấu hình Pfsense ban đầu : access vào https//local\_IP/ và tiến hành step by step cấu hình : 
