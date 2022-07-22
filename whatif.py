def is_twodigit_odd(number):
    if number % 2 == 0:
        return True
    else: 
        if len(str(number)) == 2:
            return True
        else:
            return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if sudo_mode:
        return True
    if user == file_owner:
        if writable_by_owner:
            return True
    if file_group in users_groups:
        if writable_by_group:
            return True
    if writable_by_others:
        return True
    return False

def is_leap_year(year):
    if (year % 400) == 0:
        return True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    else:
        return False


def is_sunday(day, weekday_of_first):
    days = {"M": 0, "Tu": 1, "W": 2, "Th": 3, "F": 4, "Sa": 5, "Su": 6}
    for key, value in days.items():
        if weekday_of_first == key:
            if day <= 31:
                if (day + value) % 7 == 0:
                    return True
            return False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if rains:
        if wind_scale < 7:
            return True
    if cloudy:
        if wind_scale < 7:
            if red_sky:
                return True
            if strong_flower_smell:
                return True
            if spiders_down:
                return True
            if lying_cattle:
                return True
    if strong_sunshine:
        if wind_scale < 7:
            return True            
    return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to:
        if trouble_sleeping:
            return False
    if after_4pm:
        return False
    if at_work:
        if mad_boss:
            return False
    if have_30m:
        return True
    if have_10m:
        return True
    return False
