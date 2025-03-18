# Kết nối vào máy chủ Linux bằng công cụ SSH Client

Để kết nối đến một máy chủ Linux bằng SSH Client, bạn cần có một Terminal hoặc Command Prompt trên máy tính của bạn và sử dụng lệnh SSH. Dưới đây là hướng dẫn cách thực hiện kết nối SSH đến máy chủ Linux

Để biết thông tin về cách kết nối với phiên bản Window, hãy xem hướng dẫn [Kết nối vào máy chủ Windows sử dụng công cụ Remote Desktop (RDP)](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/server/ket-noi-vao-may-chu-ao/ket-noi-vao-may-chu-windows-su-dung-cong-cu-remote-desktop-rdp) về cách kết nối với máy chủ của bạn.

***

### **Điều kiện tiên quyết** 

* **Máy chủ phải đang chạy**:
  * Sau khi máy chủ được khởi tạo thành công, thông tin của nó sẽ xuất hiện trên trang danh sách máy chủ của bảng điều khiển và trạng thái của máy chủ là Active
*   **Thông tin kết nối đến máy chủ**: Để biết thông tin kết nối của máy chủ, vui lòng kiểm tra email đã đăng ký:

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(12)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

_**Lưu ý:** Thông tin này là bảo mật và chỉ được gởi cho email đã đăng kí. VNG Cloud không thể can thiệp để phục hồi thông tin login của vServer (username/ passsword/ key) trong mọi tình huống_

***

### **Kết nối sử dụng Client trên hệ điều hành Linux và MacOS** 

#### _**Phương án 1**_: **Login SSH bằng password** 

1.  Sử dụng Terminal của Linux để kết nối đến vServer

    | `ssh -p 234` `stackops@61.28.233.113` |
    | ------------------------------------- |
2.  Thay đổi password cho user stackops ở lần đầu tiên login:\
    \
    **1 -** Nhập password của user stackops với nội dung là **instancePassword** trong email\
    **2 -** Nhập lại password của user stackops với nội dung là **instancePassword** trong email\
    **3 -** Nhập new password cho user stackops để dùng cho login sau này\
    **4 -** Nhập lại new password cho user stackops để dùng cho login sau này\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
3.  Kết nối lại đến vServer\
    \
    **1 -** Nhập password mới đã thay đổi ở Bước 2 cho user stackops\
    **2 -** Gõ lệnh sudo -i hoặc sudo su để có quyền thực thi quyền root trên Server

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

#### _**Phương án 2**_: **Login SSH bằng SSH KEY** 

Nếu bạn đã tạo một SSH Key Pair trên portal VNGCLOUD (_Nhấp vào_ [_**đây**_](https://docs.vngcloud.vn/display/ONVINA/SSH+Keys+HCM+03) _để xem hướng dẫn tạo SSH Keys_) và có add SSH Key vô vServer trong quá trình khởi tạo, bạn có thể thực hiện các bước sau đây

1.  Sử dụng Terminal của Linux để kết nối đến vServer

    | `ssh -i ~/Download/private_key01.pem -p 234` `stackops@61.28.233.113` |
    | --------------------------------------------------------------------- |
2.  Thay đổi password cho user stackops ở lần đầu tiên login\
    \
    **1 -** Nhập password của user stackops với nội dung là **instancePassword** trong email\
    **2 -** Nhập new password cho user stackops để dùng cho login sau này\
    **3 -** Nhập lại new password cho user stackops để dùng cho login sau này\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
3.  Kết nối lại đến vServer\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

***

### **Đối với Client thuộc hệ điều hành Window** 

_**Phương án 1**_**: Login SSH bằng password**

1.  Sử dụng Putty của Windows để kết nối đến vServer

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(6)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
2. Thay đổi password cho user stackops ở lần đầu tiên login

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(8)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

\
**1 -** Nhập password của user stackops với nội dung là **instancePassword** email\
**2 -** Nhập lại password của user stackops với nội dung là **instancePassword** email\
**3 -** Nhập new password cho user stackops để dùng cho login sau này\
**4 -** Nhập lại new password cho user stackops để dùng cho login sau này

3. Kết nối lại đến vServer\
   \
   **1 -** Nhập password mới đã thay đổi ở Bước 2 cho user stackops\
   **2 -** Gõ lệnh sudo -i hoặc sudo su để có quyền thực thi quyền root trên Server

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(9)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

_**Option 2**_: **Login SSH bằng SSH KEY**\
Nếu bạn đã tạo một SSH Key Pair trên portal VNGCLOUD (_Nhấp vào_ [_**đây**_](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/security/ssh-key-bo-khoa) _để xem hướng dẫn tạo SSH Keys_) và có add SSH Key vô vServer trong quá trình khởi tạo, bạn có thể thực hiện các bước sau đây

1.  Dùng putty-gen để convert file **key.pem** đã download thành file **key.ppk**\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(10)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(11)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
2.  Sử dụng Putty của Windows để kết nối đến vServer, authen bằng file **key.ppk** đã tạo ra ở trên\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(12)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(13)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(14)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
3.  Thay đổi password cho user stackops ở lần đầu tiên login\
    \
    **1 -** Nhập password của user stackops với nội dung là **instancePassword** email\
    **2 -** Nhập new password cho user stackops để dùng cho login sau này\
    **3 -** Nhập lại new password cho user stackops để dùng cho login sau này\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(15)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
4.  Kết nối lại đến vServer\


    ![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(16)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

