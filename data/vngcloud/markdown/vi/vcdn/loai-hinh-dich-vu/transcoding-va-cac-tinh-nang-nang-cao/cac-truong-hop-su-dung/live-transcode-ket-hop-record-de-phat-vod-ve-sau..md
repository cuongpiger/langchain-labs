# Live Transcode kết hợp record để phát VOD về sau.

Để tạo kênh Live Transcode kết hợp record để phát VOD về sau, hãy làm theo hướng dẫn sau:

## Cài đặt Sigma Media Server

Đầu tiên, bạn cần cài đặt Sigma Media Server theo các bước tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/transcoding-va-cac-tinh-nang-nang-cao/cai-dat-sigma-media-server).

## Khởi tạo và cấu hình dịch vụ Media Service để livestream. 

**Bước 1:** Sau khi đã cài đặt **Sigma Media Server** thành công, bạn hãy truy cập vào [https://portal.sigma.video/apps](https://portal.sigma.video/apps) với email mà bạn đã đăng ký sử dụng dịch vụ trước đó.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(647).png?raw=true)

**Bước 2:** Bạn chọn xổ menu **Product** xuống và chọn mục **Livestream**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(648).png?raw=true)

**Bước 3:** Tiếp tục bạn chọn tab **Channel**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(649).png?raw=true)

**Bước 4:** Chọn nút **Add channel** ở góc phải

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(650).png?raw=true)

**Bước 5:** Màn hình **Create Channel** hiển thị, bạn configure các tham số của kênh, chọn server xử lý trong mục **Advance configuration**.

**Chú ý: để record Livestream thành VOD phát về sau, bạn cần bật phương án Catchup như hình bên dưới và nhập thông tin nơi lưu trữ VOD.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(12)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 6:** Quay trở lại màn hình list **Channel** chúng ta sẽ thấy kênh vừa được tạo nằm trong danh sách. Click vào tên kênh để vào màn hình detail của kênh.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(652).png?raw=true)

**Bước 7:** Trong màn hình detail của kênh ta sẽ thấy thông tin RTMP Stream URL, Quý khách thay thế **Stream URL** trên màn hình bằng _****rtmp://\<server\_public\_ip>:1935/livestream****_ để stream.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(653).png?raw=true)

## Khởi tạo và cấu hình dịch vụ vCDN.

**Bước 1:** Bạn thực hiện truy cập [VNG Cloud – ](https://vcdn.vngcloud.vn/)[vCDN](https://vcdn.vngcloud.vn/)[ Portal](https://vcdn.vngcloud.vn/)

**Bước 2:** Khởi tạo một domain CDN dành cho **Live Streaming** theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/live-streaming).

**Bước 3**: Thực hiện trỏ **Origin** của CDN về **server Sigma** đang xử lý livestream
