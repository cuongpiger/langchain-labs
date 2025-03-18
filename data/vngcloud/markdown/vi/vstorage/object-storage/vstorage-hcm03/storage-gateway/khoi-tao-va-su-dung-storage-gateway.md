# Khởi tạo và sử dụng Storage Gateway

#### Hướng dẫn khởi tạo storage gateway 

1. Truy cập trang chủ VNGCloud tại [đây](https://dashboard.console.vngcloud.vn/). Chọn Service: **vStorage**, sau đó chọn **Storage Gateway**:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(555).png?raw=true)

2. Tại trang vMarketplace, chọn **Launch on Computer Engine**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(556).png?raw=true)

3. Bạn nhập thông tin App mong muốn, lựa chọn Instance phù hợp, lựa chọn loại ổ đĩa và kích thước phù hợp, sau đó chọn network, security mong muốn và chọn **Launch Application**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(557).png?raw=true)

Sau khi bạn Launch Application thành công, hệ thống sẽ thực hiện khởi tạo một server tương ứng. Sau khi VM được tạo thành công, bạn hãy truy cập vào địa chỉ External IP của VM và thực hiện đăng nhập với thông tin đăng nhập đã được gửi về email của bạn (lần đăng nhập đầu tiên sẽ đổi lại password mặc định).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(561).png?raw=true)

> **Chú ý:**
>
> Security Groups cần mở thêm các port sau để share được dữ liệu:
>
> * port web: 80,443 
> * port share:
>   * port 445,139: nếu sử dụng SMB
>   * port 111,2049,34567: nếu sử dụng NFS

***

#### Hướng dẫn tạo file share  

1. **Tạo credential**

Tại mục **Credential** chọn C**reate credentials:** 

Trong đó: 

* Credential name: nhập tên credential mong muốn.
* Region: chọn Region chứa project mà bạn muốn thực hiện lưu trữ trên vStorage.
* Project ID
* Provider: bạn có thể chọn sử dụng S3 key hoặc Swift user tùy chọn.
  * Nếu dùng Swift, bạn cần nhập username và password.
  * Nếu dùng S3 key, bạn cần nhập Access key và Secret key.

Những thông tin này bạn có thể tạo cũng như lấy thông tin trên vStorage Portal và IAM Portal. 

2. **Tạo file share**

Chọn **file share** rồi chọn C**reate file share**

Trong đó:

* Volume Information:
  * vStorage Credential: chọn credential đã tạo bên trên.
  * Container: chọn một container trong danh sách container trong project đã được khai báo sử dụng.
* Permission:
  * nfs: phân quyền theo IP, chúng tôi sẽ sử dụng IP để phân quyền, bạn cần nhập IP và chọn quyền tương ứng
  * smb: phân quyền theo User, chúng tôi sẽ sử dụng User để phân quyền, bạn cần chọn User và chọn quyền tương ứng

Chọn **Create** và đợi hoàn tất việc tạo File Share. Bạn cũng có thể xem thêm thông tin mount trong mục **Mount**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(562).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(565).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(564).png?raw=true)

#### 3. Client kết nối và sử dụng file share 

**3.1 Client nfs**

Trên máy linux, mở terminal gõ lệnh: _apt install nfs-common_

Trên UI gateway File Share -> Show Commands -> nfs -> copy -> dán lệnh vào terminal client

**3.2 Client smb**

Trên window: Trên UI gateway **File Share -> Show Commands -> smb -> window -> copy -> dán vào search của window -> nhập user/password**

Trên máy linhx, cài dặt client:  _apt install cifs-utils_ 

Trên UI gateway **File Share -> Show Commands -> smb -> window -> copy -> dán vào terminal -> nhập user/password**
