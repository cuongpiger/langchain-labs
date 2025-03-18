# Các cấu hình hỗ trợ

Hiện tại Dịch vụ VPN đang hỗ trợ đa số các loại Cấu hình phổ biến có thể tương thích một các rộng rãi. Người dùng có thể tham khảo ở đây

### Authenticated Encryption (AEAD) Algorithms 

| Keyword | Description | Note |
| --- | --- | --- |
| aes256gcm128 | 256 bit AES-GCM with 128 bit ICV | default value |
| aes192gcm128 | 192 bit AES-GCM with 128 bit ICV |  |
| aes128gcm128 | 128 bit AES-GCM with 128 bit ICV |  |
| aes256gcm96 | 256 bit AES-GCM with 96 bit ICV |  |
| aes192gcm96 | 192 bit AES-GCM with 96 bit ICV |  |
| aes128gcm96 | 128 bit AES-GCM with 96 bit ICV |  |
| aes256gcm64 | 256 bit AES-GCM with 64 bit ICV |  |
| aes192gcm64 | 192 bit AES-GCM with 64 bit ICV |  |
| aes128gcm64 | 128 bit AES-GCM with 64 bit ICV |  |
| aes256ccm128 | 256 bit AES-CCM with 128 bit ICV |  |
| aes192ccm128 | 192 bit AES-CCM with 128 bit ICV |  |
| aes128ccm128 | 128 bit AES-CCM with 128 bit ICV |  |
| aes256ccm96 | 256 bit AES-CCM with 96 bit ICV |  |
| aes192ccm96 | 192 bit AES-CCM with 96 bit ICV |  |
| aes128ccm96 | 128 bit AES-CCM with 96 bit ICV |  |
| aes256ccm64 | 256 bit AES-CCM with 64 bit ICV |  |
| aes192ccm64 | 192 bit AES-CCM with 64 bit ICV |  |
| aes128ccm64 | 128 bit AES-CCM with 64 bit ICV |  |
| aes256 | 256 bit AES-CBC |  |
| aes192 | 192 bit AES-CBC |  |
| aes128 | 128 bit AES-CB |  |

### Integrity Algorithms (Hashing) 

_Hash is ignored with GCM algorithms_

| Keyword | Description | isDefault |
| --- | --- | --- |
| sha2_256 | SHA2_256_128 HMAC (128 bit) | default value |
| sha2_384 | SHA2_384_192 HMAC (192 bit) |  |
| sha2_512 | SHA2_512_256 HMAC (256 bit) |  |
| sha | SHA1 HMAC (96 bit) | weak security |
| md5 | MD5 HMAC (96 bit) | weak security |

### Diffie Hellman Groups

| Keyworkd | Description | Note |
| --- | --- | --- |
| modp8192 | 18 (8192 bit) |  |
| modp6144 | 17 (6144 bit) |  |
| modp4096 | 16 (4096 bit) |  |
| modp3072 | 15 (3072 bit) |  |
| modp2048 | 14 (2048 bit) | default value |
| modp1536 | 5 (1536 bit) | weak security |
| modp1024 | 2 (1024 bit) | weak security |
| modp768 | 1 (768 bit) | weak security |

###  

