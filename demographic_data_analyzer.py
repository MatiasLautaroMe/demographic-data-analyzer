import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv('adult.data.csv')
    
    # 1. ¿Cuántas personas de cada raza?
    race_count = df['race'].value_counts()
    
    # 2. ¿Cuál es la edad media de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. ¿Porcentaje de personas con Bachelor?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )
    
    # 4. ¿Porcentaje con educación avanzada que gana >50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[advanced_education]['salary'] == '>50K').sum() / 
        len(df[advanced_education]) * 100, 1
    )
    
    # 5. ¿Porcentaje sin educación avanzada que gana >50K?
    no_advanced_education = ~advanced_education
    lower_education_rich = round(
        (df[no_advanced_education]['salary'] == '>50K').sum() / 
        len(df[no_advanced_education]) * 100, 1
    )
    
    # 6. ¿Mínimo de horas trabajadas?
    min_work_hours = df['hours-per-week'].min()
    
    # 7. ¿Porcentaje que trabaja mínimo horas y gana >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').sum() / 
        len(min_workers) * 100, 1
    )
    
    # 8. ¿País con mayor porcentaje que gana >50K?
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').sum() / len(x) * 100
    )
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)
    
    # 9. ¿Ocupación más popular para >50K en India?
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # No modificar
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
