# Customer Managed Key

### Tạo mới customer managed key

* Tại portal KMS, chọn menu “Customer keys” để vào danh sách customer managed key
* Chọn “Tạo Key” và thực hiện theo hướng dẫn trên màn hình tạo key

\-        Nhập thông tin key gồm: Tên Key, Diễn giải, Tag

\-        Nhập thông tin cấu hình Key gồm: Loại key, Key Usage và Key Spec

\-        Nguồn Key Material: Người dùng chọn nguồn = VNGCLOUD

                a.      VNGCLOUD: Key material được tạo trên VNG Cloud KMS

                b.     External: Người dùng tự quản lý Key Material và import vào VNG Cloud KMS cho việc sử dụng trong các dịch vụ của VNG Cloud.

* Nhấn “Tạo Key” để thực hiện tạo Key.

  \- Với Key có nguồn key material = VNGCLOUD, sau khi tạo thành công, Key có status = “Đang hoạt động”.

  \- Với Key có nguồn key material = External sau khi tạo thành công, Key có status = Pending Import. Bước tiếp theo thực hiện theo hướng dẫn ở phần “Chờ nhập nội dung key”.

### Xem danh sách key và thông tin chi tiết Key

* Vào menu “Customer keys” để xem danh sách Key do người dùng tạo
* Vào menu “VNG Cloud Keys” để xem danh sách Key do VNG Cloud tạo theo yêu cầu người dùng
* Để xem thông tin chi tiết key, người dùng tìm và di chuyển đến dòng chứa thông tin key muốn xem chi tiết và nhấn vào liên kết tại tên key.

### Xóa Key

Người dùng chỉ có thể xóa được key thuộc loại “Customer Managed Key”

* Vào menu “Customer keys”, tìm và chọn key muốn xóa. Nhấn “Xóa key”.
* KMS sẽ thông báo ảnh hưởng khi xóa key, Người dùng điền thông tin thời gian chờ để xóa key. Thời gian chờ nằm trong khoảng từ 7 đến 30 ngày.
* Nhấn “Xóa”
* Key sẽ được chuyển trạng thái sang “Chờ xóa”. Key sẽ được xóa khỏi hệ thống khi hết thời gian chờ. Trong trường hợp thay đổi quyết định, người dùng có thể dùng chức năng “Hủy xóa key”.

Với những trường hợp key đang trong giai đoạn chờ xóa, người dùng có thể thay đổi quyết định bằng cách dùng chức năng “Hủy xóa key”.

* Vào menu “Customer keys”, tìm và chọn key có trạng thái “Chờ xóa”
* Nhấn chọn “Hủy xóa key”.
* Key khi này được chuyển về trạng thái “Không hoạt động”. Người dùng có thể chuyển về trạng thái “Đang hoạt động” để sử dụng key bằng cách dùng chức năng “Enable” key.

### Enable Key.

Áp dụng với những trường hợp key không hoạt động cần sử dụng.

* Vào menu “Customer keys”, tìm và chọn key có trạng thái “Không hoạt động”
* Nhấn vào liên kết tại tên Key
* Nhấn vào nút lệnh Enable để bật trạng thái Key = Đang hoạt động

Trong trường hợp không có gói key nào đang active, người dùng không thể enable key có trạng thái “Không hoạt động”.

### Import Key Material

> Người dùng có thể import key material nhiều lần tuy nhiên key material phải giống nhau giữa các lần import

 VNG Cloud KMS hỗ trợ import nội dung key (key Material) của hai loại khóa 

* Khóa đồng bộ (Symmetric Key) 
* Khóa bất đồng bộ (Asymmetric Key) 

Để import key người dùng thực hiện theo thứ tự sau: 

 1\.      Đăng nhập vào VNG Cloud console tại Link 

2\.      Chọn Menu “Customer Keys” 

3\.      Chọn Key ID muốn tải Public Key và Import Token. Trong trường hợp Master Key chưa được tạo, người dùng có thể tham khảo hướng dẫn tạo master key. 

4\.      Chọn tab “Cấu hình mã hóa”để xem thông tin chi tiết key đồng thời kiểm tra chắc chắn key có nguồn (Origin) = External, là những key mà người dùng có thể import Key Material. 

5\.      Chọn tab “Key Material” để xem thông tin chi tiết Key material. Chọn “Import Key Materials” 

6\.      Nếu người dùng muốn tải Wrapping Public Key và Import Token (Bước 1 của qui trình import nội dung key). Thực hiện theo thứ tự sau: 

     o   Chọn loại mã hóa (Wrapping Key Spec) 

     o   Chọn thuật toán mã hóa (Wrapping Algorithm) 

     o   Chọn “Tải Wrapping Public Key và Import Token” 

7\.      Upload nội dung key vào KMS (Bước 2 của qui trình import nội dung key) 

     o   Tại khu vực “Wrapped Key Material” Chọn file chứa key material đã mã hóa để tải lên. Để thực hiện tạo Key material và đóng gói thực hiện theo hướng dẫn tại mục “Tạo và đóng gói nội dung Key” 

     o   Tại khu vực “Import Token” Chọn file import token để tải lên 

     o   Trong trường hợp muốn thiết lập ngày hết hạn của Key material, check chọn “Expiration” và điền thông tin ngày hết hạn của Key Material. Bỏ qua phần này nếu không muốn thiết lập ngày hết hạn cho nội dung key đã import. 

8\.      Nhấn “Submit” để hoàn thành quá trình import. 

###  Hướng dẫn tạo và đóng gói nội dung Key: 

#### Khóa đồng bộ (Symmetric Key) 

bước 1: Generate a 32-byte AES symmetric encryption key 

```
openssl rand -out PlaintextKeyMaterial.bin 32  
```

bước 2: Dùng wrapping public Key để mã hóa nội dung key (Key Material) 

2.1 RSAES-OAEP-SHA-256 

```
openssl pkeyutl -encrypt -inkey WrappingPublicKey.pem -pubin -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -in PlaintextKeyMaterial.bin -out EncryptedKeyMaterial.bin 
```

 2.2 RSA\_AES\_KEY\_WRAP\_SHA\_1: 

```
openssl pkeyutl -encrypt -inkey WrappingPublicKey.pem -pubin -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha1 -in PlaintextKeyMaterial.bin -out EncryptedKeyMaterial.bin
```

####   Khóa bất đồng bộ (Asymmetric Key) 

 Bước 1: Tạo khóa AES ngẫu nhiên 

```
openssl rand -out aes_key.bin 32 
```

Bước 2: Tạo khóa Private key của riêng mình 

```
openssl genpkey -algorithm RSA -out my_private_key.pem -pkeyopt rsa_keygen_bits:4096
```

Bước 3: Mã hóa khóa AES bằng khóa RSA công khai 

3.1 Wrapping algorithm: RSA-AES-KEY-WRAP-SHA-256 

```
openssl pkeyutl -encrypt -inkey WrappingPublicKey.pem -pubin -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -in aes_key.bin -out aes_key_wrapped.bin
```

3.2 Wrapping algorithm: RSA-AES-KEY-WRAP-SHA-1 

```
openssl pkeyutl -encrypt -inkey WrappingPublicKey.pem -pubin -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha1 -in aes_key.bin -out aes_key_wrapped.bin
```

Bước 4: Mã hóa Private key bằng khóa AES 

```
openssl enc -aes-256-cbc -salt -in my_private_key.pem -out my_private_key_wrapped.bin -pass file:aes_key.bin -pbkdf2 -iter 10 
```

Bước 5: Tiến hành ghép các tập tin mã hóa lại với nhau 

```
cat aes_key_wrapped.bin my_private_key_wrapped.bin > EncryptedKeyMaterial.bin 
```

