# sqlalchemy-challenge
Module 10 Challenge

## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Analysis
Data analysis showed that the most recent date in the dataset was 23 August 2017. Precipitation data was then studied for a one-year period backwards from that date. The results were then plotted as follows:

![Precipitation](https://github.com/MAamer28/sqlalchemy-challenge/assets/130619866/507a6d96-4881-47db-b071-5b00b482cec1)

The plot indicates rainy springs and summers in the Honolulu area. Below are summary statistics for the precipitation data.

        precipitation
        count	2021.000000
        mean	0.177279
        std	0.461190
        min	0.000000
        25%	0.000000
        50%	0.020000
        75%	0.130000
        max	6.700000

There were 9 stations providing data for this study. A list of stations in descending order of activity was organized as follows:

      [('USC00519281', 2772),
       ('USC00519397', 2724),
       ('USC00513117', 2709),
       ('USC00519523', 2669),
       ('USC00516128', 2612),
       ('USC00514830', 2202),
       ('USC00511918', 1979),
       ('USC00517948', 1372),
       ('USC00518838', 511)]

USC00519281 was the most active station in terms of rows of data collected from that station. Temperature data points from the aforementioned station yielded a minimum, maximum, and average temperature of (54.0,) (85.0,) (71.66378066378067,). A histogram plot was arranged to reflect all temperature data entries for that station over a period of 12 months from the most recent entry of 23 August 2017.

![TOBs](https://github.com/MAamer28/sqlalchemy-challenge/assets/130619866/b484545c-f311-47fb-9906-a63846243211)

## Climate API
See the .py file in the ClimateApp folder for an API returning the answers to the queries above.
