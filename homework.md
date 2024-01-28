# HOME WORK
# Week 1
## Question 1
in CLI:

    docker run --help

## Question 2
using this line in terminal:

    docker run -it --rm python:3.9 /bin/bash
and then:

    pip list

## Question 3

## Question 4
    SELECT MAX(trip_distance) as max_distance,
    DATE(lpep_pickup_datetime) as pickup_date
    FROM green_taxi_data
    GROUP BY pickup_date
    ORDER BY max_distance DESC


## Question 5
    SELECT SUM(total_amount) as total,
    "Borough"
    from green_taxi_data
    left join taxi_zone_data
    on "PULocationID" = "LocationID"
    WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
    GROUP BY "Borough"
    ORDER BY total DESC

## Question 6
    WITH drop_off as(
    SELECT "DOLocationID" as do_location ,max("tip_amount") as max_tip
    FROM green_taxi_data
    LEFT JOIN taxi_zone_data
    ON "PULocationID" = "LocationID"
    WHERE "Zone" like 'Astoria'
    AND date_trunc('month',lpep_pickup_datetime::timestamp) = '2019-09-01'
    GROUP BY 1
    )
    select "max_tip","Zone"
    from drop_off
    left join taxi_zone_data
    ON "do_location" = "LocationID"
    ORDER BY 1 DESC

## Question 7
