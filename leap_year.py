# leap year
# 判断一个年份是闰年
# 能同时被4和100整除
# 或者被400整除
year = float(input('please input years:'))
def leap_year(year)
if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
    print ('leap year')
else:
    print ('common year')

leap_year(float(input('please input years:')))
