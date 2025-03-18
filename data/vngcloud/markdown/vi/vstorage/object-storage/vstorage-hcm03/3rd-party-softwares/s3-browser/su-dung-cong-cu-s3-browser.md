# Sử dụng công cụ S3 Browser

#### Một số use case thông thường 

Trên giao diện ta có thể dễ dàng thấy và thực hiện các thao tác:

1. **Thêm / Xóa bucket**
2. **Upload / Download file**
3. **Tạo / Xóa Folder, File**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(541).png?raw=true)

Một số cấu hình nâng cao thường dùng:

1. **Tools → Options**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(542).png?raw=true)

1. **General**

* **Enable Multipart uploads with part size**: tuỳ vào file size mà cân nhắc size cho mỗi part để đảm bảo không quá 1000 part (số lượng part tối đa mà vstorage hỗ trợ cho mỗi file).

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(543).png?raw=true)

* **Điều tiết bandwidth:**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(544).png?raw=true)

* **Chọn folder lưu file tạm:**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(545).png?raw=true)

* **Cấu hình proxy (nếu có):**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(546).png?raw=true)

> **Chú ý:**
>
> 1. Không nên sử dụng phiên bản S3 Browser quá cũ/ quá mới trên các hệ điều hành có phiên bản quá cũ/ quá mới vì có thể gặp lỗi.
> 2. S3 Browser có hỗ trợ dọn incomplete segments khi tải object lớn (multipart upload). Khi bạn sử dụng S3 Browser để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, hệ thống vStorage đang quá tải, S3 Browser của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. Chúng tôi khuyến cáo bạn thực hiện xóa bỏ những segment rác này để tối ưu hóa chi phí và dung lượng lưu trữ bằng cách:
>    1. Mở ứng dụng **S3 Browser**, chọn **Tools** sau đó chọn **Uncompleted Multipart Uploads**.
>    2. Chọn một hoặc nhiều phần **tệp tin** được tải lên và chọn **Abort** hoặc nhấp chuột phải và chọn **Abort**. 
>
> Chi tiết tham khảo tại: [https://s3browser.com/uncompleted-multipart-uploads.aspx](https://s3browser.com/uncompleted-multipart-uploads.aspx)
