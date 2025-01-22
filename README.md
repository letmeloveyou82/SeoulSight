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

<br>

---

<br>

## 🗒️기획

이 프로젝트는 서울시의 실시간 도시 데이터를 활용하여 외국인 관광객들이 관광 특구(서울시에서 지정한 관광 명소)에 대한 정보를 쉽게 얻을 수 있도록 돕는 것을 목표로 합니다. 날씨, 인구 혼잡도, 연령대별 인구 비율 등의 데이터를 시각화하여 관광객들이 실시간 정보를 기반으로 여행을 더욱 효과적으로 계획할 수 있도록 지원합니다.
### 목표

1. **실시간 업데이트 제공**: 관광 특구의 날씨, 인구 혼잡도, 인구 특성 정보를 실시간으로 제공.
2. **정보 접근성 향상**: 복잡한 데이터를 직관적으로 이해할 수 있도록 시각화.
3. **관광 편의성 증대**: 실시간 및 예측 정보를 기반으로 효과적인 여행 계획 수립 지원.

### 주요 기능

1. **날씨 정보 제공**: 각 관광 특구의 실시간 날씨 정보를 제공하여 야외 활동 준비를 돕습니다.
2. **인구 혼잡도 정보 제공**: 관광 특구의 인구 밀집도를 실시간으로 파악할 수 있도록 지원합니다.
3. **연령대별 인구 비율 제공**: 관광 특구별 연령대 인구 비율을 시각화하여 다양한 연령층의 관심을 충족시킵니다.

<br>

---

<br>

## 👨‍💻기술스택

| **역할**            | **종류**                                                                                                              |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| 🤝 협업 도구         | ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) <br> ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) |
| 🗄️ 데이터베이스      | ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) <br> ![DBeaver](https://img.shields.io/badge/dbeaver-372923.svg?style=for-the-badge&logo=dbeaver&logoColor=white) |
| 💬 커뮤니케이션 도구 | ![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white) <br> ![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) |
| 🛠️ 개발 및 관리 도구 | ![MobaXterm](https://img.shields.io/badge/mobaxterm-2C2E34.svg?style=for-the-badge&logo=mobaxterm&logoColor=white) <br> ![Elasticsearch](https://img.shields.io/badge/elasticsearch-%230377CC.svg?style=for-the-badge&logo=elasticsearch&logoColor=white)<br>![Logstash](https://img.shields.io/badge/Logstash-005571.svg?&style=for-the-badge&logo=Logstash&logoColor=white)|
| :eyes: 시각화 도구 | ![Kibana](https://img.shields.io/badge/Kibana-E8478B.svg?&style=for-the-badge&logo=Kibana&logoColor=white)|

<br>

---

<br>


## 아키텍처
![Image](https://github.com/user-attachments/assets/52c258f3-f856-476a-9e4e-cdaf404212ee)

<br>

---

<br>

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
### Logstash 실행 문제 해결

#### 주제: 운영체제에 설치된 JDK-17로 Logstash 구동하기

### 문제 설명

Logstash가 서브 프로세스들을 관리하기 위해 JDK의 IO 서브 시스템에 대해 open access 권한을 요청하지만, **JDK 버전**의 문제로 IO 서브 시스템에 대한 접근이 제한되어 문제가 발생합니다.

### 오류 메시지:

```
WARNING, using JAVA_HOME while Logstash distribution comes with a bundled JDK
2025-01-21T17:34:36.483+09:00 [main] WARN FilenoUtil : Native subprocess control requires open access to the JDK IO subsystem
Pass '--add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.base/java.io=ALL-UNNAMED' to enable.
```
---

### JDK 9 ~ JDK 17까지의 모듈 시스템 변화

#### JDK 9

- **모듈 시스템 도입**: Java Reflection API를 통해 비공개(private) 클래스 멤버들에 대한 접근이 가능하던 부분을 제한.
- **목표**: 보안성과 유지보수성을 강화하기 위해 내부 요소들에 대한 접근을 제한.
- **완화된 강력한 캡슐화**: JDK 9에서는 JDK 8의 `java.*`나 `sun.*` 패키지에 대해서 리플렉션을 통한 접근을 허용.
    
    #### 리플렉션이란?
    
    - 리플렉션은 **런타임에 클래스, 메소드, 필드, 생성자 등의 정보를 조사하거나 조작할 수 있도록 하는 기능**입니다.
    - 주로 **컴파일 시점에는 알 수 없는 객체의 정보를 런타임에 동적으로 분석하거나 수정**할 때 사용됩니다.

#### JDK 16

- **강력한 캡슐화**: JEP 396을 통해 기본적으로 JDK 내부 패키지에 대한 접근을 차단.
- `-illegal-access` 명령어 옵션의 기본값이 `deny`로 변경되었으며, 특정 패키지에 대한 전체 접근을 `-add-opens` 옵션으로 명시적으로 허용 가능.

#### JDK 17

- **JEP 403 적용**: JDK 내부 요소들에 대한 접근을 완전히 차단.
- `-illegal-access` 옵션 제거.
- `-add-opens`를 사용하여 특정 패키지에 대한 전체 접근 불가능
    - `-add-opens`를 사용하여 특정 패키지 내의 서브 패키지들에 대해 접근을 허용해야 함.

---
### 해결 방법

1. **Logstash 실행 시 JVM 옵션 설정**
    
    **jvm.options 파일**에서 JVM 옵션을 설정합니다.
    
    - `Xmx1g` 설정 아래에 다음 옵션을 추가합니다:
    
    ```
    --add-opens java.base/sun.nio.ch=ALL-UNNAMED
    --add-opens java.base/java.io=ALL-UNNAMED
    ```

    - `-add-opens java.base/sun.nio.ch=ALL-UNNAMED`: `sun.nio.ch` 패키지에 모든 `unnamed` 모듈에서 접근을 허용합니다. 이는 저수준 I/O 관련 클래스를 포함하고 있습니다.
    - `-add-opens java.base/java.io=ALL-UNNAMED`: `java.io` 패키지에 모든 `unnamed` 모듈에서 접근을 허용합니다.
2. **GC 설정 추가**
    
    `GC configuration` 섹션에 다음 옵션을 추가합니다:
    
    ```
    -XX:+IgnoreUnrecognizedVMOptions
    ```
    
    - 이 옵션은 JVM 버전 차이로 인해 일부 명령어가 인식되지 않을 경우 이를 무시하도록 설정합니다.

---

## 결과

- `FilenoUtil`에 대한 Open Access 권한 문제 해결.
- Logstash가 정상적으로 서브 프로세스를 제어하며 실행됩니다.
![Image](https://github.com/user-attachments/assets/78c6bb2f-facd-4abb-b876-b381667f7e91)

---

## 참고 자료

- [JEP 396: Strongly Encapsulate JDK Internals by Default](https://openjdk.org/jeps/396)
- [JEP 403: Strong Encapsulation of JDK Internals](https://openjdk.org/jeps/403)
- https://helloworld.kurly.com/blog/75-java-module-with-gson-serialization/
