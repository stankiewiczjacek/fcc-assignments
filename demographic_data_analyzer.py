import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # Some info about data
    # r5 = df.head(5)
    # print(r5)
    # print(df.columns)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df['race']
    race_count = races.value_counts()

    # What is the average age of men?
    men = df.loc[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bac_deg = df.loc[df['education'] == 'Bachelors']
    percentage_bachelors = round(100*(len(bac_deg))/(len(df)),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    hi_ed_50 = higher_education.loc[higher_education['salary'] == '>50K']
    lo_ed_50 = lower_education.loc[lower_education['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = round(100*(len(hi_ed_50))/(len(higher_education)),1)
    lower_education_rich = round(100*(len(lo_ed_50))/(len(lower_education)),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    hours = df['hours-per-week']
    min_work_hours = hours.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df.loc[df['hours-per-week'] == min_work_hours]
    min_workers_hi = min_workers.loc[min_workers['salary'] == '>50K']

    rich_percentage = round(100*(len(min_workers_hi))/(len(min_workers)),1)

    # What country has the highest percentage of people that earn >50K?
    cs = df['native-country']
    countries_s = cs.value_counts()
    countries = countries_s.to_frame()
    countries['n_rich'] = 0
    for c in countries.index:
        cx1 = df.loc[df['native-country'] == c]
        cx2 = cx1.loc[cx1['salary'] == '>50K']
        countries.at[c, 'n_rich'] = len(cx2)

    countries['r_rich'] = round(100 * countries['n_rich'] / countries['count'],1)
    # print(countries)
    r_rich = countries['r_rich']

    highest_earning_country = countries['r_rich'].idxmax()
    highest_earning_country_percentage = r_rich.max()


    # Identify the most popular occupation for those who earn >50K in India.
    i50 = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    i50jobs = i50['occupation']
    i50list = i50jobs.value_counts()

    top_IN_occupation = i50list.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
