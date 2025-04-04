# Sử dụng ứng dụng OBS Studio để push luồng Live Stream

Bên dưới là hướng dẫn sử dụng ứng dụng OBS Studio để push luồng Live Stream.

**Bước 1**: Đầu tiên, bạn cần thực hiện khởi tạo một **Live Entrypoint** và một **Live Stream** trên hệ thống vCDN theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/live-streaming). Bạn có thể bỏ qua bước này nếu bạn đã có sẵn một **Live Entrypoint** và một **Live Stream.**

> **Lưu ý:**
>
> * Khi khởi tạo Live Entrypoint, tại mục Publish IPs, bạn cần bỏ địa chỉ IP 0.0.0.0 và nhập User Name, Password mong muốn sử dụng.



**Bước 2**: Mở ứng dụng OBS trên thiết bị của bạn và chọn **Settings**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(223).png?raw=true)

**Bước 3:** Tại trang Settings, bạn tiếp tục chọn **Stream** ở Tab bên trái. Trong đó:

* **Service**: Custom...
* **Server**: `rtmp://vnpt.entrypoint.vcdn.live/xxxxxxxxxxxxxxxx/` (Live EP domain được cung cấp khi bạn tạo và LiveApp của các bạn có thể tìm thấy tại mục cấu hình Live Entrypoint)
* **Stream Key**: `demo1?u=xxxxxx&p=xxxxxxx` (Channel (demo1) bạn có thể nhập tùy ý| Username và password bạn nhập lúc khởi tạo Live Entrypoint)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(224).png?raw=true)

**Bước 4:** Sau khi tạo 1 domain Live CDN được mapping với Live App đã push stream thì link view được tạo ra sẽ có dạng `https://domaincdn.vcdn.cloud/demo1/index.m3u8.`
