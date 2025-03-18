---
hidden: true
---

# Cách tính phí

Tại VNG Cloud, với sản phẩm vCloudStack mang đến cho khách hàng hai (02) gói mô hình sử dụng dịch vụ, tùy vào nhu cầu sử dụng và định hướng phát triển hệ thống mà khách hàng có thể cân nhắc quyết định nên sử dụng gói mô hình dịch vụ nào:

* Mô hình High Scale
* Mô hình HCI

***

### 1/ Mô hình High Scale 

Mô hình cung cấp cố định phần mềm hỗ trợ quản lý vận hành theo cơ sở hạ tầng (vật lý) gồm:

| STT | Danh mục | Đơn vị | Số lượng |
| --- | --- | --- | --- |
| 1 | Cụm máy chủ (Compute cluster) gồm 6 nodes: + Bộ xử lý: 02 x 16 lõi cores + Ram: 512 GB + Ổ đĩa (Disk): 02 x 480 GB SSD/VNME + NIC: 04 x10G SFP + Bộ thu phát | Cụm (Cluster) | 1 |
| 2 | Cụm lưu trữ (Storage cluster) gồm 4 nodes: + Bộ xử lý: 02 x 16 lõi cores + RAM: 128 GB + Ổ đĩa (Disk): 09 x 1.92 TB SSD/NVEME + NIC: 04 x10G SFP + Bộ thu phát | Cụm (Cluster) | 1 |
| 3 | Cụm Backup (Backup Cluster) gồm 1 node: + Bộ xử lý: 02 x 8 lõi cores + RAM: 128 GB + Ổ đĩa (Disk): 10 x 7.6 TB SSD hoặc 10 x 8TB HDD + NIC: 04 x10G SFP + Bộ thu phát | Cụm (Cluster) | 1 |
| 4 | Thiết bị Firewall | Thiết bị | 2 |
| 5 | Thiết bị định tuyến : 48 x 10 G SFP + bộ thu phát | Thiết bị | 2 |
| 6 | Đường truyền kết nối: + Tuyến chính (Main line): DarkFiber/MPLS + Tuyến phụ (Seconda line): MPLS/VPN | Đường truyền (line) | 2 |
| 7 | Dịch vụ triển khai | Gói | 1 |

### 2/ Mô hình HCI 

Mô hình cung cấp cố định phần mềm hỗ trợ quản lý vận hành theo cơ sở hạ tầng (vật lý) gồm:

| STT | Danh mục | Đơn vị | Số lượng |
| --- | --- | --- | --- |
| 1 | Cụm máy chủ và lưu trữ (Compute và Storage Cluster) gồm 6 nodes: + Bộ xử lý: 02 x 16 lõi cores + Ram: 768 GB + Ổ đĩa OS (Disk): 02 x 480 GB SSD/VNME + Ổ đĩa data (Disk): 08 x 1.92 TB SSD/NVME + NIC: 04 x10G SFP + Bộ thu phát | Cụm (Cluster) | 1 |
| 2 | Cụm Backup (Backup Cluster) gồm 1 node: + Bộ xử lý: 02 x 8 lõi cores + RAM: 128 GB + Ổ đĩa (Disk): 10 x 7.6 TB SSD hoặc 10 x 8TB HDD + NIC: 04 x10G SFP + Bộ thu phát | Cụm (Cluster) | 1 |
| 3 | Thiết bị Firewall | Thiết bị | 2 |
| 4 | Thiết bị định tuyến : 48 x 10 G SFP + bộ thu phát | Thiết bị | 2 |
| 5 | Đường truyền kết nối: + Tuyến chính (Main line): DarkFiber/MPLS + Tuyến phụ (Seconda line): MPLS/VPN | Đường truyền (line) | 2 |
| 6 | Dịch vụ triển khai | Gói | 1 |
