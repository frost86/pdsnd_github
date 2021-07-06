import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter any one of the following cities (Chicago, New York City, Washington): ').lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        city = input('Enter any one of the following cities (Chicago, New York City, Washington): ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter which month you want to filter by (January, February, ... , June, or all): ').lower()
    while month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june' and month != 'all':
        month = input('Enter which month you want to filter by (January, February, ... , June, or all): ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter which day you want to filter by (Monday, Tuesday, ... , Sunday, or all): ').lower()
    while day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day!= 'all':
        day = input('Enter which day you want to filter by (Monday, Tuesday, ... , Sunday, or all): ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # *** SOURCE FOR THE CODE IN THIS FUNCTION: Based on the Practice Problems (No. 3) earlier in the lesson for this project ***
    # Load data into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract the month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # Filter the month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filter the month to create a new dataframe
        df = df[df['month'] == month]
    
    # Filter the day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def start_the_clock():
    start_time = time.time()
    rounded_time = round((time.time() - start_time), 1)
    return rounded_time

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # *** SOURCE FOR THE CODE IN THIS FUNCTION: Based on the Practice Problems (No. 1) earlier in the lesson for this project ***
    
    # TO DO: display the most common month
    # Convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # Find the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    # Convert the Start Time to datetime -- already done above
    # Extract day from the Start Time column to create a day column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # Find the most common day
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day: {}'.format(popular_day))

    # TO DO: display the most common start hour
    # Convert the Start Time to datetime -- already done above
    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # Find the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % start_the_clock())
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common start station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common end station: {}'.format(popular_end_station))

    # *** SOURCE FOR THE CODE IN THIS FUNCTION: https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python (BENY; October 29, 2018) ***
    # TO DO: display most frequent combination of start station and end station trip
    combo_stations = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most common combination of start station and end station: {}'.format(combo_stations))

    print("\nThis took %s seconds." % start_the_clock())
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time: {}'.format(round(total_travel_time, 1)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time: {}'.format(round(mean_travel_time, 1)))

    print("\nThis took %s seconds." % start_the_clock())
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Number of user types:\n{}'.format(user_types))
    print('\n')

    # *** SOURCE FOR THE CODE IN THIS FUNCTION: https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas#24870404 (chrisb; July 21, 2014) ***
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('Number of gender types:\n{}'.format(gender_types))
        print('\n')
    else:
        print('The Gender column does not exist.')
        print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # Earliest year of birth
        print('Earliest year of birth: {}'.format(int(df['Birth Year'].min())))
        # Most recent year of birth
        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        # Most common year of birth
        print('Most common year of birth: {}'.format(int(df['Birth Year'].mode())))
    else:
        print('The Birth Year column does not exist.')
        print('\n')

    print("\nThis took %s seconds." % start_the_clock())
    print('-'*40)

# *** SOURCE FOR THE CODE IN THIS FUNCTION: Based on code provided by Reviewer from initial submission ***
def display_raw_data(df):
    """ If requested by the user, show the raw data 5 rows at a time """
    i = 5
    print('\n')
    raw = input('Would you like to see the first 5 rows of raw data? ').lower()
    pd.set_option('display.max_columns', 200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            # Display next five rows
            print(df.head(i))
            raw = input("Would you like to see the next 5 rows of raw data? ").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            
        while restart != 'yes' and restart != 'no':
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            
        if restart == 'no':
            break


if __name__ == "__main__":
	main()

