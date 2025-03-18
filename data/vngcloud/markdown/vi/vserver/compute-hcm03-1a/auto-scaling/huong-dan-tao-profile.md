# Hướng dẫn tạo profile

Truy cập vào dịch vụ Bandwidth tại đường link: [https://portal3.vngcloud.vn/auto-scale#/profiles/list.html](https://portal3.vngcloud.vn/auto-scale#/profiles/list.html), sau đó nhấn **Create Profile.**

**Bước 1: Tạo template cho instance**. 

Tại đây bạn sẽ define các giá trị cấu hình của 1 instance mà mình muốn auto-scaling group sẽ tạo thêm / giảm bớt khi thực hiện scaling.  

Tạo template sẽ gồm các thông tin là: Profile / instance name, Image, Flavor, Volume, Network 

Các bước dưới đây sẽ mô tả cách nhập thông tin cho template 

* Profile & Instance name:  

Tại Profile information, click chọn và đặt tên cho profile &  instance, lưu ý chỉ đặt các ký tự A->Z hoặc số. Tên profile và instance giới hạn từ 6-20 ký tự 

* **IMAGE:** Chọn trong danh sách OS có sẵn   

Bạn cũng có thể chọn danh sách Image bạn đã tạo (Xem hướng dẫn [Tạo Image cho Server](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/image)) 

* **FLAVOR** 
* **VOLUME** 
* **NETWORK**

Tương ứng với các thông số bạn chọn cho template, bạn có thể xem giá tham khảo ở góc trái với các thông tin như hình dưới  

Lưu ý đây chỉ là giá tham khảo cho profile, VNDT sẽ không lấy bất kỳ phí gì khi bạn tạo profile (template). Phí phải trả khi sử dụng auto-scaling sẽ tính dựa vào thực tế sử dụng của bạn (tổng số phút instance scale) và thanh toán vào cuối tháng. (Xem thêm tại phần phí auto-scaling)  

Sau khi đã nhập đầy đủ các thông tin cho template, chọn vào Next để qua bước 2 profile information  

**Bước 2: Profile information (Optional)** 

Các thông tin ở bước 2 không bắt buộc, bạn có thể bỏ qua nếu không có nhu cầu sử dụng.  

**Bước 3: Summary**  

Xem lại các thông tin đã tạo, nếu không có vấn đề gì chọn create profile. Lưu ý: bạn sẽ không bị charge bất kỳ phí gì khi tạo profile. 

Sau khi tạo thành công, bạn sẽ thấy profile mới tạo hiển thị ở giao diện profile management  

Nếu bạn muốn xem thông tin chi tiết của profile, nhấp vào ô vuông tickbox bên trái tên profile 

\
