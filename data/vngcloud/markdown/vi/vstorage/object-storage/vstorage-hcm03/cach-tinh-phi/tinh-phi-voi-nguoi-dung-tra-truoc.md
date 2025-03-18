# Tính phí với người dùng trả trước

#### Người dùng trả trước khởi tạo project 

Khi bạn khởi tạo một project, nếu bạn là người dùng trả trước thì mặc định **số tiền phải thanh toán** là số tiền bạn cần phải trả để **sử dụng 1 tài nguyên cụ thể**, tính trên các yếu tố:

* Cấu hình tài nguyên (quota lưu trữ).
* Đơn giá theo cấu hình (Có giảm giá hoặc không): tại thời điểm thực hiện hành động trên tài nguyên (đã bao gồm VAT).
* Thời gian sử dụng tài nguyên: Ngày bắt đầu, Ngày kết thúc (tính tới phút).
* Giảm trừ Coupon (nếu có).

Ví dụ công thức tính giá bạn cần thanh toán khi khởi tạo một project như sau:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Gói lưu trữ | Quota mặc định | Đơn giá trên quota mặc định (bao gồm VAT) (2) | Thời gian sử dụng (3) | Giá trị Coupon (4) | Thành tiền = (2) * (3) - (4) |
| Gold | 30GB | 33,000 VND / 1 tháng | 1 tháng | 20,000 VND | 13,000 VND |
| Silver | 30GB | 19,800 VND / 1 tháng | 1 tháng | Không có | 19,800 VND |
| Archive | 30GB | 33,660 VND/ 6 tháng | 6 tháng | 10,000 VND | 23,660 VND |
| Khi bạn thay đổi hạn mức quota thì giá gói lưu trữ sẽ được thay đổi tương ứng. Mỗi gói lưu trữ được chúng tôi quy định riêng về dung lượng sử dụng, số lượng request. Để biết thêm, hãy tham khảo tại  [vStorage là gì?](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/vstorage-la-gi) Tương tự khi bạn thực hiện gia hạn project, tăng/ giảm kích thước gói lưu trữ chúng tôi cũng sẽ tính giá tiền bạn cần thanh toán thêm hoặc giá tiền mà bạn có thể được hoàn trả lại. Chi tiết tham khảo tại  [Quản lý hóa đơn, chi phí & tài nguyên trên VNG Cloud](https://docs.vngcloud.vn/vng-cloud-document/vn/quan-ly-hoa-don-chi-phi-and-tai-nguyen-tren-vng-cloud) . |  |  |  |  |  |

***

#### Người dùng trả trước gia hạn hoặc thiết lập gia hạn tự động project 

Khi bạn thực hiện gia hạn (renew) một project, nếu bạn là người dùng trả trước thì mặc định **số tiền phải thanh toán** là số tiền chênh lệch được tính theo chu kỳ gia hạn mà bạn lựa chọn. Chúng tôi cung cấp các chu kỳ lưu trữ khi gia hạn project bao gồm: 1 tháng, 3 tháng, 6 tháng, 12 tháng, 24 tháng, 36 tháng. Khi bạn thực hiện chọn chu kỳ gia hạn, hệ thống sẽ tự động tính toán thời gian có hiệu lực của chu kỳ lưu trữ mới và tổng số tiền bạn cần chi trả cho việc gia hạn project. Quy tắc tính số tiền thanh toán chênh lệch dựa trên các yếu tố: 

* t\_start: thời điểm khởi tạo dịch vụ (Start time).
* t\_end: thời điểm kết thúc dịch vụ (End time).
* t\_resize: thời điểm thực hiện resize project (Time of resizing).
* p\_original: giá ban đầu (Billing Price).
* p\_new: giá sau khi thay đổi (Resizing Price).01-01-08:00:05

Ví dụ công thức tính giá bạn cần thanh toán khi gia hạn một project như sau:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gói lưu trữ | Đơn giá cũ | Thời điểm bắt đầu gói lưu trữ | Thời điểm kết thúc gói lưu trữ | Thời điểm thực hiện gia hạn | Chu kỳ gia hạn | Thời điểm kết thúc gói lưu trữ mới | Đơn giá mới |
| Silver | 19,800 VND / 1 tháng | 06-03-2023 | 05-04-2023 | 08-03-2023 | 1 tháng | 05-05-2023 | 19,800 VND |
| Silver | 19,800 VND / 1 tháng | 06-03-2023 | 05-04-2023 | 08-03-2023 | 3 tháng | 04-07-2023 | 59,400 VND |
| Silver | 19,800 VND / 1 tháng | 06-03-2023 | 05-04-2023 | 08-03-2023 | 6 tháng | 02-10-2023 | 118,800 VND |
| Silver | 19,800 VND / 1 tháng | 06-03-2023 | 05-04-2023 | 08-03-2023 | 12 tháng | 30-03-2024 | 237,600 VND |
| Silver | 19,800 VND / 1 tháng | 06-03-2023 | 05-04-2023 | 08-03-2023 | 24 tháng | 25-03-2025 | 475,200 VND |

\


***

#### Người dùng trả trước thay đổi tăng hoặc giảm quota lưu trữ của project 

Khi bạn thực hiện tăng giảm kích thước gói lưu trữ (resize) một project, nếu bạn là người dùng trả trước thì mặc định **số tiền phải thanh toán** là số tiền chênh lệch được tính theo kích cỡ gói lưu trữ mà bạn lựa chọn. Bạn có thể tăng giảm quota về mức tối thiểu hoặc tối đa mà chúng tôi cung cấp. Khi bạn thực hiện chọn chu kỳ gia hạn, hệ thống sẽ tự động tính toán tổng số tiền bạn cần chi trả cho việc tăng giảm quota lưu trữ. Quy tắc tính số tiền thanh toán chênh lệch dựa trên các yếu tố: 

* Gói lưu trữ hiện tại
* Quota hiện tại
* Đơn giá trên quota hiện tại (1)
* Quota mới
* Đơn giá trên quota mới (2)

Ví dụ công thức tính giá bạn cần thanh toán khi tăng giảm quota lưu trữ của một project như sau:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gói lưu trữ | Thời điểm bắt đầu gói lưu trữ | Thời điểm kết thúc gói lưu trữ | Quota hiện tại | Quota mới | Đơn giá trên quota hiện tại | Thời điểm resize | Số tiền chưa được sử dụng (1) | Đơn giá trên quota mới (2) | Số ngày sử dụng quota mới (3) | Số tiền cần thanh toán = (2)/30*(3) - (1) |
| Silver | 06-03-2023 | 05-04-2023 | 30 GB | 80 GB | 19,800 VND/ 1 tháng | 31/03/2023 | 3,300 VND | 52,800 VND/ 1 tháng | 5 | 5,500 VND |

***

#### Người dùng xóa project còn hiệu lực 

Khi bạn thực hiện xóa project còn hiệu lực, nếu bạn là người dùng trả trước thì mặc định bạn sẽ nhận được số tiền hoàn trả là số tiền chênh lệch được tính theo số ngày thực tế mà bạn chưa sử dụng gói lưu trữ. Quy tắc tính số tiền thanh toán chênh lệch dựa trên các yếu tố: 

* t\_start: Thời điểm khởi tạo dịch vụ (Start time)\
  t\_end: Thời điểm kết thúc dịch vụ (End time)\
  t\_delete: Thời điểm thực hiện trả cấu hình (Time of deletion)\
  p: Giá tiền (Billing Price)

Ví dụ công thức tính số tiền bạn được hoàn trả khi xóa một project như sau: 

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gói lưu trữ | Thời điểm bắt đầu gói lưu trữ | Thời điểm kết thúc gói lưu trữ (1) | Quota hiện tại | Thời điểm xóa project  (2) | Đơn giá gốc (3) | Số ngày được hoàn tiền (4) = (1) - (2) | Số tiền được hoàn lại = (3) * (4) * 24 *60 / (30 * 24 * 60) |
| Silver | 01-01-2023 | 01-02-2023 | 30 GB | 08-01-2023 | 19,800 VND | 24 ngày | 15,840 VND |
