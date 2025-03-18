# K8S Flavor

Trong một Kubernetes cluster, cấu hình "flavor" thường được gọi là "node instance type" hoặc "node profile". Đây là một cấu hình tài nguyên phần cứng dành cho Kubernetes Cluster với các tùy chọn cụ thể hóa về tài nguyên như CPU, RAM, GPU mà bạn có thể chọn để cấu hình cho Master Node và Minion Node trong cluster của bạn. Cấu hình này quyết định hiệu năng và khả năng chịu tải của các node trong cluster.

**Master Node Flavor:** Master Node là trung tâm quản lý của cluster Kubernetes và không chạy các ứng dụng sản phẩm. Do đó, cần ít tài nguyên hơn so với Worker Node.

* **CPU và RAM:** Master Node cần ít tài nguyên CPU và RAM hơn vì nó chủ yếu thực hiện quản lý và điều phối công việc của các Worker Node.
* **GPU:** K8S chủ yếu tập trung vào việc quản lý và phân phối các ứng dụng và dịch vụ nên ít khi sử dụng GPU tuy nhiên có một vài trường hợp đòi hỏi GPU để thực hiện các tác vụ đồ họa, học máy, xử lý dữ liệu lớn và nhiều tác vụ khác

**Minion Node Flavor:** Minion Node chạy các container của ứng dụng và phải có đủ tài nguyên để hỗ trợ chúng.

* **CPU và RAM:** Cấu hình này tùy thuộc vào số lượng và loại container bạn muốn chạy trên mỗi Minion Node. Cung cấp đủ tài nguyên CPU và RAM để đảm bảo hiệu suất của ứng dụng.
* **GPU:** K8S chủ yếu tập trung vào việc quản lý và phân phối các ứng dụng và dịch vụ nên ít khi sử dụng GPU tuy nhiên có một vài trường hợp đòi hỏi GPU để thực hiện các tác vụ đồ họa, học máy, xử lý dữ liệu lớn và nhiều tác vụ khác

Cần lưu ý rằng cấu hình flavor phải được điều chỉnh để phù hợp với yêu cầu cụ thể của ứng dụng và khả năng của tài nguyên hệ thống. Một cấu hình không thích hợp có thể dẫn đến hiệu năng kém hoặc thất bại của ứng dụng trong cluster Kubernetes của bạn.

VNG Cloud K8S cung cấp các Flavor phù hợp với đa dạng nhu cầu để người dùng có thể lựa chọn theo bảng bên dưới:

***

### **Master Node Flavor** 

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Flavor ID** | Tên Flavor | **CPU** | **Bộ nhớ RAM (GB)** | GPU | CPU Flatform |
| flav-07b02234-7981-4f79-bc58-137148b56a6f | eci.ins.s-general-2x4 | 2 | 4 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |
| flav-70a62913-b591-40d0-8774-7d79d2fdfd37 | eci.ins.s-general-4x8 | 4 | 8 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |
| flav-e63afe0f-7fe5-4afd-96a3-88046dd08aaf | eci.ins.s-general-8x16 | 8 | 16 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |

### **Minion Node Flavor** 

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Flavor ID** | Tên Flavor | **CPU** | **Bộ nhớ RAM (GB)** | GPU | CPU Flatform |
| **Flavor ID** | Tên Flavor | **CPU** | **Bộ nhớ RAM (GB)** | GPU | CPU Flatform |
| flav-49528db1-71d2-452f-bf75-e48c7ae0922f | eci.ins.s1-highmem-2x16 | 2 | 16 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-a3b67f38-dd45-47e3-8755-273b6b1e506f | eci.ins.s1-highmem-4x32 | 4 | 32 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-54a945d5-a811-4c55-a22f-6b3338223794 | eci.ins.s1-highmem-8x64 | 8 | 64 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-bf0dc4ef-3262-4730-a1fb-14eb27ba1fdb | eci.ins.s1-highmem-16x128 | 16 | 128 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-50d0f16b-cc73-4301-ae6e-07ef3b538a6c | eci.ins.s1-highmem-32x256 | 32 | 256 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-afef7157-38ac-49e0-8329-327f1559733e | eci.ins.s1-standard-2x8 | 2 | 8 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-bb0bc0db-2710-44a1-933e-2b9e1fb99d6e | eci.ins.s1-standard-4x16 | 4 | 16 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-d83e3d9d-83a6-4935-aca7-e7891a415a51 | eci.ins.s1-standard-8x32 | 8 | 32 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-4ee7c1db-ad75-4b0a-9f8a-3e43f0b27df3 | eci.ins.s1-standard-16x64 | 16 | 64 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-12f11d02-ab75-4157-8a14-f7be6f14095e | eci.ins.s1-standard-32x128 | 32 | 128 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-a0e2e1b8-4278-441b-9857-465e507fb38f | eci.ins.s1-highcpu-2x2 | 2 | 2 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-4988e043-2cee-4e64-bf8b-e97171a66045 | eci.ins.s1-highcpu-4x4 | 4 | 4 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-e87c9a15-e1bc-4ee1-a25d-389dbadc4325 | eci.ins.s1-highcpu-8x8 | 8 | 8 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |
| flav-152e00ea-5412-44c5-868f-0b30e37e4f90 | eci.ins.s-general-2x4 | 2 | 4 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |
| flav-f5e0201d-606f-4480-be72-de11f46d48ff | eci.ins.s-general-4x8 | 4 | 8 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |
| flav-aece130a-2a09-4d0d-b5eb-0c79589f1547 | eci.ins.s-general-8x16 | 8 | 16 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |
| flav-4b949be1-e3ef-4d73-8ce4-cd264fee86df | eci.ins.s-general-16x32 | 16 | 32 | 0 | Powered by Intel Broadwell and Cascade Lake CPU platforms |
| flav-4d67306c-6fd2-4363-85ac-98e4319d7eb6 | eci.ins.s1-highcpu-16x16 | 16 | 16 | 0 | Powered by Intel Cascade Lake and Ice Lake CPU platforms |

\
