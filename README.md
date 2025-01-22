# SeoulSight
<br>

## 목차
1.[기획](#기획)


<br>

---

<br>


## MEMBERS
|<img src="https://avatars.githubusercontent.com/u/98368034?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/49242646?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/103468518?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/103871252?v=4" width="150" height="150"/>|
|:-:|:-:|:-:|:-:|
|장수현<br/>[@Aunsxm](https://github.com/Aunsxm)|최윤정<br/>[@letmeloveyou82](https://github.com/letmeloveyou82)|김창성<br/>[@kcs19](https://github.com/kcs19)|김우현<br/>[@woody6624](https://github.com/woody6624)|

## 기획
- 사용할 데이터 소스
  - 

## 아키텍처
![Image](https://github.com/user-attachments/assets/52c258f3-f856-476a-9e4e-cdaf404212ee)

## 사용한 필드 설명

| **필드명**          | **데이터 타입**      | **내용**                                                                 |
|----------------------|----------------------|---------------------------------------------------------------------------|
| `area_nm`           | `VARCHAR(255)`      | 지역 이름 (예: 광화문·덕수궁)                                             |
| `area_cd`           | `VARCHAR(50)`       | 지역 코드 (예: POI009)                                                   |
| `area_congest_lvl`  | `VARCHAR(50)`       | 혼잡 수준 (예: 약간 붐빔)                                                 |
| `area_congest_msg`  | `TEXT`              | 혼잡 메시지                                                              |
| `area_ppltn_min`    | `INT`               | 최소 인구 수 (예: 40000)                                                 |
| `area_ppltn_max`    | `INT`               | 최대 인구 수 (예: 42000)                                                 |
| `male_ppltn_rate`   | `FLOAT`             | 남성 인구 비율 (예: 50.8)                                                |
| `female_ppltn_rate` | `FLOAT`             | 여성 인구 비율 (예: 49.2)                                                |
| `ppltn_rate_0`      | `FLOAT`             | 0대 인구 비율 (예: 0.1)                                                  |
| `ppltn_rate_10`     | `FLOAT`             | 10대 인구 비율 (예: 1.3)                                                 |
| `ppltn_rate_20`     | `FLOAT`             | 20대 인구 비율 (예: 15.5)                                                |
| `ppltn_rate_30`     | `FLOAT`             | 30대 인구 비율 (예: 27.6)                                                |
| `ppltn_rate_40`     | `FLOAT`             | 40대 인구 비율 (예: 27.3)                                                |
| `ppltn_rate_50`     | `FLOAT`             | 50대 인구 비율 (예: 17.3)                                                |
| `ppltn_rate_60`     | `FLOAT`             | 60대 인구 비율 (예: 7.2)                                                 |
| `ppltn_rate_70`     | `FLOAT`             | 70대 이상 인구 비율 (예: 3.7)                                            |
| `temp`              | `FLOAT`             | 현재 온도 (예: 4.7)                                                      |
| `sensible_temp`     | `FLOAT`             | 체감 온도 (예: 4.8)                                                      |
| `wind_spd`          | `FLOAT`             | 풍속 (예: 2.8)                                                           |
| `precipitation`     | `VARCHAR(50)`       | 강수량 (예: -)                                                           |
| `pcp_msg`           | `TEXT`              | 강수 메시지 (예: 비 또는 눈 소식이 없어요.)                              |
| `uv_index`          | `VARCHAR(50)`       | 자외선 지수 (예: 낮음)                                                   |
| `uv_msg`            | `TEXT`              | 자외선 메시지                                                            |
| `pm25_index`        | `VARCHAR(50)`       | PM2.5 지수 (예: 매우나쁨)                                                |
| `pm25`              | `INT`               | PM2.5 농도 (예: 125)                                                     |
| `pm10_index`        | `VARCHAR(50)`       | PM10 지수 (예: 나쁨)                                                     |
| `pm10`              | `INT`               | PM10 농도 (예: 138)                                                      |
| `air_idx`           | `VARCHAR(50)`       | 대기질 지수 (예: 점검중)                                                 |
| `air_idx_mvl`       | `VARCHAR(50)`       | 대기질 이동 지수 (예: 점검중)                                            |
| `air_msg`           | `TEXT`              | 대기질 메시지                                                            |
| `weather_time`      | `DATETIME`          | 날씨 데이터 시간 (예: 2025-01-21 12:40)                                  |
| `warn_val`          | `VARCHAR(50)`       | 경고 값 (예: 한파)                                                       |
| `warn_stress`       | `VARCHAR(50)`       | 경고 수준 (예: 주의보)                                                   |
| `announce_time`     | `INT`               | 발표 시간 (예: 0)                                                        |
| `command`           | `VARCHAR(50)`       | 명령 상태 (예: 해제)                                                     |
| `cancel_yn`         | `VARCHAR(50)`       | 취소 여부 (예: 정상)                                                     |
| `warn_msg`          | `TEXT`              | 경고 메시지 (예: 해당 특보는 해제되었습니다.)                            |

---


## 시각화 데이터
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/1511ac5c-4690-41ea-9e25-1853b04565d4" alt="Image"></td>
    <td><img src="https://github.com/user-attachments/assets/517c7b3c-8ef1-46a6-be71-3abf5b541cd9" alt="Image"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/dd4c6edc-e142-44f8-bc24-bab4b061b561" alt="Image"></td>
    <td><img src="https://github.com/user-attachments/assets/9c75434d-9613-4f00-b713-8c2d872d06f5" alt="Image"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="https://github.com/user-attachments/assets/c6b9a6a3-97d2-4772-85b6-3c3d34fba3ab" alt="Image"></td>
  </tr>
</table>


## 데이터 파싱

#### 1. XML형식 데이터 파싱
제공받은 API의 데이터 형식이 XML이었기 때문에, 필요한 정보만 추출하여 딕셔너리 형태로 반환하였습니다.
```
def fetch_and_parse_api_data(api_key, area_name):
    url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/citydata/1/5/{area_name}'
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        data = {
            "area_nm": root.findtext('.//AREA_NM', default=''),
            "area_cd": root.findtext('.//AREA_CD', default=''),
           ...
            "warn_msg": root.findtext('.//WARN_MSG', default='')
        }
        
        
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
```

#### 2. mysql 데이터 삽입
10분마다 최신 데이터를 MySQL 데이터베이스에 업데이트하여 최신 정보를 유지합니다.
해당 데이터가 이미 데이터베이스에 존재하는지 확인하고, 존재하면 갱신하고, 없으면 새로 삽입합니다.
```
def upsert_data_into_mysql(data, db_config, table_name):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Check if area_cd already exists
            select_sql = f"SELECT COUNT(*) FROM {table_name} WHERE area_cd = %s"
            cursor.execute(select_sql, (data["area_cd"],))
            result = cursor.fetchone()

            if result[0] > 0:  # area_cd exists, perform UPDATE
                update_columns = ", ".join([f"{key} = %s" for key in data.keys()])
                update_sql = f"UPDATE {table_name} SET {update_columns} WHERE area_cd = %s"
                cursor.execute(update_sql, list(data.values()) + [data["area_cd"]])
                print(f"Data for {data['area_cd']} has been updated.")
            else:  # area_cd does not exist, perform INSERT
                columns = ", ".join(data.keys())
                placeholders = ", ".join(["%s"] * len(data))
                insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(insert_sql, list(data.values()))
                print(f"Data for {data['area_cd']} has been inserted into the database.")

            connection.commit()

    except Exception as e:
        print(f"MySQL error: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
  while True:
          # Fetch and insert or update data for each area
          for area in areas:
              parsed_data = fetch_and_parse_api_data(API_KEY, area)
              if parsed_data:
                  upsert_data_into_mysql(parsed_data, DB_CONFIG, TABLE_NAME)
          
          print("Waiting for 10 minutes before the next fetch...")
          time.sleep(600)  # 600 seconds = 10 minutes
```



## 트러블 슈팅
주제 : 운영체제에 설치된 JDK-17로 Logstash 구동하기

문제 : Logstash가 서브 프로세스들을 관리하기 위하여 JDK의 IO 서브 시스템에 대하여 open access권한을 요청하지만 JDK 버전의 문제로 IO 서브 시스템에 대한 접근이 제한되어 문제가 발생

### JDK 16에서의 변화
출처 : https://blogs.oracle.com/javakr/post/jdk-16

JEP 396: JDK 내부를 강력하게 캡슐화  - JDK 9에서 내부 API를 강력하게 캡슐화하여 액세스 권한을 제한
이로 인하여 open access권한이 제한됩니다. 이를 해결해주어야 Warning에 대한 문제가 사라집니다.

```
WARNING, using JAVA_HOME while Logstash distribution comes with a bundled JDK
2025-01-21T17:34:36.483+09:00 [main] WARN FilenoUtil : Native subprocess control requires open access to the JDK IO subsystem
Pass '--add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.base/java.io=ALL-UNNAMED' to enable.
```
![Image](https://github.com/user-attachments/assets/ac747e92-2754-4d2b-b851-6a7a8c508067)

### 해결 방법
파일 수정 - logstash 하단의 jvm.options 파일 수정
```
-Xmx1g 밑 부분에
--add-opens java.base/sun.nio.ch=ALL-UNNAMED
--add-opens java.base/java.io=ALL-UNNAMED
를 추가해줍니다.

첫번째 명령어는 module-info.java가 없는 모든 unnamed 모듈에서 JDK의 기본 모듈에서
저수준 I/O관련 클래스들을 포함하고 있는 JAVA NIO 내부 구현과 관련된 패키지에 접근을 
가능하게 해줍니다.
두번째 명령어는 java.io패키지에 모든 unnamed 모듈이 접근 가능하도록 해줍니다.

또한 ## GC configuration 밑 부분에 
-XX:+IgnoreUnrecognizedVMOptions
를 추가하여 혹여나 JVM 버전 차이로 인하여 인식하지 못하는 명령이 있을 경우 무시하는 옵션을
추가합니다.
```

### 결과
FilenoUtil에 대한 Openacess 권한 문제에 대한 내용이 해결되어 나타나지 않습니다.
![Image](https://github.com/user-attachments/assets/1960d0b2-0dbd-462b-9f98-546ce40e0147)
```
C:\02.devEnv\ELK\logstash-7.11.1\bin>logstash -f ../config/test.conf
Using JAVA_HOME defined java: C:\02.devEnv\jdk-17
WARNING, using JAVA_HOME while Logstash distribution comes with a bundled JDK
Sending Logstash logs to C:/02.devEnv/ELK/logstash-7.11.1/logs which is now configured via log4j2.properties
```
