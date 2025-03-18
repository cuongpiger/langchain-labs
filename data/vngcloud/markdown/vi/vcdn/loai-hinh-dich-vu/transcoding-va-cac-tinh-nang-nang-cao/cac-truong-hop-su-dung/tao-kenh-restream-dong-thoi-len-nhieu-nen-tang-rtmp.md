# Tạo kênh Restream đồng thời lên nhiều nền tảng (RTMP)

Để tạo kênh Restream đồng thời trên nhiều nền tảng, hãy làm theo hướng dẫn sau:

## Cài đặt Sigma Media Server

Đầu tiên, bạn cần cài đặt Sigma Media Server theo các bước tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/transcoding-va-cac-tinh-nang-nang-cao/cai-dat-sigma-media-server).

## Khởi tạo và cấu hình dịch vụ Media Service để livestream. 

**Bước 1:** Sau khi đã cài đặt **Sigma Media Server** thành công, bạn hãy truy cập vào [https://portal.sigma.video/apps](https://portal.sigma.video/apps) với email mà bạn đã đăng ký sử dụng dịch vụ trước đó.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(647).png?raw=true)

**Bước 2:** Bạn chọn xổ menu **Product** xuống và chọn mục **Media Live.** Tiếp tục bạn chọn tab **Channel -> Transcode channels**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 3:** Chọn nút **Add** ở góc phải. Màn hình **Create Transcode Channel** hiển thị, trong tab Config, bạn cần nhập các thông tin cơ bản cho kênh bao gồn **Name** và **Name Modifier**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 4:** Tiếp tục thực hiện configure đầu vào ở tab **Input**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 5:** Tại màn hình **Create Input Transcode**, bạn chọn kiểu đầu vào **RTMP** như sau:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(6)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 6:** Sau khi đóng màn hình **Create** bên trên, hệ thống sẽ hiển thị **danh sách** các đầu vào của kênh. Tại đây, bạn cần **chọn** các đầu vào tương ứng:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(7)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 7:** Tại tab **profile**, bạn nhập các profile của đầu vào bằng cách chọn **Add profile** nếu đã có sẵn hoặc chọn **New profile** để tạo profile mới

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(8)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 8:** Trong ví dụ này, chúng tôi sẽ thêm một profile **video** định dạng 1080p và một **audio** 44\_1khz

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(9)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 9:** Tiếp theo, bạn cấu hình các luồng nhận stream mà bạn mong muốn stream tới

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(10)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Bước 10:** Nhập thông tin **RTMP** sau đó nhấn **Submit**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(11)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

**Tương tự như trên, quý khách có thể stream đồng thời tới nhiều RTMP khác bằng cách thêm cấu hình tại mục Target.**

**Sau khi thực hiện các bước bên trên, tại mục Input sẽ hiển thị thông tin RTMP nhận luồng stream. Quý khách thực hiện stream thông qua đường dẫn tại mục này.**
