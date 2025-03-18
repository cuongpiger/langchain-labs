# Pull và Push image với docker

_\*Yêu cầu máy tính đã cài Docker engine (như Docker Desktop)_

## Push Image

Đầu tiên để có thể push image thì ta cần có sẵn 1 Repository trên vCR, ví dụ ta đã tạo sẵn 1 repo như sau:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(13)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Để push image lên Repo, trước tiên ta cần gắn tag cho image

| “docker tag SOURCE\_IMAGE\[:TAG] vcr.vngcloud.vn/96000-sdkimage/IMAGE\[:TAG]” docker tag 09042024/hello-world vcr.vngcloud.vn/96000-sdkimage/hello-world:first |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- |

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Login bằng user/pass Repo

| docker login vcr.vngcloud.vn -u 96000-khaivt |
| -------------------------------------------- |

Với user là 96000-khaivt (xem trên portal) và pass là secret key khi tạo user

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

* Push image lên Repo:

| ![](https://docs.vngcloud.vn/vng-cloud-document/vn/vcontainer-registry/truong-hop-su-dung/file:/C:/Users/LAP14383-local/AppData/Local/Packages/oice_16_974fa576_32c1d314_3436/AC/Temp/msohtmlclip1/01/clip_image005.gif)    docker push vcr.vngcloud.vn/96000-sdkimage/IMAGE\[:TAG] docker push vcr.vngcloud.vn/96000-sdkimage/hello-world:first |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)

## Pull Image

Đầu tiên ta cũng cân login bằng user và password như lúc push, sau đó thực hiện pull bằng lệnh sau:

| docker pull vcr.vngcloud.vn/96000-sdkimage/IMAGE\[:TAG] docker pull vcr.vngcloud.vn/96000-sdkimage/hello-world:first |
| -------------------------------------------------------------------------------------------------------------------- |

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png?raw=true)
