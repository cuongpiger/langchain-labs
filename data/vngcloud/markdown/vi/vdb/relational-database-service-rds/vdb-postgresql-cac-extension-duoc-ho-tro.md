# vDB PostgreSQL - Các extension được hỗ trợ

PostgreSQL nổi tiếng với tính linh hoạt. Bạn hoàn toàn có thể mở rộng các core-function của Postgresql bằng các Extensions.

Mặc định, khi khởi tạo một database với vDB PostgreSQL, bạn đã được bật sẵn một số extension (danh sách bên dưới), ngoài ra bạn cũng có thể chủ động bật thêm một số extension khác tùy theo nhu cầu (danh sách bên dưới).

## **1.Danh sách các extension được bật sẵn:** 

Đối với PostgreSQL, các database được tạo mới sẽ được bật sẵn các Extension như trong database **template1.** 

Sau khi tạo database, bạn có thể dùng lệnh:

|  `\dx` |
| ------ |

hoặc

| `select * from pg_extension;`  |
| ------------------------------ |

để xem danh sách các extension đã được bật trên database.

\


Dưới đây là danh sách các extension đã được bật sẵn:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No** | **Name** | **Description** | **Version Postgresql hỗ trợ** | **Version** |
| 1 | btree_gin | support for indexing common datatypes in GIN | TBU | 1.2 |
| 2 | btree_gist | support for indexing common datatypes in GiST | TBU | 1.5 |
| 3 | chkpass | data type for auto-encrypted passwords | TBU | 1 |
| 4 | citext | data type for case-insensitive character strings | TBU | 1.4 |
| 5 | cube | data type for multidimensional cubes | TBU | 1.2 |
| 6 | dict_int | text search dictionary template for integers | TBU | 1 |
| 7 | dict_xsyn | text search dictionary template for extended synonym processing | TBU | 1 |
| 8 | hstore | data type for storing sets of (key, value) pairs | TBU | 1.4 |
| 9 | isn | data types for international product numbering standards | TBU | 1.1 |
| 10 | lo | Large Object maintenance | TBU | 1.1 |
| 11 | ltree | data type for hierarchical tree-like structures | TBU | 1.1 |
| 12 | pg_trgm | text similarity measurement and index searching based on trigrams | TBU |  |
| 13 | plpgsql | PL/pgSQL procedural language | TBU | 1 |
| 14 | postgis | PostGIS geometry, geography, and raster spatial types and functions | TBU | 2.5.4 |
| 15 | postgres_fdw | foreign-data wrapper for remote PostgreSQL servers | TBU |  |
| 16 | unaccent | text search dictionary that removes accents | TBU |  |
| 17 | vector | vector data type and ivfflat and hnsw access methods | 14, 15 | 0.8.0 |

**Lưu ý:** N**ế**u bạn muốn tạo database trắng hoàn toàn, hãy dùng **template0.**

VD:

| `CREATE DATABASE dbname TEMPLATE template0;` |
| -------------------------------------------- |

## **2. Danh sách các extension bạn có thể tự bật:** 

Bạn có thể tự bật một Extension bằng cách chạy lệnh:

| create extension \<extension\_name>; |
| ------------------------------------ |

\


|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Version** |
| address_standardizer | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. | 2.5.4 |
| address_standardizer_data_us | Address Standardizer US dataset example | 2.5.4 |
| amcheck | functions for verifying relation integrity | 1 |
| autoinc | functions for autoincrementing fields | 1 |
| earthdistance | calculate great-circle distances on the surface of the Earth | 1.1 |
| fuzzystrmatch | determine similarities and distance between strings | 1.1 |
| insert_username | functions for tracking who changed a table | 1 |
| intagg | integer aggregator and enumerator (obsolete) | 1.1 |
| intarray | functions, operators, and index support for 1-D arrays of integers | 1.2 |
| moddatetime | functions for tracking last modification time | 1 |
| pageinspect | inspect the contents of database pages at a low level | 1.6 |
| pg_buffercache | examine the shared buffer cache | 1.3 |
| pg_freespacemap | examine the free space map (FSM) | 1.2 |
| pg_prewarm | prewarm relation data | 1.1 |
| pg_stat_statements | track execution statistics of all SQL statements executed | 1.6 |
| pg_trgm | text similarity measurement and index searching based on trigrams | 1.3 |
| pg_visibility | examine the visibility map (VM) and page-level visibility info | 1.2 |
| pgcrypto | cryptographic functions | 1.3 |
| pgrouting | pgRouting Extension | 3.0.0 |
| pgrowlocks | show row-level locking information | 1.2 |
| pgstattuple | show tuple-level statistics | 1.5 |
| postgis_sfcgal | PostGIS SFCGAL functions | 2.5.4 |
| postgis_tiger_geocoder | PostGIS tiger geocoder and reverse geocoder | 2.5.4 |
| postgis_topology | PostGIS topology spatial types and functions | 2.5.4 |
| refint | functions for implementing referential integrity (obsolete) | 1 |
| sslinfo | information about SSL certificates | 1.2 |
| tablefunc | functions that manipulate whole tables, including crosstab | 1 |
| tcn | Triggered change notifications | 1 |
| timetravel | functions for implementing time travel | 1 |
| tsm_system_rows | TABLESAMPLE method which accepts number of rows as a limit | 1 |
| tsm_system_time | TABLESAMPLE method which accepts time in milliseconds as a limit | 1 |
| unaccent | text search dictionary that removes accents | 1.1 |
| uuid-ossp | generate universally unique identifiers (UUIDs) | 1.1 |

bạn có thể dùng lệnh sau để kiểm tra danh sách các extension đang được hỗ trợ trên vDB của mình:

| `select * from pg_available_extensions;` |
| ---------------------------------------- |

Nếu bạn cần extension nào chưa được hỗ trợ, vui lòng liên hệ với **VNG Cloud Support** để được hỗ trợ.



## **3. Lưu ý:** 

\+ Extension vector chỉ available cho các vDB khởi tạo từ 08/01/2024. 

\+ Để sử dụng trên các vDB đã khởi tạo trước đó, bạn vui lòng liên hệ VNG Cloud Support để được hỗ trợ enable.

