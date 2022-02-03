create table all_weeks_country_data (
country_name                  varchar(200),
country_iso2                  varchar(200),
week                          date,
category                      varchar(200),
weekly_rank                    number,
show_title                    varchar(200),
season_title                  varchar(200),
cumulative_weeks_in_top_10     number
);

create table all_weeks_global_data (
week                          date,
category                      varchar(200),
weekly_rank                    number,
show_title                    varchar(200),
season_title                  varchar(200),
weekly_hours_viewed            number,
cumulative_weeks_in_top_10     number
);

create table most_popular_data (
category                      varchar(200),
rank                           number,
show_title                    varchar(200),
season_title                  varchar(200),
hours_viewed_first_28_days     number
);