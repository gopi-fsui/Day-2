def is_leap_year(year):
    # first version
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #         return False
    #     return True
    # return False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False
    # given by ai(mind-blowing!!!)
    # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 
