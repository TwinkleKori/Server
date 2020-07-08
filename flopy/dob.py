month_names=["january","february","march",
            "aprill","may", "jun", "july ",
             "august", "september","october",
               "november","december"]
suffixes=['st','nd', 'rd']+\
17*['th']+\
['st','nd','rd']+\
7*['th']+\
['st']
dob=input("enter your date of birth in dd-mm-yyyy format:")
dd_mm_yyyy=dob.split("-")
date=int(dd_mm_yyyy[0])
month=int(dd_mm_yyyy[1])
year=dd_mm_yyyy[2]
date_suffix=suffixes[date-1]
full_date=str(date)+date_suffix
month_name=month_names[month-1]
final_date=full_date+"of"+month_name+","+year
print(final_date)