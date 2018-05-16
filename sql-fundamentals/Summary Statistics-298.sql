## 1. Introduction ##

SELECT COUNT(Major) from recent_grads where ShareWomen<0.5

## 2. Finding a Column's Minimum and Maximum Values in SQL ##

SELECT Major,Major_category,MIN(Median) from recent_grads
where Major_category='Engineering';

## 3. Calculating Sums and Averages in SQL ##

Select SUM(Total) from recent_grads

## 4. Combining Multiple Aggregation Functions ##

SELECT AVG(Total),MIN(Men),MAX(Women) from recent_grads

## 5. Customizing The Results ##

SELECT COUNT(*) as "Number of Students", MAX(Unemployment_rate) as "Highest Unemployment Rate" from recent_grads

## 6. Counting Unique Values ##

SELECT COUNT(DISTINCT(Major)) as "unique_majors",COUNT(DISTINCT(Major_category)) as "unique_major_categories",COUNT(DISTINCT(Major_code)) as "unique_major_codes"
FROM recent_grads

## 7. Performing Arithmetic in SQL ##

SELECT Major, Major_category, (P75th - P25th) quartile_spread FROM recent_grads ORDER BY quartile_spread LIMIT 20