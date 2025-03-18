# Chỉnh sửa File Storage

Trên mỗi file storage, bạn có thể thực hiện chỉnh sửa một số thông số, cụ thể:

* **Đối với file storage NFS**: Cho phép chỉnh sửa quyền truy cập (ACL) trực tiếp trên file bằng cách chọn **Edit** trên file storage bạn muốn chỉnh sửa. Tuy nhiên, việc chỉnh sửa ACL có thể gây gián đoạn cho File storage này lên đến **10 giây**. ****Thực hiện hành động này thường xuyên sẽ gây gián đoạn cho File storage của bạn.****

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(1).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(1).png?raw=true)

* **Đối với file storage SMB sử dụng Basic Authentication**: Cho phép thực hiện các thao tác như thêm mới tài khoản, vô hiệu hóa, thay đổi mật khẩu, hoặc xóa các tài khoản authentication đã tạo.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(911).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(912).png?raw=true)

* **Đối với file storage SMB sử dụng AD Authentication**: Không cho phép thay đổi thông tin của Active Directory; nếu cần thay đổi, ****nên tạo một file storage mới để đảm bảo tính ổn định của hệ thống.****
