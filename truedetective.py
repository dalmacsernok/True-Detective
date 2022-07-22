def is_twodigit_odd(number):
    return ((number % 2 != 0) and (len(str(number)) == 2))


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return True if sudo_mode else True if user == file_owner and writable_by_owner else True if file_group in users_groups and writable_by_group else True if writable_by_others else False
   

def is_leap_year(year):
    return (((year % 4 == 0) and (year % 100 != 00)) or (year % 400 == 0))


def is_sunday(day, weekday_of_first):
    days = {"M": 0, "Tu": 1, "W": 2, "Th": 3, "F": 4, "Sa": 5, "Su": 6}
    for key, value in days.items():
        if weekday_of_first == key: 
            return day <= 31 and (day + value) % 7 == 0 


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return True if (rains and wind_scale < 7) else True if cloudy and wind_scale < 7 and (red_sky or strong_flower_smell or spiders_down or lying_cattle) else True if strong_sunshine and wind_scale < 7 else False
 

def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return False if want_to and trouble_sleeping else False if after_4pm else False if at_work and mad_boss else True if have_30m else True if have_10m else False
