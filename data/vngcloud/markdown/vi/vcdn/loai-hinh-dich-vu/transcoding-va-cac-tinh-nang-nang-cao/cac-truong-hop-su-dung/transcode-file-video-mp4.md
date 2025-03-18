# Transcode file video (MP4)

**Bài toán đặt ra:** 

* Bạn đang có File MP4 gốc độ phân giải 4K, lưu trữ trên bất kỳ dịch vụ object storage nào tương thích với S3.

**Hiện tại, bạn cần:** 

* File MP4 sau khi transcode sang các độ phân giải khác nhau, lưu trữ trên dịch vụ object storage tương thích với S3 và có thể truy cập qua vCDN của VNG Cloud.

**Giải pháp thực hiện:**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(632).png?raw=true)

Thành phần thực hiện: 

* Dữ liệu nguồn là file .mp4 cần transcode, lưu trữ trên dịch vụ bất kỳ tương thích với S3-compatible.
* Media Service là phần mềm chuyên dụng để xử lý file media để phục vụ nhu cầu VOD, Livestream. Media Service sử dụng vServer để làm compute engine và hiện tại đã có sẵn trên dịch vụ vMarketplace của vServer.
* Dữ liệu đích là file .mp4 sau khi đã transcode, lưu trữ trên disk của vServer. 
* Sau khi đã có Dữ liệu đích, Quý khách có thể sử dụng để làm Origin cho hệ thống CDN.

Để thực hiện bài toán trên, hãy làm theo hướng dẫn bên dưới:

## Khởi tạo bucket trên bất kỳ dịch vụ S3-compatible để làm nơi lưu trữ dữ liệu nguồn

Đâu tiên, bạn cần khởi tạo bucket trên bất kỳ dịch vụ S3-compatible để làm nơi lưu trữ dữ liệu nguồn. Bạn có thể sử dụng AWS S3, Google Storage,... hoặc bạn cũng có thể chọn sử dụng vStorage do VNGCloud phát triển làm nơi lưu trữ dữ liệu nguồn. Chi tiết các bước khởi tạo bucket trên vStorage, vui lòng tham khảo thêm tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-container/khoi-tao-container). Sau khi bucket đã khởi tạo xong, bạn hãy thực hiện: 

* Thiết lập quyền truy cập public từ internet đến các object theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/cac-tinh-nang-cua-vstorage/lam-viec-voi-container/chuyen-che-do-cong-khai-container).
* Upload một file .MP4 để làm sample cho transcoding
* Thực hiện tạo S3 Key cho project theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/quan-ly-truy-cap/quan-ly-tai-khoan-truy-cap-vstorage/tai-khoan-service-account/khoi-tao-vstorage-credentials/khoi-tao-s3-key).

## Cài đặt Sigma Media Server

Đầu tiên, bạn cần cài đặt Sigma Media Server theo các bước tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/transcoding-va-cac-tinh-nang-nang-cao/cai-dat-sigma-media-server).

## Khởi tạo và cấu hình dịch vụ Media Service để livestream. 

**Bước 1:** Sau khi đã cài đặt Sigma Media Server thành công, bạn hãy truy cập vào [https://portal.sigma.video/apps](https://portal.sigma.video/apps) với email mà bạn đã đăng ký sử dụng dịch vụ trước đó.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(654).png?raw=true)

**Bước 2:** Bạn chọn xổ menu **Product** xuống và chọn mục **Media VOD**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(655).png?raw=true)

**Bước 3:** Tiếp tục bạn chọn tab **VOD**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(656).png?raw=true)

**Bước 4:** Chọn nút **Add** ở góc phải để tạo job transcoding

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(657).png?raw=true)

**Bước 5:** Chọn một **server** để thực thi job transcoding, mặc định Sigma Media Server mà bạn đã khởi tạo trước đó trên **vMarketPlace** sẽ được chọn.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(658).png?raw=true)

**Bước 6:** Chọn loại file nguồn cần transcode. Bạn cần nhập vào link [URL](https://han01.vstorage.vngcloud.vn/v1/AUTH\_210ff69ad18d4bfa9920b165ef8ddef4/con\_01/big\_buck\_bunny\_720p\_30mb.mp4) của file nguồn đã được upload lên dịch vụ S3. Ví dụ với vStorage, URL của object sẽ có định dạng tương tự: [https://hcm03.vstorage.vngcloud.vn/v1/AUTH\_123456/cont\_01/pexels\_videos\_1390942%20(2160p).mp4](https://hcm03.vstorage.vngcloud.vn/v1/AUTH\_bcd882dd104f40cb8e20f1cd6bb0b4c6/cont\_01/pexels\_videos\_1390942%20\(2160p\).mp4)**Chú ý: bạn cần thực hiện chuyển chế độ công khai (Make Public) cho container/ bucket trên vStorage hoặc Bất kỳ dịch vụ S3 để Sigma có thể truy cập vào link này.**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(660).png?raw=true)

**Bước 7:** Tại mục **Destination**, chọn kiểu output **Third-party Storage** -> **Generic S3** để lưu file kết quả

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(661).png?raw=true)

**Bước 8**: Cấu hình thông tin S3 của bạn

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(662).png?raw=true)

**Bước 9:** Config các **profile** của đầu vào

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(663).png?raw=true)

**Bước 10:** Config các **profile** đầu ra

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(664).png?raw=true)

**Bước 11:** Trong kịch bản này chúng ta sẽ Chọn **HLS**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(665).png?raw=true)

**Bước 12:** Config các tham số **HLS**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(666).png?raw=true)

**Bước 13:** Bấm **Create Job** để bắt đầu transcode

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(667).png?raw=true)

**Bước 14**: Trở về tab VOD chúng ta sẽ thấy % xử lý, hoặc thông báo lỗi nếu có của các job đã tạo.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(668).png?raw=true)

## Khởi tạo và cấu hình dịch vụ vCDN.

**Bước 1:** Bạn thực hiện truy cập [VNG Cloud – ](https://vcdn.vngcloud.vn/)[vCDN](https://vcdn.vngcloud.vn/)[ Portal](https://vcdn.vngcloud.vn/)

**Bước 2:** Khởi tạo một domain CDN dành cho VOD theo hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/video-on-demand-streaming).

**Bước 3:** Chọn **Origin** của **CDN** là **S3**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(646).png?raw=true)

Sau khi quá trình transcode thành công, Quý khách có thể truy cập đến video kết quả bằng link CDN sau: ****https://\<CDN Domain>/sigma-vod/\<transcode\_job\_id>/master.m3u8****
