# Intro to NLP - Assignment 1

## Team
|Student name| CCID |
|------------|------|
|dongheng li  |1500760      |


## TODOs

In this file you **must**:
- [ ] Fill out the team table above. Please note that CCID is **different** from your student number.
- [ ] Acknowledge all resources consulted (discussions, texts, urls, etc.) while working on an assignment. Non-detailed oral discussion with others is permitted as long as any such discussion is summarized and acknowledged by all parties.
- [ ] Provide clear installation and execution instructions that TAs must follow to execute your code.
## Installation
Please use 'pip' instead of 'pip3', pip means using the current python, so make sure your python version is 3.7 or newer.

`pip install regex`

`pip install argparse`

`pip install pandas`


## Execution
Use the following command in parent directory of directory data, output and src and file README.md.

`python src/main.py data/dev/ output/dev.csv`

## Data

The assignment's development data can be found inside [data/dev](data/dev).

And after running the main.py, the results file dev.csv can be found under [output/](output/)

## Code
The features are summarized into:

![EXCEL_Sh6R2BV26e](https://user-images.githubusercontent.com/61613205/192934722-25e11ca6-6940-4930-8585-7a16bc7c7363.png)

After read from all files, every files has gone through all the functions below to extract as much info. as it can.
And I designed functions:

`get_dayof_week()` that includes: `dayofweek`

`get_month()` that includes all month related feature:`day-month`, `day-month-year`, `month`, `month`,`relative-year`, `month-day`, `month-year`.

`get_year()` that includes all year related feature:`year`, `day-month-year`, `month-year`, `quarter-of-year`.

`get_relative_year_month_week()` that includes: `relative-year/month/week`, `part-of-relative_year/month/week`, `month,relative-year`.

`get_decade()` that includes:`dacade`, `part-of-dacade`.

`get_relative_years_months_weeks_days()` that includes:`relative-years/months/weeks/days`.

For those overlapping ones, since regex can't exclude from history, it is still easy to log them all and elimilate the dupicate ones using

`df[~df.duplicated()]`

## Conclusion

Overall, all the SIMPLE DATES and DIETIC DATES are extracted from using all the functions and no partial extractions.





