# CDN Purge Cache

## Tổng quan

**CDN Purge Cache** được sử dụng trong các trường hợp cần làm mới hoặc xóa bỏ các nội dung đã được cache trên hệ thống CDN. 

Sau đây là mô tả chi tiết các bước thực hiện Purge Cache trên CDN:

* **Bước 1:** Đầu tiên, bạn đã khởi tạo một **Object Download** trên hệ thống vCDN. Chi tiết các bước vui lòng tham khảo tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vcdn/loai-hinh-dich-vu/object-download). Giả sử, bên dưới tôi đã khởi tạo 1 Object Download _tuongtk3-download_ ( vCDN Domain: _tuleemu0l7obj.vcdn. cloud_) và liên kết với S3 Origin. Trên S3 Origin, tôi đã tạo các file demo1.txt ... demo5.txt, text1.txt ... text5.txt.
* **Bước 2:** Thực hiện test Purge Cache By (ALL, BEGIN, END, CONTAIN, URI(s) ). Trong đó: 
  * **ALL**: Xóa toàn bộ cache.
  * **BEGIN**: Xóa cache cho các URL bắt đầu bằng một chuỗi nhất định.
  * **END**: Xóa cache cho các URL kết thúc bằng một chuỗi nhất định.
  * **CONTAIN**: Xóa cache cho các URL chứa một chuỗi cụ thể.
  * **URI(s)**: Xóa cache cho một hoặc nhiều URI cụ thể.
* **Bước 3:** Gọi đến các link để CDN lưu cache 
  * Với vCDN Domain: _tuleemu0l7obj.vcdn. cloud_, bạn có thể thực hiện gọi đến các link để CDN lưu cache như sau: 
    * [https://tuleemu0l7obj.vcdn.cloud/purge\_lab/text1.txt](https://tuleemu0l7obj.vcdn.cloud/purge_lab/text1.txt)
    * [https://tuleemu0l7obj.vcdn.cloud/purge\_lab/demo1.txt\
      ](https://tuleemu0l7obj.vcdn.cloud/purge_lab/demo1.txt)
    * ....

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/1.png?raw=true)

* Khi CDN đã lưu cache ta sẽ thấy header  `X-Cache: HIT`  và `X-Cache-Version: $Thời_gian_timestamp_lưu_cache` ở CDN

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/2.png?raw=true)

* Đối với những file chưa được lưu cache ở CDN header sẽ có dạng  `X-Cache: MISS` và `X-Cache-Version: $Thời_gian_ timestamp_lưu_cache` ở CDN

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/3.png?raw=true)

 Chi tiết mỗi loại bạn vui lòng tham khảo hướng dẫn bên dưới:

## Chi tiết

### 1.    Purge Cache By ALL.

Purge by ALL: sẽ xóa hết tất cả link (tất cả Cache của resources trên CDN).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Trước khi Purge Cache các file đã được Cache ở CDN

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Thay đổi nội dung của các file, sau đó refresh trình duyệt. Do các file đã được Cache ở CDN nên khi thay đổi ở Origin các file ở CDN chưa được thay đổi theo.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Tiến hành Purge Cache: Chọn **Service** và **CDN** tương ứng và **Purge by ALL**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Sau khi Purge cache CDN đã gọi về Origin để lấy nội dung mới nhất.

 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

### 2.    Purge Cache By BEGIN

Purge by BEGIN: Sẽ xóa hết các resource đang được Cache ở CDN bắt đầu bằng ký tự nhập vào.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(5)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Tương tự như Purge by ALL, trước khi Purge Cache các file đã được Cache ở CDN. Tiến hành Purge Cache: Chọn **Service** và **CDN** tương ứng và **Purge by BEGIN**. Tại URI nhập: `/purge_lab/text*` (xóa cache tất cả các file text\* ở vCDN).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(6)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Sau khi Purge kiểm tra file `/purge_lab/text*` đã được gọi về Origin để lấy nội dung mới nhất.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(7)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Do các file `/purge_lab/demo*` không được Purge nên nội dung vẫn được lấy từ Cache ở CDN.

 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(8)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

 

### 3.    Purge Cache By CONTAIN

Purge by CONTAIN: Sẽ xóa hết các resource đang được Cache ở CDN có chuỗi ký tự nhập vào.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(9)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Tương tự như Purge by ALL, trước khi Purge Cache các file đã được Cache ở CDN. Tiến hành Purge Cache: Chọn **Service** và **CDN** tương ứng và **Purge by CONTAIN**. Tại URI nhập: `/*demo*`  (xóa cache tất cả các file \*demo\* đang được cache ở vCDN).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(10)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Sau khi Purge Cache các file `/purge_lab/demo1.txt` ... Đã được gọi về Origin để lấy nội dung mới.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(11)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Các file `/purge_lab/text1.txt` ... Vẫn lấy nội dung từ Cache ở CDN

 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(12)%20(1)%20(1)%20(1)%20(1).png?raw=true)

### 4.    Purge Cache By END.

Purge by END: Sẽ xóa hết các resource đang được Cache ở vCDN kết thúc chuỗi ký tự nhập vào.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(13)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Tương tự như Purge by ALL, trước khi Purge Cache các file đã được Cache ở CDN. Tiến hành Purge Cache: Chọn **Service** và **CDN** tương ứng và **Purge by END**. Tại URI nhập: `/*1.txt`  (xóa cache tất cả các file  \*1.txt đang được cache ở CDN).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(14)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Sau khi Purge Cache các file `/*1.txt` ... Đã được gọi về Origin để lấy nội dung mới.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(15)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Các file `/purge_lab/text1.txt` ... Vẫn lấy nội dung từ Cache ở CDN.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(16)%20(1)%20(1)%20(1)%20(1).png?raw=true)

### 5.    Purge Cache By URI(s).

Purge by URI(s): Sẽ xóa đúng với link được chỉ định.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(17)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Tương tự như Purge by ALL, trước khi Purge Cache các file đã được Cache ở CDN. Tiến hành Purge Cache: Chọn **Service** và **CDN** tương ứng và **Purge by URI(s)**. Tại URI nhập: `/purge_lab/demo1.txt` , `/purge_lab/demo2.txt` ... (xóa cache các link chỉ định đang được cache ở vCDN).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(18)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Sau khi Purge Cache các file `/purge_lab/demo1.txt` ... Đã được gọi về Origin để lấy nội dung mới.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(19)%20(1)%20(1)%20(1).png?raw=true)

* Các file khác không được chỉ định Purge Cache ... Vẫn lấy nội dung từ Cache ở CDN.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(20)%20(1)%20(1)%20(1).png?raw=true)
