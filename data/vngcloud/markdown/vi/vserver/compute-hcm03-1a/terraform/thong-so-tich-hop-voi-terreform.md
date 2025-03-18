# Thông số tích hợp với Terraform

\
Nội dung

* [Những thông số truyền từ Terraform](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/terraform/thong-so-tich-hop-voi-terreform#thongsotichhopvoiterreform-nhungthongsotruyentuterreform)
* [Những thuộc tính truyền cho Terraform](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/terraform/thong-so-tich-hop-voi-terreform#thongsotichhopvoiterreform-nhungthuoctinhtruyenchoterreform)

## Những thông số truyền từ Terraform 

### Mẫu truyền ví dụ 

```
resource "vngcloud_vserver_server" "server"{
 project_id = "pro-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 name = "example-server"
 encryption_volume = false
 flavor_id = "flav-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 image_id = "img-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 network_id = "net-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 root_disk_size = 20
 root_disk_type_id = "vtype-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 ssh_key = "ssh-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 security_group = ["secg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]
 subnet_id = "sub-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

### Các tham số (Arguments) 

| No. | Thông số | Bắt buộc | Loại dữ liệu | Mô tả | Dữ liệu mẫu |
| --- | --- | --- | --- | --- | --- |
| 1 | project_id | **BẮT BUỘC** | **STRING** | Mã của Project. | pro-462803f3-6858-466f-bf05-df2b33faa360 |
| 2 | name | **BẮT BUỘC** | **STRING** | Tên của Server. | example-server-name |
| 3 | encryption_volume | **BẮT BUỘC** | **BOOLEAN** | Server có dùng các Volume mã hóa hay không? | False |
| 4 | flavor_id | **BẮT BUỘC** | **STRING** | Mã của Flavor. | flav-e2028a81-cc75-47e4-8af1-9eef2f857f84 |
| 5 | image_id | **BẮT BUỘC** | **STRING** | Mã của Image. | img-b5bf635e-0456-4765-b493-31d5fcfc05aa |
| 6 | network_id | **BẮT BUỘC** | **STRING** | Mã của Network. | net-961d6867-b65a-40ac-879e-d84e4dc768e0 |
| 7 | root_disk_size | **BẮT BUỘC** | **NUMBER** | Kích thước của boot volume. | 20 |
| 8 | root_disk_type_id | **BẮT BUỘC** | **STRING** | Mã của loại boot volume. | vtype-61c3fc5b-f4e9-45b4-8957-8aa7b6029018 |
| 9 | ssh_key | **TÙY CHỌN** | **STRING** | Mã của SSH key. | ssh-7bd70c56-1f05-4989-a0f0-cc3496b62001 |
| 10 | security_group | **TÙY CHỌN** | **STRING** | Mã của Security group. | secg-3b12a078-b862-43b5-a56b-d7fc4429e535 |
| 11 | subnet_id | **BẮT BUỘC** | **STRING** | Mã của subnet. | sub-c1ebba8f-baa8-434c-beb7-2916199bb812 |
| 12 | host_group_id | **TÙY CHỌN** | **STRING** | Mã của Host Group. | / |
| 13 | action | **TÙY CHỌN** | **STRING** | Những hành động với Server. Các hành động đó có thể là: stop; start; reboot. | start |
| 14 | attach_floating | **TÙY CHỌN** | **BOOLEAN** | Server có được gắn floating IP không? | True |
| 15 | expire_password | **TÙY CHỌN** | **BOOLEAN** | Bỏ qua thay đổi password thì false, nếu không thì true. | False |
| 16 | os_licence | **TÙY CHỌN** | **BOOLEAN** | Bản quyền của Hệ điều hành OS. | True |
| 17 | root_disk_encryption_type | **TÙY CHỌN** | **STRING** | Kiểu mã hóa của boot volume. | / |
| 18 | source_type | **TÙY CHỌN** | **STRING** | Loại Source. | / |
| 19 | user_name | **TÙY CHỌN** | **STRING** | Tên của User. | usernamestackops |
| 20 | user_password | **TÙY CHỌN** | **STRING** | Mật khẩu của USer. | VngGCloud3030 |
| 21 | server_group | **TÙY CHỌN** | **STRING** | Mã của Server Group. | / |
| 22 | user_data | **TÙY CHỌN** | **STRING** | User_data được cung cấp khi kích hoạt sử dụng server. | ${data.template_cloudinit_config.user_data.rendered} |
| 23 | user_data_base64_encode | **TÙY CHỌN** | **BOOLEAN** | Có được sử dụng trực tiếp mã hóa dữ liệu nhị phân base64 thay vì user_data thường không? Việc sử dụng này thay cho User_data bất cứ khi nào giá trị không phải là chuỗi UTF-8 hợp lệ. | True |
| 24 | is_poc | **TÙY CHỌN** | **BOOLEAN** | Sử dụng ví POC. | True |

> **Ghi chú**
>
> * Với thông tin truyền thay đổi (Resize) thì vẫn truyền thuộc tính **is\_poc** về hệ thống của VNG Cloud.
> * Nếu không truyền **is\_poc** thì user sẽ sử dụng ví thường;
> * Trường hợp ngừng sử dụng ví POC và sau đó server bị hết hạn sử dụng, tuy nhiên Server chưa tắt liền mà hệ thống VNG sẽ định kỳ có job quét (11h hàng ngày) để xét tắt các Server bị hết hạn, do đó trước 11h user có thể nạp credit để thanh toán sử dụng tiếp Server.

> **Lưu ý**
>
> Khi Server đã hết hạn và trạng thái là Kết thúc (Terminated). Nếu User muốn gia hạn (renew) tài nguyên (resource) thì **User phải vào User Portal để gia hạn nếu sử dụng Terraform**, vì Terraform không có chức năng gia hạn.

## **Những thuộc tính truyền cho Terraform** 

***

Sau khi VNG Cloud ghi nhận các thông số truyền từ Terraform, sẽ có những thuộc tính sau được xuất ra cho Terreform cho user sử dụng:

* **id** STRING : Mã định danh của Server này;
* **external\_interfaces:** Danh sách các thông tin của Network External:
  * **external\_interfaces** STRING;
  * **floating\_ip** STRING;
  * **interface\_type**STRING;
  * **mac** STRING;
  * **network\_uuid** STRING;
  * **port\_uuid** STRING;
  * **status** STRING;
  * **subnet\_uuid** STRING;
  * **type** STRING;
* **internal\_interfaces:** Danh sách các thông tin của Network External:
  * **external\_interfaces** STRING;
  * **floating\_ip** STRING;
  * **interface\_type** STRING;
  * **mac** STRING;
  * **network\_uuid** STRING;
  * **port\_uuid** STRING;
  * **status** STRING;
  * **subnet\_uuid** STRING;
  * **type** STRING.
