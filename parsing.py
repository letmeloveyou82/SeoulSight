import requests
import xml.etree.ElementTree as ET
import pymysql
import time

from config import API_KEY, DB_CONFIG

# Function to fetch and parse API data
def fetch_and_parse_api_data(api_key, area_name):
    url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/citydata/1/5/{area_name}'
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        data = {
            "area_nm": root.findtext('.//AREA_NM', default=''),
            "area_cd": root.findtext('.//AREA_CD', default=''),
            "area_congest_lvl": root.findtext('.//AREA_CONGEST_LVL', default=''),
            "area_congest_msg": root.findtext('.//AREA_CONGEST_MSG', default=''),
            "area_ppltn_min": root.findtext('.//AREA_PPLTN_MIN', default=''),
            "area_ppltn_max": root.findtext('.//AREA_PPLTN_MAX', default=''),
            "male_ppltn_rate": root.findtext('.//MALE_PPLTN_RATE', default=''),
            "female_ppltn_rate": root.findtext('.//FEMALE_PPLTN_RATE', default=''),
            "ppltn_rate_0": root.findtext('.//PPLTN_RATE_0', default=''),
            "ppltn_rate_10": root.findtext('.//PPLTN_RATE_10', default=''),
            "ppltn_rate_20": root.findtext('.//PPLTN_RATE_20', default=''),
            "ppltn_rate_30": root.findtext('.//PPLTN_RATE_30', default=''),
            "ppltn_rate_40": root.findtext('.//PPLTN_RATE_40', default=''),
            "ppltn_rate_50": root.findtext('.//PPLTN_RATE_50', default=''),
            "ppltn_rate_60": root.findtext('.//PPLTN_RATE_60', default=''),
            "ppltn_rate_70": root.findtext('.//PPLTN_RATE_70', default=''),
            "temp": root.findtext('.//TEMP', default=''),
            "sensible_temp": root.findtext('.//SENSIBLE_TEMP', default=''),
            "wind_spd": root.findtext('.//WIND_SPD', default=''),
            "precipitation": root.findtext('.//PRECIPITATION', default=''),
            "pcp_msg": root.findtext('.//PCP_MSG', default=''),
            "uv_index": root.findtext('.//UV_INDEX', default=''),
            "uv_msg": root.findtext('.//UV_MSG', default=''),
            "pm25_index": root.findtext('.//PM25_INDEX', default=''),
            "pm25": root.findtext('.//PM25', default=''),
            "pm10_index": root.findtext('.//PM10_INDEX', default=''),
            "pm10": root.findtext('.//PM10', default=''),
            "air_idx": root.findtext('.//AIR_IDX', default=''),
            "air_idx_mvl": root.findtext('.//AIR_IDX_MVL', default=''),
            "air_msg": root.findtext('.//AIR_MSG', default=''),
            "weather_time": root.findtext('.//WEATHER_TIME', default=''),
            "warn_val": root.findtext('.//WARN_VAL', default=''),
            "warn_stress": root.findtext('.//WARN_STRESS', default=''),
            "announce_time": root.findtext('.//ANNOUNCE_TIME', default=''),
            "command": root.findtext('.//COMMAND', default=''),
            "cancel_yn": root.findtext('.//CANCEL_YN', default=''),
            "warn_msg": root.findtext('.//WARN_MSG', default='')
        }
        
        
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Function to insert or update data into MySQL
def upsert_data_into_mysql(data, db_config, table_name):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Check if area_cd already exists
            select_sql = f"SELECT COUNT(*) FROM {table_name} WHERE area_cd = %s"
            cursor.execute(select_sql, (data["area_cd"],))
            result = cursor.fetchone()

            if result[0] > 0:  # area_cd exists, perform UPDATE
                print(data["area_cd"])
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

# Main function
if __name__ == "__main__":
    TABLE_NAME = "place"

    # List of area names to be processed
    areas = [
        '강남 MICE 관광특구', '동대문 관광특구', '명동 관광특구', 
        '이태원 관광특구', '잠실 관광특구', '종로·청계 관광특구', '홍대 관광특구'
    ]

    while True:
        # Fetch and insert or update data for each area
        for area in areas:
            parsed_data = fetch_and_parse_api_data(API_KEY, area)
            if parsed_data:
                upsert_data_into_mysql(parsed_data, DB_CONFIG, TABLE_NAME)
        
        print("Waiting for 10 minutes before the next fetch...")
        time.sleep(600)  # 600 seconds = 10 minutes
