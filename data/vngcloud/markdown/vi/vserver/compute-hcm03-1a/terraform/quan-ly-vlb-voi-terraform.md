# Quản lý vLB với Terraform

#### Để quản lý vLB với Terraform, bạn cần làm các bước sau đây: 

**Bước 1:** Cài đặt Terraform CLI như hướng dẫn tại [đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/terraform/cai-dat-terraform)

**Bước 2:** Để có thể thực hiện quản lý vLB với Terraform bạn cần tạo **Service account** từ Root account trên trang chủ **IAM** (xem hướng dẫn cách tạo Service account và sử dụng IAM [tại đây](https://docs.vngcloud.vn/vng-cloud-document/vn/vdb/relational-database-service-rds/quan-ly-thong-tin-rds-instance)), trong trường hợp này lấy ví dụ cho việc bạn muốn tạo Load Balancer với Terraform cần có các quyền (Policy) sau:

* CreateLoadBalancer
* GetLoadBalancer

hoặc bạn có thể cấp quyền **vLBFullAccess** (nên có quyền **vLBReadOnlyAccess** để get thông tin resource sau khi tạo xong). Tham khảo thêm về cách phân quyền cho từng **Resource, Action** tương ứng [{Trang phân quyền IAM}](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/quan-ly-dinh-danh-va-truy-cap-iam-cho-vserver/cac-hanh-dong-tai-nguyen-va-dieu-kien-can-cho-phan-quyen-truy-cap-vserver).

> **Ghi chú:** Mỗi hành động quản lý tài nguyên khác nhau sẽ yêu cầu các quyền khác nhau, vì thế điều cần thiết là phải thiết lập một bộ phân quyền hợp lý phù hợp với nhu cầu kinh doanh của bạn.

**Bước 3:** Tạo thư mục chứa terraform file và tải example từ VNG Cloud repo tại [đây](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples)

Sau khi tải thư mục Example về máy, người dùng mở file [_**variable.tf**_](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/variable.tf) _(theo đường dẫn **terraform-providder-vngcloud/ examples/** ),_ sau đó thay đổi các thông tin cần thiết như sau:

* **Client\_id:** Lấy tại trang chủ IAM/ Service accoun&#x74;**/ Tab Security credentials**
* **Client\_secret:** Lấy khi khởi tạo Service account tại trang chủ **IAM** hoặc có thể reset lại tại trang IAM/ Service accoun&#x74;**/ Tab Security credentials**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(303).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(304).png?raw=true)

```
variable "client_id" {  
type = string  
default = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
variable "client_secret" {  
type = string  
default = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

**Bước 4:** Kiểm tra lại thông tin file [**main.tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/main.tf) _**(**&#x74;heo đường dẫn **terraform-providder-vngcloud/ examples/ )**_**,** trường hợp này bạn cần xóa đi các dòng bên dưới:

* _module "vserver" {source = "./modules/vng-cloud-vserver"}_
* module "k8s" {source = "./modules/vng-cloud-k8s" }

_chỉ để lại:_

* _module "vlb" { source = "./modules/vng-cloud-vlb" }_

```
terraform {  
required_providers {    
vngcloud = {      
source  = "vngcloud/vngcloud"      
version = "1.1.0"    
}
} 
provider "vngcloud" {  
token_url        = "https://iamapis.vngcloud.vn/accounts-api/v2/auth/token"  
client_id        = var.client_id  
client_secret    = var.client_secret  
vserver_base_url = "https://hcm-3.api.vngcloud.vn/vserver/vserver-gateway"  
vlb_base_url = "https://hcm-3.api.vngcloud.vn/vserver/vlb-gateway"}
module "vlb" {  
source = "./modules/vng-cloud-vlb" }
}
```

\
**Bước 5:** Sau đó truy cập vào thư mục vng-cl _**terraform-providder-vngcloud/ examples/ modules/ vng-cloud-vlb)**_, và mở file [**variable/tf**](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples/modules/vng-cloud-vlb)**:** 

* **project\_id**: thông tin project của bạn, bạn có thể lấy ở [{Tab Limit}](https://hcm-3.console.vngcloud.vn/vserver/limit) trên vServer Portal, Ví dụ: **pro-462803f3-6858-466f-bf05-df2b33faa360:**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(305).png?raw=true)

* **subnet\_id**: chỉ định subnet id mà vServer sẽ được tạo trên đó, bạn có thể lấy từ [{Tab VPC}](https://hcm-3.console.vngcloud.vn/vserver/network/vpc), nếu chưa khởi tạo bất cứ subnet nào bạn có thể xem hướng dẫn tại [{Trang tạo subnet}](https://docs.vngcloud.vn/vng-cloud-document/vn/vserver/compute-hcm03-1a/network/virtual-private-cloud-vpc):

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(306).png?raw=true)

```
variable "project_id" {  
type    = string  
default = "pro-462803f3-6858-466f-bf05-df2b33faa360"
}
variable "subnet_id" {  
type    = string  
default = "sub-5f101cba-7ce0-4084-8576-06b8dbfb298a"}
```



**Bước 6:** Kiểm tra lại thông tin file [**main.tf**](https://github.com/vngcloud/terraform-provider-vngcloud/blob/main/examples/modules/vng-cloud-vlb/main.tf) _(theo đường dẫn **terraform-providder-vngcloud/ examples/ modules/ vng-cloud-vlb**)_, trong file chúng tôi để sẵn một số câu lệnh: **Create LB**, **Listener, Policy, Pool,** trường hợp này để Tạo mới LB bạn chỉ cần để lại resource **Create** **LB** theo hướng dẫn bên dưới:

```
data "vngcloud_vlb_lb_packages" "lb_packages" {  
project_id = var.project_id
} 
resource "vngcloud_vlb_load_balancer" "example"{  
project_id = var.project_id  
name       = "example_vlb"  
package_id =  data.vngcloud_vlb_lb_packages.lb_packages.packages[0].uuid  
scheme     = "Internet"  
subnet_id  = var.subnet_id  
type       = "Layer 7"
}
```

**Bước 7:** Khởi chạy terraform command

* Sau khi hoàn tất các thông tin trên, để terraform khởi tạo và tải VNG Cloud provider về đồng thời thiết lập các thông tin cần thiết chạy lệnh bên dưới, lưu ý khi chạy cần đứng tại thư mục terraform-provider-vngcloud/ [**examples**](https://github.com/vngcloud/terraform-provider-vngcloud/tree/main/examples)/: 

| `terraform init` |
| ---------------- |

Hệ thống sẽ trả ra kết quả:



```
vnglab:vngcloud cbr09$ terraform init 

Initializing the backend... 

Initializing provider plugins...
- Finding vngcloud/vngcloud versions matching "0.0.5"...
- Installing vngcloud/vngcloud v0.0.5...
- Installed vngcloud/vngcloud v0.0.5 (self-signed, key ID A6A27B3126EF15EB) 

Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html 

Terraform has created a lock file .terraform.lock.hcl to record the providerselections it made above. Include this file in your version control repositoryso that Terraform can guarantee to make the same selections by default whenyou run "terraform init" in the future. 

Terraform has been successfully initialized! 

You may now begin working with Terraform. Try running "terraform plan" to seeany changes that are required for your infrastructure. All Terraform commandsshould now work. 

If you ever set or change modules or backend configuration for Terraform,rerun this command to reinitialize your working directory. If you forget, othercommands will detect it and remind you to do so if necessary.
```

Sau đó, bạn để xem những thay đổi sẽ được áp dụng trên những resource mà terraform đang quản lý bạn có thể chạy:

| `terraform plan` |
| ---------------- |

Cuối cùng bạn chọn chạy dòng lệnh 

| `terraform apply` |
| ----------------- |

và chọn **YES** để thực hiện việc khởi tạo vServer thông qua Terraform

**Bước 8**: Bạn có thể lên Portal để xem LB đang được khởi tạo từ Terraform
