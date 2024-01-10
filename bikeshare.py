import time
import pandas as pd
import numpy as np

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
    def get_city():
        """
        Asks the user to input a city and handles invalid inputs.
        Returns:
            (str) city - name of the city to analyze
        """
        while True:
            city = input("Please enter the name of the city (Chicago, New York City, Washington): ")
            city = city.lower()
            if city in ['chicago', 'new york city', 'washington']:
                return city
            else:
                print("Invalid input. Please enter a valid city.")

    city = get_city()

    # TO DO: get user input for month (all, january, february, ... , june)
    def get_month():
        """
        Asks the user to input a month and handles invalid inputs.
        Returns:
            (str) month - name of the month to filter by, or "all" for no month filter
        """
        while True:
            month = input("Please enter the name of the month (January, February, ..., June, or 'all' for no month filter): ")
            month = month.lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                return month
            else:
                print("Invalid input. Please enter a valid month.")

    month = get_month()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day():
        """
        Asks the user to input a day of the week and handles invalid inputs.
        Returns:
            (str) day - name of the day to filter by, or "all" for no day filter
        """
        while True:
            day = input("Please enter the name of the day of the week (Monday, Tuesday, ..., Sunday, or 'all' for no day filter): ")
            day = day.lower()
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                return day
            else:
                print("Invalid input. Please enter a valid day.")

    day = get_day()

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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month()
    most_common_month = df['Month'].mode()[0]

    print("The most common month is:", most_common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Day of Week'] = df['Start Time'].dt.day_name()
    most_common_day = df['Day of Week'].mode()[0]

    print("The most common day of the week is:", most_common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = df['Start Time'].dt.hour()
    most_common_hour = df['Hour'].mode()[0]

    print("The most common start hour is:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_combination = df['Start-End Combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is:", most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = pd.to_datetime(df['Trip Duration'], unit='s')
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel_time)

    # TO DO: display mean travel time
    df['Trip Duration'] = pd.to_datetime(df['Trip Duration'], unit='s')
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("Counts of gender:", gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mode()[0]
    print("The earliest year of birth is:", earliest_year)
    print("The most recent year of birth is:", most_recent_year)
    print("The most common year of birth is:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
