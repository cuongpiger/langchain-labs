# Kết nối MDS Instance

Để kết nối với DB Instance có **Database Engine** là Redis, bạn có thể sử dụng redis-cli, hay các thư viện redis client của các ngôn ngữ lập trình như jedis, redis-py,...

Nếu muốn truy cập bằng giao diện, bạn có thể tham khảo tool AnotherRedisDesktopManager tải tại link sau:

[https://www.electronjs.org/apps/anotherredisdesktopmanager](https://www.electronjs.org/apps/anotherredisdesktopmanager)

sau đó thực hiện theo video hướng dẫn (bắt đầu ở 1:00):

[Video](https://youtu.be/1kvJi3Hg4wM)

Nếu sử dụng tool cli, bạn có thể làm theo bài viết sau sử dụng **redis-cli**.

Để sử dụng redis-cli, trên Linux bạn có thể tải source và build như sau:

| `wget http://download.redis.io/redis-stable.tar.gztar xvzf redis-stable.tar.gzcd redis-stablemake distclean // Ubuntu systems onlymakesudo make install` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |

* [Bước 1. Xác định thông tin Endpoint & Port để truy cập:](https://docs.vngcloud.vn/vng-cloud-document/vn/vdb/memorystore-database-service-mds/ket-noi-mds-instance#ketnoimdsinstance-buoc1.xacdinhthongtinendpoint-and-portdetruycap)
* [Bước 2: Tùy chỉnh Security Group Rules để bảo vệ DB Instance (tùy chọn)](https://docs.vngcloud.vn/vng-cloud-document/vn/vdb/memorystore-database-service-mds/ket-noi-mds-instance#ketnoimdsinstance-buoc2-tuychinhsecuritygrouprulesdebaovedbinstance-tuychon)
* [Bước 3. Kết nối bằng redis-cli](https://docs.vngcloud.vn/vng-cloud-document/vn/vdb/memorystore-database-service-mds/ket-noi-mds-instance#ketnoimdsinstance-buoc3.ketnoibangredis-cli)

### Bước 1. Xác định thông tin Endpoint & Port để truy cập: 

Tại giao diện quản lý Database, bạn chọn vào MemoryCache Database instance vừa tạo, chọn đến tab **Connectivity & Security**, xem tại mục **Endpoint & Port**. Vì lí do bảo mật, các MDS Instance chỉ có một Endpoint Private. Bạn chỉ có thể kết nối tới từ một vServer chung Network hoặc từ các Network có mở ACL tới.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

Ngoài ra, bạn cũng có thể thiết lập một SSH Tunnel trên một vServer chung Network với MDS Instance này và kết nối từ xa thông qua Internet. 

### Bước 2: Tùy chỉnh Security Group Rules để bảo vệ DB Instance (tùy chọn) 

Mục **Security Group Rules** cho phép bạn giới hạn những **Remote IP** nào được phép truy cập vào DB Instance của bạn. Để tiện lợi cho việc sử dụng, khi vừa khởi tạo, VNG Cloud cho phép bạn truy cập không hạn chế từ mọi nơi (0.0.0.0/0) vào DB Instance. Tuy nhiên, VNG Cloud khuyến nghị bạn tùy chỉnh lại mục này sao cho chỉ những **Remote IP** tin cậy được truy cập vào.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Để thay đổi, bạn chọn vào **EDIT** và điền IP (theo chuẩn CIDR) thích hợp. Bên cạnh đó bạn cũng có thể nhấn **ADD RULE** để thêm những RULE mới.
* Sau khi hiệu chỉnh, nhấn **Save** và chờ một lát để thay đổi được lưu lại.
* Để chắc chắn kết nối được thông suốt, bạn có thể dùng các công cụ kiểm tra như telnet.

Khi kết nối đã thông suốt, bạn có thể tiến hành kết nối tới DB Instance.

### Bước 3. Kết nối bằng redis-cli 

Sau khi có thông tin endpoint, bạn có thể kết nối tới thông qua IP & Port.

VD: DB Instance có IP: `10.23.0.5`, port: 6379, bạn kết nối bằng redis-cli như sau:

| <p><code>$ redis-cli -h 10.23.0.5 -p 6379</code><br><br><code>10.23.0.5:6379></code></p> |
| ---------------------------------------------------------------------------------------- |

Chúc mừng bạn đã truy cập thành công.
