# Tạo mới Public NAT



> **Lưu ý quan trọng**
>
> * _**NAT và VM đi qua NAT ra internet phải cùng subnet**_
> * _**Public interface của NAT được tạo tự động khi NAT được tạo thành công, người dùng có thể cấu hình public IP vào các gói**_ [_**bandwidth**_](https://docs.vngcloud.vn/vng-cloud-document/v/vn/vserver/compute-hcm03-1a/network/bandwidth-hcm-03/dich-vu-datatransfers-bandwidth) _**đã mua (nếu có) để tăng băng thông cho NAT.**_
> * _**NAT chỉ kết nối với internet qua port 53, 80, 443 và các gói tin** ********icmp.**** ******Trong trường hợp cần hỗ trợ các port khác, khách hàng có thể chỉnh sửa tại trang Detail, tham khảo**_ [_**tại đây**_](https://docs.vngcloud.vn/vng-cloud-document/vn/vnetwork/public-nat-instance/them-xoa-nat-port)
> * _**Trong trường hợp muốn phân giải DNS, người dùng phải đảm bảo** ********route**** ******ở trên được cấu hình chính xác đi qua gateway NAT cho IP Resolver**_

* Người dùng login vào [https://hcm-3-vnetwork.console.vngcloud.vn/nat/list](https://hcm-3-vnetwork.console.vngcloud.vn/nat/list) với region = HCM
* Chọn menu “**Public NAT Instance**” tại thanh menu bên trái màn hình
* Chọn chức năng “**Create a Public NAT**”
* Nhập thông tin NAT theo yêu cầu gồm:
  * Tên NAT
  * Gói dịch vụ
  * VPC, Subnet
* Kiểm tra thông tin giá dịch vụ tại phần “**Summary**”
*  Nhấn “**TẠO PUBLIC NAT**”

Khi NAT được tạo thành công, người dùng sẽ thấy NAT xuất hiện trên màn hình danh sách NAT.

Người dùng cần thực hiện bước cấu hình các VM nào sẽ đi qua NAT bằng cách sử dụng NAT IP gateway theo cú pháp của OS Linux

_`ip route add <internet_ip> via <nat_gateway_ip> dev <interface>`._

* `<internet_ip>`: IP internet, ví dụ : 0.0.0.0/0 hoặc default
* `<nat_gateway_ip>`: IP gate way được cung cấp trên màn hình chi tiết thông tin NAT sau khi NAT được tạo thành công
* dev `<interface>`: Device private interface của VM kết nối với NAT 

Dưới đây là ví dụ add route trên VM với OS Linux theo cú pháp ở trên: 

_`ip route add 0.0.0.0/0 via 10.0.0.100 dev eth0`_

**Trong trường hợp đã tồn tại route ra internet thông qua một gateway IP khác thì người dùng phải phải remove route hiện tại và add route mới đến NAT gateway IP.** 

_**Dưới đây là một ví dụ về route ra internet đã tồn tại qua một gateway IP khác trên OS Linux**_

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(712).png?raw=true)

_**Sau khi xóa route đã tồn tại trên VM, add lại route ra internet qua NAT**_

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(708).png?raw=true)

_**Kết quả thành công như hình**_

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(709).png?raw=true)



