DROP TABLE place;

CREATE TABLE place (
    area_nm VARCHAR(255) NOT NULL, -- 지역 이름 (예: 광화문·덕수궁)
    area_cd VARCHAR(50) NOT NULL, -- 지역 코드 (예: POI009)
    area_congest_lvl VARCHAR(50), -- 혼잡 수준 (예: 약간 붐빔)
    area_congest_msg TEXT, -- 혼잡 메시지
    area_ppltn_min INT, -- 최소 인구 수 (예: 40000)
    area_ppltn_max INT, -- 최대 인구 수 (예: 42000)
    male_ppltn_rate FLOAT, -- 남성 인구 비율 (예: 50.8)
    female_ppltn_rate FLOAT, -- 여성 인구 비율 (예: 49.2)
    ppltn_rate_0 FLOAT, -- 0대 인구 비율 (예: 0.1)
    ppltn_rate_10 FLOAT, -- 10대 인구 비율 (예: 1.3)
    ppltn_rate_20 FLOAT, -- 20대 인구 비율 (예: 15.5)
    ppltn_rate_30 FLOAT, -- 30대 인구 비율 (예: 27.6)
    ppltn_rate_40 FLOAT, -- 40대 인구 비율 (예: 27.3)
    ppltn_rate_50 FLOAT, -- 50대 인구 비율 (예: 17.3)
    ppltn_rate_60 FLOAT, -- 60대 인구 비율 (예: 7.2)
    ppltn_rate_70 FLOAT, -- 70대 이상 인구 비율 (예: 3.7)
    temp FLOAT, -- 현재 온도 (예: 4.7)
    sensible_temp FLOAT, -- 체감 온도 (예: 4.8)
    wind_spd FLOAT, -- 풍속 (예: 2.8)
    precipitation VARCHAR(50), -- 강수량 (예: -)
    pcp_msg TEXT, -- 강수 메시지 (예: 비 또는 눈 소식이 없어요.)
    uv_index VARCHAR(50), -- 자외선 지수 (예: 낮음)
    uv_msg TEXT, -- 자외선 메시지
    pm25_index VARCHAR(50), -- PM2.5 지수 (예: 매우나쁨)
    pm25 INT, -- PM2.5 농도 (예: 125)
    pm10_index VARCHAR(50), -- PM10 지수 (예: 나쁨)
    pm10 INT, -- PM10 농도 (예: 138)
    air_idx VARCHAR(50), -- 대기질 지수 (예: 점검중)
    air_idx_mvl VARCHAR(50), -- 대기질 이동 지수 (예: 점검중)
    air_msg TEXT, -- 대기질 메시지
    weather_time DATETIME, -- 날씨 데이터 시간 (예: 2025-01-21 12:40)
    warn_val VARCHAR(50), -- 경고 값 (예: 한파)
    warn_stress VARCHAR(50), -- 경고 수준 (예: 주의보)
    announce_time INT, -- 발표 시간 (예: 0)
    command VARCHAR(50), -- 명령 상태 (예: 해제)
    cancel_yn VARCHAR(50), -- 취소 여부 (예: 정상)
    warn_msg TEXT -- 경고 메시지 (예: 해당 특보는 해제되었습니다.)
);

show tables;
