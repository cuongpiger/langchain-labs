# Live Streaming

## **Tổng quan** 

Dịch vụ hỗ trợ phát nội dung trực tiếp như sự kiện, chương trình truyền hình, và thể thao đến nhiều người dùng qua nền tảng internet với chất lượng cao và ổn định.

***

## Sơ đồ hoạt động

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(207).png?raw=true)

**Cơ Chế Phân Phối Dữ Liệu**

Sử dụng phương pháp [PU](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/tong-quan/kien-truc-tong-quan/co-che-phan-phoi-du-lieu/phuong-phap-pull)[LL](https://docs.vngcloud.vn/display/ONVINA/Live+Streaming#\_Ph%C6%B0%C6%A1ng\_ph%C3%A1p\_PULL), [PUS](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/tong-quan/kien-truc-tong-quan/co-che-phan-phoi-du-lieu/phuong-phap-push)[H](https://docs.vngcloud.vn/pages/viewpage.action?pageId=36045441) chọn tín hiệu đầu vào và tín hiệu đầu ra, đảm bào đường truyền tốt nhất, ổn định nhất, nhiều điểm truy cấp nhất cho dịch vụ live.

***

## **Tính Năng Dịch Vụ** 

* **Tùy chọn thời gian chunk size**: Giúp tối ưu caching và phân phối nội dung.
* **Hỗ trợ multi-Origin**: Cho phép tích hợp nhiều nguồn khi tạo CDN.
* **Kết nối HTTPS đến Origin**: Đảm bảo bảo mật khi truyền dữ liệu.
* **Bảo mật link đầu ra**:
  * Tùy chỉnh caching phù hợp với từng loại nội dung.
  * Hỗ trợ **CNAME** cho CDN.
* **Quản lý tín hiệu Live Entrypoint**: Dễ dàng theo dõi và quản lý tín hiệu đầu vào.
* **Hỗ trợ Adaptive Bitrate (ABR)**:
  * Mã hóa video nguồn với nhiều tốc độ bit khác nhau.
  * Codec video phổ biến: **H.264/AVC** và **H.265/HEVC**.
  * Codec âm thanh phổ biến: **AAC**.
  * Đáp ứng nhiều loại băng thông người dùng trực tuyến.

***

## Hướng dẫn khởi tạo Live Stream CDN 

### **Bước 1: Tạo Live Entrypoint**

Đầu tiên, bạn cần thực hiện khởi tạo một Live Entrypoint theo hướng dẫn sau: 

1. Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)
2. Chọn mục **Live Entrypoint**, sau đó chọn **Create new.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(832).png?raw=true)

3. Tiếp tục thực hiện nhập/chọn: 

* **Live Entrypoint Configuration:**
  * **Live Entrypoint name:** Tên của Live Entrypoint, dùng để xác định tín hiệu đầu vào trên hệ thống.
  * **Description:** Mô tả ngắn gọn về Live Entrypoint, giúp quản lý và nhận biết dễ dàng.
*   **Publish and Media Configuration:**

    * **Live app:** Tên ứng dụng phát live. Đây là một định danh quan trọng để phân biệt các luồng tín hiệu trong hệ thống.
    * **TimeShift:** Cho phép người xem tua lại nội dung live trong khoảng thời gian ngắn (mặc định VCDN hiện tại chỉ hỗ trợ 30 phút). Bạn có thể chọn **Bật/tắt** sử dụng tùy nhu cầu.
    * **Security Configuration:**
      * **Publish IP(s):** Danh sách các địa chỉ IP được phép gửi tín hiệu RTMP đến hệ thống. Bạn cần nhập IP của thiết bị hoặc server gửi tín hiệu. Nếu không nhập đúng IP, hệ thống sẽ chặn tín hiệu. Nếu không nhập IP, bạn bắt buộc cần nhập Username và Password theo hướng dẫn bên dưới.
      * **User Name, Password:** Thông tin xác thực để bảo vệ tín hiệu RTMP. Bạn cần nhập username và password để bảo mật tín hiệu RTMP đầu vào.

    ****Lưu ý:**** ******Bạn phải nhập ít nhất một trong hai mục** ********Publish IP(s)**** ******hoặc** ********Username/Password******, hoặc có thể nhập cả hai.**

    * **Entrypoint Zone:** 
      * **Primary Zone:** Nhà cung cấp dịch vụ chính nhận tín hiệu RTMP (VD: Viettel, VNPT, VNG HCM). Bạn cần chọn ISP phù hợp với tín hiệu của bạn. Trong đó **RTMP URL**: Đường dẫn để push tín hiệu RTMP đến ISP chính.
      * **Backup Zone:** Nhà cung cấp dự phòng nếu tín hiệu từ Primary Zone gặp sự cố. Bạn cần chọn ISP dự phòng từ danh sách (hoặc chọn "Not Use" nếu không cần dự phòng).
    * **Media Config:**
      * **Media Type:** Định dạng nội dung live stream, vCDN hiện tại chỉ hỗ trợ định dạng **HLS**. 
      * **Segment Size:** Thời gian đóng gói mỗi phân đoạn tín hiệu RTMP thành file HLS hoặc DASH. Bạn cần chọn giá trị phù hợp (2s, 4s, 6s, 10s). Giá trị nhỏ giúp giảm độ trễ nhưng tăng tải hệ thống.

4. Chọn **Submit**.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(834).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(836).png?raw=true)

### **Bước 2: Tạo Live Streaming**

Tiếp theo, bạn cần thực hiện khởi tạo một Live Streaming theo hướng dẫn sau: 

1. Truy cập vào vCDN Portal tại [https://vcdn.vngcloud.vn](https://vcdn.vngcloud.vn/live-entrypoint/list.html)
2. Chọn mục **Live Streaming**, sau đó chọn **Create new.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(837).png?raw=true)

3. Tiếp tục thực hiện nhập/ chọn: 

* **CDN Info:**
  * **CDN Name**: Tên của CDN Live Streaming, dùng để nhận diện khi quản lý các luồng CDN.
  * **Type**: Lựa chọn loại dịch vụ CDN cho Live Streaming. Bạn có thể lựa chọn: 
    * **CDN Packaging**: Hệ thống sẽ xử lý "đóng gói" (packaging) nội dung trực tiếp trên CDN. Hãy chọn CDN Packaging nếu bạn muốn hệ thống tối ưu thời gian xử lý và giảm tải từ nguồn.
    * **Origin Packaging**: Đóng gói nội dung tại nguồn (Origin), sau đó CDN chỉ truyền tải.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(838).png?raw=true)

* **CDN Configuration**
  * **Live Entrypoint**: Lựa chọn Live Entrypoint đã tạo từ **bước 1** trước làm nguồn dữ liệu.
  * **Channel:** Định danh của kênh phát live trên hệ thốngs.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(839).png?raw=true)

* **Security:**
  * **HTTPS (HTTP/2)**: Bật hoặc tắt chế độ bảo mật HTTPS cho luồng CDN. Bạn có thể tạo mới một **Certificate** bằng cách chọn **Add new**.
  * **Minimum TLS Version**: Phiên bản thấp nhất của giao thức TLS được phép sử dụng. Chúng tôi đang hỗ trợ các giao thức TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3. Bạn hãy chọn sử dụng các phiên bản cao (TLS 1.2 hoặc 1.3) để đảm bảo tính bảo mật.
  * **Token Configuration**:
    * **Token Type**: Chọn loại token dùng để xác thực người xem. Bạn có thể chọn token type Akamai, SBD hoặc VNG.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(840).png?raw=true)

* **Access Filter:**
  * **IP Address CIDR**: Giới hạn cho phép/ từ chối truy cập dựa trên địa chỉ IP bằng cách chọn **Allow**/ **Block** và nhập địa chỉ IP hoặc CIDR tương ứng.
  * **HTTP Referer**: Giới hạn cho phép/ từ chối truy cập từ các website cụ thể bằng cách chọn **Allow/ Block** và nhập domain tương ứng.
  * **Geo Location:** Giới hạn cho phép, từ chối truy cập theo quốc gia/khu vực bằng cách chọn **Allow/ Block** và nhập mã Geo Location tương ứng. Bạn có thể tham khảo giá trị country code tương ứng tại [https://en.wikipedia.org/wiki/List\_of\_ISO\_3166\_country\_codes](https://en.wikipedia.org/wiki/List\_of\_ISO\_3166\_country\_codes).
* **CORS Configuration**
  * **Simple**: Khi chọn Simple, bạn chỉ cần chỉ định các domain cụ thể được phép truy cập thông qua **Allow Origin.**
  * **Advance**: Khi chọn Advance, ngoài việc chỉ định domain cụ thể, bạn cần cấu hình chi tiết hơn về **Allow Header, Allow Method, Expose Header, Allow Credentials** được phép.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(841).png?raw=true)

* **Caching**
  * **Caching Level**: Xác định mức độ cache của CDN.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(842).png?raw=true)

* **Page Rules:** Tính năng này giúp khách hàng tối ưu các điều kiện và các tùy chọn để giúp website thể hiện được nhiều mục đích khác nhau. Để tạo Page rules, vui lòng chọn **Create Page Rule**, popup sẽ hiện ra, lúc này bạn cần chọn: 
  * **URL pattern:** cần áp dụng pagerule, hỗ trợ kiểu khai báo “\*” đại diện cho một chuỗi nhiều ký tự. Ví dụ: /trang\_landing\_cu.html. Sau khi nhập URL pattern, bạn hãy chọn **Add new rule**. Mỗi Rules khi thỏa điệu kiện đúng URI được request sẽ có thể tùy chọn thực thi một trong các hành động sau:
    * Response Header Override
    * Resolve Origin Override
    * Origin Base Directory
    * Deny Access
  * Chọn **Save changes** để lưu thay đổi.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(843).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(844).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(845).png?raw=true)

4. Chọn **Submit** để hoàn thành việc tạo Live Stream.

### **Bước 3: Cấu hình và truy cập vào Channel Live Stream**

Sau khi bạn tạo xong Live Entrypoint và Live Streaming, lúc này, bạn có thê cấu hình và truy cập vào live thông qua: 

* **Đối với link sử dụng HTTPS:** 

```
https://<vCDN Domain>/ <ChannelName>
```

* **Đối với link sử dụng HTTP:** 

```
http://<vCDN Domain>/ <ChannelName>
```
