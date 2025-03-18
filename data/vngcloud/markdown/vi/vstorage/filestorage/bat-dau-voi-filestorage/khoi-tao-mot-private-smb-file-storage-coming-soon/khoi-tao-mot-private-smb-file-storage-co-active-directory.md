# Khởi tạo một Private SMB File Storage có Active Directory

Để khởi tạo một SMB (Server Message Block) có Active Directory trên hệ thống File Storage, bạn có thể làm theo các bước sau:

## Khởi tạo Windows server on vServer

Dưới đây là hướng dẫn cơ bản cho việc khởi tạo Windows server trên vServer, nếu bạn đã có sẵn server, hãy bỏ qua bước này. 

<details>

<summary>Hướng dẫn tạo Windows server</summary>

Trước khi có thể thực hiện khởi tạo Windows server, hãy đảm bảo bạn khởi tạo VPC, Subnet trên hệ thống vServer. Tiếp theo, thực hiện các bước theo hướng dẫn bên dưới để khởi tạo Windows server: 

1. Đăng nhập vào vServer tại [https://hcm-03.console.vngcloud.tech/vserver](https://hcm-03.console.vngcloud.tech/vserver/v-server/create-server).
2. Tiếp tục chọn mục **Servers**.
3. Chọn **Create a Server.**
4. Ở mục **Basic Configuration**, nhập **Server name** để mô tả tên cho Server của bạn. Tên Server có thể bao gồm các chữ cái (a-z, A-Z, 0-9, '\_', '-'). Độ dài dữ liệu đầu vào nằm trong khoảng từ 5 đến 50. Nó không được bao gồm khoảng trắng ở đầu hoặc ở cuối và tên Server name phải khác với Username
5. Lựa chọn **Zone** mà bạn mong muốn tạo server.
6. Nhập thông tin **Tag** bao gồm **Key**/ **Value** cho server và click **Add** để thêm tag này nếu bạn có nhu cầu.
7. Lựa chọn **OS Images: Windows,** tiếp tục chọn **Window version** tùy thuộc theo nhu cầu sử dụng của bạn.
8. Dưới mục **Instance type,** là danh sách các cấu hình Flavor, bạn có thể chọn cấu hình Flavor mong muốn cho Server của mình theo. **iot.v1.small1x1** được chúng tôi đề xuất như một cấu hình cơ bản mặc định để khởi tạo Server
9. Ở mục **Volume Settings**, nhập cấu hình cho Boot OS Volume (Root) gồm **Size GB**, **Volume Type SSD** và **IOPS**, sau đó chọn **Next**
10. Ngoài ra bạn có thể thêm **Data Volume** vào Server trong quá trình khởi tạo bằng cách chọn **Add Data volume,** sau đó **n**hập cấu hình cho Data Volume gồm **Volume name**, **Size GB**, **Volume Type SSD** và **IOPS**, chọn **Next**
11. Kế tiếp chọn thông số mục **Network settings:** Tại đây có thể chọn **VPC** để cấp Private IP cho Server và **Subnet** từ danh sách bạn đã tạo trước đó, hoặc có thể nhấn vào [**đây**](https://hcm-3.console.vngcloud.vn/vserver/network/vpc) để tạo mới VPC và Subnet, cần lưu ý ràng sau khi tạo VPC và Subnet, nó sẽ hiển thị tại trang danh sách cho phép bạn chọn trong quá trình khởi tạo Server:
    1. Tích vào ô Floating IP để gán Public IP cho Server (Nhấn vào [**đây**](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/network/floating-ip) để xem hướng dẫn attach/ detach Floating IP)
    2. **Security group** để quản lý bộ ACL - Access Control List cho Server. (Nhấp vào [**đây**](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/security/security-groups) để xem hướng dẫn tạo và quản lý Security group)
12. Nhập thông tin **Authentication**: Empty: hệ thống sẽ tự động tạo và gắn password hoặc user tự tinh chỉnh và enable hay disable việc bỏ qua change password lần đầu.
13. Ở mục **Other Settings**, có thể tùy chọn server Group hoặc không theo nhu cầu sử dụng. Bạn có thể gán Server vào các Group trước đó đã tạo (Với các thuộc tính như cùng Compute Host hay khác Compute Host)
14. Chọn **Launch Server** và thực hiện các bước thanh toán để hoàn thành việc khởi tạo server

<img src="../../../../.gitbook/assets/image (21) (2).png" alt="" data-size="original">

</details>

> **Chú ý:** 
>
> Security Groups trên Windows server cần mở thêm các port sau để share được dữ liệu:
>
> * Với File Storage NFS: **Outbound** cần mở thêm port **2049**
> * Với File Storage SMB có Basic Authentication: **Outbound** cần mở thêm port **445**
> * Với File Storage SMB Có Active Directory Authentication: **Inbound** cần mở thêm list port để có thể kết nối được từ File Storage đến AD.

***

## Kết nối tới Windows server vừa khởi tạo

Dưới đây là hướng dẫn cơ bản cho việc kết nối tới Windows server trên vServer, nếu bạn đã sử dụng Console trực tiếp trên vServer Portal, vui lòng bỏ qua bước này.

<details>

<summary>Kết nối tới Windows server </summary>

**Để có thể kết nối vào máy chủ Window, trước tiên, bạn cần cài đặt RDP:** Theo mặc định, Windows sẽ bao gồm RDP Client. Để xác minh, hãy nhập **mstsc** tại cửa sổ Command Prompt. Nếu máy tính của bạn không nhận ra lệnh này, hãy xem trang chủ Windows và tìm kiếm bản tải xuống cho ứng dụng[ Microsoft Remote Desktop](https://www.microsoft.com/vi-vn/windows).

1. Truy cập vào trang quản lý Server tại trình điều khiển của chúng tôi tại: [https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server](https://hcm-3.console.vngcloud.vn/vserver/v-server/cloud-server)
2. Chọn **Server** cần kết nối, sau đó chọn **Action, tiếp tục chọn Connect**
3. Trên trang **Connect to Server**, chọn tab **RDP (Window)**

<img src="../../../../.gitbook/assets/image (894).png" alt="" data-size="original">

4. Chọn **Download RDP File**. Trình duyệt của bạn sẽ nhắc bạn mở hoặc lưu tệp RDP. Khi bạn đã hoàn tất tải xuống tệp, hãy chọn **Done** để quay lại trang máy chủ:
5. Thực hiện mở tệp tin đã tải xuống để thực hiện remote tới Windows server. Chọn **Connect** để tiếp tục kết nối với máy chủ của bạn

<img src="../../../../.gitbook/assets/image (895).png" alt="" data-size="original">

6. Tài khoản quản trị viên được chọn theo mặc định. Bạn cần sao chép và dán mật khẩu mà bạn đã lưu trước đó vào pop-up đăng nhập (Thông tin này lấy từ email), trong đó nhập thông tin **InstanceLogin** vào **Username**, **InstancePassword** vào **Password.**
7. Chọn **OK.** Do tính chất của chứng chỉ tự ký, bạn có thể nhận được cảnh báo rằng chứng chỉ bảo mật không thể được xác thực. Sử dụng các bước sau để xác minh danh tính của máy tính từ xa hoặc chỉ cần chọn **Yes** (Windows) hoặc **Continue** (Mac OS X) nếu bạn tin cậy chứng chỉ.

<img src="https://docs.vngcloud.vn/~gitbook/image?url=https%3A%2F%2F3672463924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FB0NrrrdJdpYOYzRkbWp5%252Fuploads%252FNH1l2utiMi3RJxfBoknu%252Fimage.png%3Falt%3Dmedia%26token%3Db50838b8-d830-4273-a67f-6ccfe237ccf4&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f64057f4&#x26;sv=2" alt="" data-size="original">

8. Màn hình sẽ hiển thị đang kết nối đến máy chủ **Window** thành công

<img src="../../../../.gitbook/assets/image (896).png" alt="" data-size="original">

</details>

**Sau khi bạn đã kết nối được vào Windows server, bạn cần đảm bảo Windows server của bạn đã có địa chỉ IP tĩnh, bạn có thể kiểm tra và cấu hình IP tĩnh theo hướng dẫn sau:** 

* **Kiểm tra cấu hình mạng của VM bằng cách:**
  * Truy cập **Control Panel > Network & Internet > Network Connections**.
  * Chọn **Ethernet adapter**, nhấp chuột phải và chọn **Properties**.
* **Thiết lập địa chỉ IP tĩnh (Static IP):**
  * Trong màn hình **Properties**, chọn **Internet Protocol Version 4 (TCP/IPv4)** rồi bấm nút **Properties**.
  * Chọn **Use the following IP address** để thiết lập địa chỉ IP tĩnh.
  * Cung cấp thông tin địa chỉ:
    * **IP Address:** địa chỉ IP tĩnh của VM.
    * **Subnet Mask:** Subnet mask tương ứng, ví dụ nếu Subnet của bạn có CIDR: /24 thì Subnet Mask cần nhập là `255.255.255.0`.
    * **Default gateway:** địa chỉ default gateway phải nằm cùng trong Network với IP tĩnh của VM, và dựa trên Subnet Mask. Ví dụ: IP tĩnh là `10.50.3.9`, Subnet Mask là `255.255.255.0` thì Default gateway có thể là `10.50.3.1`
    * **Preferred DNS server:** địa chỉ IP của DNS Domain (thường cũng chính là địa chỉ IP tĩnh của VM)  (bạn có thể bổ sung sau khi đã khởi tạo DNS domain theo hướng dẫn bên dưới)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(923).png?raw=true)

***

## Khởi tạo Active Directory trên Windows Server

> **Chú ý:** 
>
> * Bạn bắt buộc cần sử dụng Administrator để thực hiện khởi tạo DNS Server cũng như Active Directory Domain Service theo hướng dẫn ở các bước bên dưới.

Để khởi tạo được Active Directory trên Windows Server, bạn cần thực hiện:

* **Cài đặt và cấu hình DNS Server**
* **Tạo Forward Lookup Zone**
* **Tạo Reverse Lookup Zone**
* **Kiểm tra DNS Name**
* **Cài đặt và cấu hình Active Directory**

Cụ thể, vui lòng thực hiện theo các bước bên dưới:

### Cài đặt và cấu hình DNS Server

Để cài đặt và cấu hình DNS Server trên Windows Server, bạn có thể làm theo các bước sau:

1. Từ màn hình **Desktop**, bạn mở **Start** menu và chọn **Server Manager.**
2. Chọn mục **All Servers,** chọn chuột phải sau đó chọn **Add roles and Features**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(897).png?raw=true)

3. Tại trang **Before you begin,** nhấn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(898).png?raw=true)

4. Tại trang **Installation Type**: Chọn **Role-based or feature-based installation** sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(3).png?raw=true)

5. Tại mục **Server Selection**: bạn chọn **Select a server from the server pool** và **chọn server hiện tại** sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(15).png?raw=true)

6. Tại mục **Server Roles**: Tick chọn **DNS Server** sau đó nhấn **Next** và **Install** để cài đặt.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(899).png?raw=true)

7. Lúc này, bạn sẽ được nhắc thêm các tính năng cần thiết cho DNS Server, chọn **Add Features** nếu bạn đồng ý với các mặc định.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(900).png?raw=true)

8. Tại trang **Confirmation**, kiểm tra lại các lựa chọn của bạn và nhấn Install để bắt đầu cài đặt DNS Server

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(1)%20(2).png?raw=true)

9. Sau khi việc cài đặt hoàn tất, bạn hãy nhấn **Close**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(6)%20(1)%20(2).png?raw=true)

### Tạo một Forward Lookup Zone 

Tiếp theo, bạn sẽ cần tạo một Forward Lookup Zone để chuyển domain thành địa chỉ IP. Cụ thể các bước thực hiện như sau: 

1. Thực hiện mở **DNS Manager** bằng cách chọn **Tools**, sau đó chọn **DNS**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(7)%20(1)%20(2).png?raw=true)

2. Trong DNS Manager, chọn vào DNS đang có và tiếp tục nhấp chuột phải vào **Forward Lookup Zones** và chọn **New Zone**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(8)%20(1).png?raw=true)

3. Màn hình Tạo zone mới hiển thị, tiếp tục chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(9)%20(6).png?raw=true)

4. Tại màn hình **Zone Type**: chọn **Primary zone,** sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(11)%20(4).png?raw=true)

5. Tại màn hình **Zone Name**: nhập tên domain của bạn và chọn **Next**. Ví dụ: `example.local`

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(13)%20(4).png?raw=true)

6. Tại màn hình **Zone File**, chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(24).png?raw=true)

7. Tại màn hình **Dynamic Update**: Chọn:

* **Allow only secure dynamic updates (Recommended for Active Directory):** nếu bạn đã có sẵn **Active Directory** integrate với **zone** của bạn. Nếu bạn chọn phương án này, **Window servers sẽ tự động tạo một** ********Reverse Lookup Zone******, bạn có thể bỏ qua các bước tại** ********Tạo một Reverse Lookup Zone**** ******bên dưới.**
* **Do not allow dynamic updates:** nếu bạn chưa có sẵn **Active Directory** nào integrate với **zone** của bạn. Nếu bạn chọn phương án này, bạn cần thực hiện **tạo Reverse Lookup Zone thủ công** theo hướng dẫn bên dưới. 
* Sau đó, bạn chọn **Next.** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1).png?raw=true)

8. Chọn **Finish** để hoàn thành việc tạo New Zone

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(15)%20(3).png?raw=true)

9. Sau khi chọn **Finish**, bạn sẽ thấy forwarding lookup zone trên màn hình chính như hình

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(16)%20(2).png?raw=true)

10. Sau khi tạo zone, bạn cần thêm bản ghi cho **Domain Controller** bằng cách chọn vào **Zone** vừa tạo, nhần chuột phải và chọn **New Host (A or AAAA)**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(17)%20(2).png?raw=true)

11. Tại màn hình **New Host,** bạn cần:

* **Name**: Nhập tên Windows server của bạn (VD: `demo-server-smb`).
* **IP Address**: Nhập địa chỉ IP tĩnh của Domain Controller (VD: `10.50.3.9`).
* Nhấn **Add Host**.

11. Nếu bạn chọn **Create associated pointer (PTR) record**, bạn cần phải tạo một **Reverse Loopup Zone**, các bước khởi tạo tương tự tạo **Forward Lookup Zone**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1).png?raw=true)

### Tạo một Reverse Lookup Zone

Nếu bạn chưa có sẵn **Active Directory** nào integrate với **zone** của bạn hoặc bạn muốn tự quản lý Reverse Lookup Zone, bạn có thể thực hiện tạo Reverse Lookup Zone theo hướng dẫn sau.

<details>

<summary>Khởi tạo Reverse Lookup Zone </summary>

Tiếp theo, bạn sẽ cần tạo một Reverse Lookup Zone để chuyển IP thành domain. Cụ thể các bước thực hiện như sau:

1. Thực hiện mở **DNS Manager** bằng cách chọn **Tools**, sau đó chọn **DNS**

<img src="../../../../.gitbook/assets/image (917).png" alt="" data-size="original">

2. Trong DNS Manager, chọn vào DNS đang có và tiếp tục nhấp chuột phải vào **Reverse Lookup Zones** và chọn **New Zone**

<img src="../../../../.gitbook/assets/image (2) (1) (1) (1).png" alt="" data-size="original">

3. Tại màn hình **Zone Type**: chọn **Primary zone,** sau đó chọn **Next**

<img src="../../../../.gitbook/assets/image (3) (1) (1) (1).png" alt="" data-size="original">

4. Màn hình Tạo zone mới hiển thị, chọn **IPv4 Reverse Lookup Zone** tiếp tục chọn **Next**

<img src="../../../../.gitbook/assets/image (4) (1) (1).png" alt="" data-size="original">

5. Tại màn hình **Reverse Lookup Zone Name**: nhập Network ID, Network ID tại đây chính là subnet của IP mà bạn cần thực hiện reverse lookup và chọn **Next**. Ví dụ: `10.50.3`.

<img src="../../../../.gitbook/assets/image (4) (1) (1) (1).png" alt="" data-size="original">

6. Tại màn hình **Zone File**, bạn có thể tạo Zone File mới hoặc chọn 1 Zone File đã có sẵn, sau đó chọn **Next**

<img src="../../../../.gitbook/assets/image (5) (1) (1).png" alt="" data-size="original">

7. Tại màn hình **Dynamic Update**: Chọn **Do not allow dynamic updates**, sau đó chọn **Next**

<img src="../../../../.gitbook/assets/image (6) (1) (1).png" alt="" data-size="original">

8. Chọn **Finish** để hoàn thành việc tạo New Zone

<img src="../../../../.gitbook/assets/image (7) (1).png" alt="" data-size="original">

9. Sau khi chọn **Finish**, bạn sẽ thấy Reverse lookup zone trên màn hình chính như hình

<img src="../../../../.gitbook/assets/image (11).png" alt="" data-size="original">

10. Sau khi tạo xong **reverse lookup zone**, bạn cần tạo **Pointer (PTR)** bằng cách chọn vào **Zone** vừa tạo, nhần chuột phải và chọn **New Pointer (PTR)**

<img src="../../../../.gitbook/assets/image (16).png" alt="" data-size="original">

11. Tại màn hình **New Resource Record,** bạn cần:
    1. **Host IP Address**: Nhập địa chỉ IP tĩnh của Domain Controller (VD: `10.50.3.9`).
    2. **Host Name:** Nhập tên Windows server của bạn (VD: `demo-smb`).
    3. Nhấn **OK**.

<img src="../../../../.gitbook/assets/image (10).png" alt="" data-size="original">



</details>

### Kiểm tra DNS name 

Trên Windows server của bạn, mở Command Prompt và chạy:

```bash
nslookup <DNS Domain>
hoặc
nslookup <IP Address>
```

Ví dụ: 

```bash
nslookup example.local
hoặc
nslookup 10.50.3.9
```

Kết quả hiển thị ví dụ như sau: 

```bash
nslookup example.local
---
Server: demo-smb
Address: 10.50.3.9
Name: example.local

nslookup 10.50.3.9
---
Server: demo-smb
Address: 10.50.3.9
```

### Cài đặt và cấu hình Active Directory Domain Services

Để cài đặt và cấu hình Active Directory Domain Service trên Windows Server, bạn có thể làm theo các bước sau:

1. Từ màn hình **Desktop**, bạn mở **Start** menu và chọn **Server Manager**
2. Chọn mục **All Servers,** chọn chuột phải sau đó chọn **Add roles and Features**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(877).png?raw=true)

3. Tại mục **Before You Begin**, chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(878).png?raw=true)

4. Tại mục **Installation Type**: Chọn **Role-based or feature-based installation** sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(879).png?raw=true)

5. Tại mục **Server Selection**: bạn chọn **Select a server from the server pool** và **chọn server hiện tại** sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(17).png?raw=true)

6. Tại mục **Server Roles**: Tick chọn **Active Directory Domain Services.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(18).png?raw=true)

7. Lúc này, bạn sẽ được nhắc thêm các tính năng cần thiết cho Active Directory, chọn **Add Features** nếu bạn đồng ý với các mặc định, sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(880).png?raw=true)

8. Tại trang **Feature**, giữ các thông số mặc định và chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(882).png?raw=true)

9. Tại trang AD DS, chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(883).png?raw=true)

10. Tại trang **Confirmation**, kiểm tra lại các lựa chọn của bạn và nhấn **Install** để bắt đầu cài đặt AD DS

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(884).png?raw=true)

11. Sau khi chọn **Install**. Hệ thống sẽ bắt đầu cài đặt, bạn không cần khởi động lại server ngay sau khi cài đặt.
12. Khi việc cài đặt hoàn thành, bạn chọn tiếp **Promote this server to a domain controller**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(885).png?raw=true)

13. Tại màn hình **Deployment Configuration**, chọn **Add a new forest** sau đó nhập **DNS domain name** đã tạo (****chính là Zone name đã tạo tại bước Tạo một Forward Lookup Zone****) sau đó chọn **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(887).png?raw=true)

14. Tại màn hình **Domain Controller Options**, bạn hãy nhập **Password** và **Confirm Password** cho DSRM của bạn

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(888).png?raw=true)

15. Tại mục DNS Option, bạn bỏ qua và chỉ nhần **Next**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(889).png?raw=true)

16. Tại mục **Additional Options**, bạn hãy kiểm tra lại **NetBIOS name** và thay đổi nếu bạn thấy cần thiết sau đó chọn **Next. NetBIOS domain name** là domain rút gọn của Root domain name, 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(890).png?raw=true)

17. Tại màn hình **Paths**, bạn có thể thay đổi các đường dẫn tới **Database folder, Log file folder, Sysvol** hoặc giữ như mặc định của hệ thống, sau đó chọn Next

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(891).png?raw=true)

18. Tại màn hình **Review Options**, bạn hãy review lại các thông số và chọn **Next** nếu thông tin đã đúng

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(892).png?raw=true)

19. Tại màn hình **Prerequisites Check**, bạn sẽ thấy kết quả kiểm tra, tiếp tục chọn **Install** để hệ thống cài đặt AD

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(893).png?raw=true)

20. Sau khi quá trình cài đặt hoàn thành, hệ thống sẽ tự động khởi động lại server của bạn, bạn cần login lại vào server với tài khoản **Administrator**

> **Chú ý:**
>
> * Bạn có thể thực hiện phân quyền cho tài khoản AD hoặc nhóm thông qua tính năng cấp quyền truy cập qua Group Policy hoặc ACL. Cụ thể, tham khảo thêm tại [đây](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/active-directory-overview).

### Lấy thông tin DNS Domain Name, AD Domain Name

Bạn có thể sử dụng câu lệnh bên dưới để lấy thông tin DNS Domain Name, AD Domain Name đã khởi tạo, bạn có thể sử dụng PowerShell trên window servers thông qua lệnh: 

* Lấy thông tin **DNS Domain Name:** 

```powershell
Get-DnsClientGlobalSetting
```

* Lấy thông tin **AD Domain Name:** 

```powershell
(Get-WmiObject Win32_ComputerSystem).Domain
```

***

## Khởi tạo File Storage

**Bước 1:** Truy cập vào [https://efs.console.vngcloud.vn/overview](https://efs.console.vngcloud.vn/overview)

**Bước 2:** Chọn mục **File Storage** sau đó chọn **Create a File storage.**

**Bước 3:** Tại màn hình khởi tạo File Storage, bạn cần nhập/ chọn: 

* **File Storage name:** tên gợi nhớ của file storage. Tên file cần dài từ 5 tới 50 ký tự và có thể bao gồm các ký tự a-z, A-Z, 0-9, '-', '\_'
* **Description**: nhập mô tả cho file storage.
* **File storage type:** chọn loại ổ đĩa mà bạn mong muốn sử dụng. Hiện tại chúng tôi chỉ cung cấp loại ổ đĩa **Standard HDD.**
* **Protocol:** chọn NFS và version NFS mà bạn mong muốn
* **Tag:** bạn có thể thêm các tag để đánh dầu file storage theo nhu cầu.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(1)%20(2)%20(1).png?raw=true)

* **File Storage Max quota:** trong bước khởi tạo file storage, bạn cần đặt một giới hạn quota tối đa cho file storage đó. Quota này có ý nghĩa chính là giới hạn dung lượng lưu trữ mà file storage có thể sử dụng, giúp quản lý tài nguyên hiệu quả. ****Mức quota tối thiểu bạn cần chọn là 1 TB và mức quota tối đa chúng tôi cung cấp là 50 TB.**** Nếu bạn có nhu cấu sử dụng nhiều hơn 50 TB cho một file storage, vui lòng liên hệ với chúng tôi.
* **Network type**: đối với loại file SMB, network type bắt buộc phải là Private. Lúc này, bạn cần chọn **VPC**, **Subnet** mà bạn đã khởi tạo từ vServer Portal.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(904).png?raw=true)

* **Window Authentication: c**ấu hình quyền truy cập thông qua **Active Directory Authentication**
  * **Active Directory Authentication:** Nếu Windows server của bạn sử dụng Active Directory để quản lý người dùng và quyền truy cập, thì AD Authentication sẽ dễ dàng tích hợp và quản lý tập trung. Bạn có thể xác thực thông qua Active Directory domain name, DNS server IP addresses, Username, Password trên Active Directory của bạn. Ví dụ, ứng với Avtive Directory đã tạo bên trên, tôi sẽ nhập vào:
    * **Active Directory domain name**: nhập thông tin AD Domain name của bạn, bạn có thể lấy thông tin này theo hướng dẫn ở bên trên. Ví dụ `example.local`
    * **DNS server IP Address**: Địa chỉ địa chỉ IP DNS Server, thường cũng chính là địa chỉ IP tĩnh của VM, ví dụ: `10.50.3.9.`Nếu bạn có 2 DNS IP, bạn có thể nhập theo mẫu `10.50.3.3,10.50.3.9`
    * **Username:** Tên tài khoản admin, ví dụ `Administrator`
    * **Password**: Mật khẩu bạn đã tạo ở bước **Cài đặt và cấu hình Active Directory Domain Services**, ví dụ: `123456789aA@`
    * **Confirm Password:** Xác nhận mật khẩu, ví dụ: `123456789aA@`

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(7)%20(1)%20(2)%20(1).png?raw=true)

**Bước 5:** Chọn **Create File Storage.**

**Bước 6:** Sau khi hệ thống khởi tạo xong File Storage SMB, bạn có thể lấy thông tin **File Storage IP Address** tại phần thông tin chi tiết của File Storage và tiếp tục thực hiện các bước bên dưới

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(21).png?raw=true)

***

## Map File Storage vừa khởi tạo tới Windows server 

Trên Windows Server, bạn có thể map file storage SMB thông qua giao diện hoặc dòng lệnh.

### **Qua giao diện**

1. **Mở File Explorer.**
2. Nhấp chuột phải vào **This PC** và chọn **Map network drive**.
3. Trong cửa sổ **Map Network Drive**:
   1. **Drive letter**: Chọn một ký tự ổ đĩa (VD: `Z:`).
   2. **Folder**: Nhập đường dẫn SMB share, ví dụ: `\\<File Storage IP Address>\<File Storage Name>`. Ví dụ `\\10.50.3.8\demo-smb`.
   3. Chọn **Finish**, sau khi hoàn tất, bạn có thể kiểm tra trong **File Explorer** để thấy ổ đĩa được map.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(22).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(23).png?raw=true)

> **Chú ý:**
>
> * Để tự động map file storage SMB mỗi lần khởi động Windows Server, bạn có thể lưu thông tin khi map qua giao diện bằng cách tích vào ô **Reconnect at sign-in** trước khi nhấn **Finish**.

### **Qua dòng lệnh**

Sử dụng lệnh sau trong **Command Prompt** hoặc **PowerShell**:

```cmd
net use Z: \\<File Storage IP Address>\<File Storage Name> 
```

* **Z:**: Là ký tự ổ đĩa mà bạn muốn gắn.
* **\\\\\<File Storage IP Address>\\\<File Storage Name>**: Đường dẫn File Storage SMB.

Ví dụ:

```cmd
net use Z: \\10.50.3.8\demo-smb
```

### Qua trực tiếp File Explorer

Đơn giản hơn, bạn cũng có thể truy cập trực tiếp tới File Storage SMB qua File Explorer qua các bước:

1. Mở **File Explorer**: Nhấn tổ hợp phím **Windows + E** hoặc nhấp vào biểu tượng File Explorer.
2. Nhập **UNC Path**: Trên thanh địa chỉ, nhập đường dẫn UNC đến file share. Ví dụ:

```
\\10.50.3.8\demo-smb
```

3. Nhấn **Enter**.

***

## Write data tới File Storage

Sau khi bạn đã **map File Storage SMB** vào Windows Server thành công, bạn có thể thực hiện việc ghi dữ liệu (write data) tới File Storage như sau:

1. **Mở trình soạn thảo văn bản (Notepad):**
   * Trên Windows Server, mở **Notepad** bằng cách:
     * Nhấn **Start** và gõ **Notepad**, sau đó nhấn **Enter**.
   * Hoặc, nhấn tổ hợp phím **Windows + R**, nhập `notepad` và nhấn **Enter**.
2. **Viết nội dung vào file:**
   *   Trong Notepad, nhập một nội dung đơn giản, ví dụ:

       ```
       Đây là file test ghi vào SMB share.
       ```
   * Hoặc nhập bất kỳ nội dung nào bạn muốn.
3. **Lưu file vào file storage SMB:**
   * Nhấn **File > Save As...**.
   * Trong hộp thoại **Save As**, điều hướng đến ổ đĩa mà bạn đã map SMB share (VD: `Z:`).
   * Đặt tên file (VD: `testfile.txt`).
   * Nhấn **Save** để lưu file.
4. **Kiểm tra file trong SMB share:**
   * Mở **File Explorer** (phím tắt: **Windows + E**).
   * Điều hướng đến ổ đĩa SMB (VD: `Z:`).
   * Tìm và mở file `testfile.txt` mà bạn vừa lưu để xác minh nội dung
