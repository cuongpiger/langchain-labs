# Third-party integration process

## Tổng quan

vMarketplace là nơi tổng hợp nhiều ứng dụng phổ biến phù hợp cho các nghành khác nhau như giải trí, ngân hàng, bất động sản, bán lẻ, sản xuất,... Các ứng dụng được vMarketplace hỗ trợ build sẵn thành các image, giúp người dùng bỏ qua các bước tìm kiếm và cài đặt rườm ra để có thể triển khai máy chủ ảo một cách dễ dàng và nhanh chóng. Từ việc tích hợp với vMarketplace, mang lại lợi ích đáng kể cho quý doanh nghiệp, nhà cung cấp ứng dụng có thể kể đến như sau:

* **Tăng khả năng tiếp cận khách hàng:** vMarketplace là nơi tập trung của một lượng lớn người dùng, do đó việc tải lên image của bạn tại đó giúp bạn tiếp cận được một lượng lớn khách hàng tiềm năng.
* **Tăng doanh số bán hàng:** Việc có sản phẩm trên Marketplace giúp tăng sự thu hút và chuyển đổi của sản phẩm, từ đó tăng doanh số bán hàng của bạn.
* **Xây dựng uy tín và niềm tin:** Một ứng dụng chất lượng, được đăng tải trên một nền tảng uy tín giúp xây dựng niềm tin và uy tín của thương hiệu của bạn trong mắt khách hàng.
* **Tiếp cận với thị trường mới:** vMarketplace cung cấp một cơ hội tuyệt vời để tiếp cận với các thị trường mới mà bạn có thể chưa từng đến được, từ đó mở rộng phạm vi hoạt động kinh doanh của bạn.
* **Hỗ trợ tiếp thị sản phẩm:** vMarketplace thường có các công cụ tiếp thị tích hợp sẵn, giúp bạn dễ dàng quảng bá sản phẩm của mình và thu hút người mua.

## Quy trình tích hợp 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/71729271.png?raw=true)

* Bước 1: Đối tác cài đặt môi trường, kiểm thử tính khả dụng của ứng dụng trên môi trường VNG Cloud và một số tài liệu cần thiết
* Bước 2: VNG Cloud đóng gói image theo yêu cầu, tài liệu mà đối tác cung cấp
* Bước 3: VNG Cloud kiểm thử tính đúng đắn và khả dụng của ứng dụng trên môi trường kiểm thử
* Bước 4: Đối tác đồng kiểm thử ứng dụng trên môi trường kiểm thử
* Bước 5: Người dùng cuối cài đặt và sử dụng ứng dụng trên vMarketplace

**Yêu cầu chi tiết & SLA**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Giai đoạn** | **Bên chịu trách nhiệm** | **Công việc** | **Cam kết SLA** |
| 1 | Chuẩn bị | Đối tác & VNG Cloud Support | - VNG Cloud cung cấp môi trường để quý đối tác triển khai thử ứng dụng trên môi trường VNG Cloud <br> - Đối tác riển khai thử ứng dụng trên môi trường VNG Cloud <br> - Đối tác đánh giá tính khả dụng của ứng dụng trên môi trường VNGCloud <br> - Đối tác cung cấp tài liệu cho các yêu cầu: Hướng dẫn đóng gói image Hướng dẫn sử dụng ứng dụng: Mô tả ứng dụng, Tính giá (Theo VM/License), Hướng dẫn truy cập và kết nối, Support Contact,… Các Standards & Limitation: Cấu hình (Ram, CPU, Storage), Manage Security Group Rules,… <br> - Hướng dẫn đóng gói image <br> - Hướng dẫn sử dụng ứng dụng: Mô tả ứng dụng, Tính giá (Theo VM/License), Hướng dẫn truy cập và kết nối, Support Contact,… <br> - Các Standards & Limitation: Cấu hình (Ram, CPU, Storage), Manage Security Group Rules,… | No SLA Commitment |
| 2 | Đóng gói image | VNG Cloud Support | - Nghiên cứu tài liệu và triển khai thử ứng dụng <br> - Đóng gói ứng dụng theo yêu cầu <br> - Tải lên image dùng thử trên Marketplace Portal (môi trường staging) | 5 - 7 ngày làm việc |
| 3 | Kiểm thử trên vMarketplace | VNG Cloud Support | - QC Testing: UI, Tính bảo mật, Khả năng truy cập, Tính khả dụng,… <br> - Kiểm thử trên môi trường Production | 1 - 2 ngày làm việc |
| 4 | Đồng kiểm thử | Đối tác & VNG Cloud Support | - Đối tác đồng kiểm thử tính đúng đắn của ứng dụng trên môi trường Production <br> - Quay về bước 2 nếu có yêu cầu thay đổi | 1 - 2 ngày làm việc |
| 5 | Phát hành | VNG Cloud Support | - Thông báo phát hành ứng dụng mới trên vMarketplace đến người dùng VNG Cloud | 1 - 2 ngày làm việc |
| 6 | Sử dụng thực tế | Người dùng cuối & VNG Cloud Support | - Người dùng cuối triển khai và sử dụng ứng dụng trên môi trường VNG Cloud <br> - VNG Cloud Support team hỗ trợ người dùng cuối sử dụng, cài đặt và kết nối đến ứng dụng dựa trên tài liệu đối tác cung cấp <br> - Ghi nhận phản hồi và đánh giá nâng cấp ứng dụng | Dựa trên SLA Server nếu có bất kỳ vấn đề gì liên quan đến máy chủ ảo triển khai ứng dụng |
