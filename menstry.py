import tkinter
from tkinter import *
from tkinter import ttk

main = Tk()
main.title('Menstrual Cycle Calculator')
main.configure(bg="white")

 
def answer(event):
    monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    try:
        int_day = int(day_entry.get())
        str_month = str(monthvar.get())
        capital_month=str_month.capitalize()
        if (capital_month in monthlist): 
            if capital_month == "January":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    day_error.set("")
                    month_error.set("")
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of January")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of February")
            elif capital_month == "February":
                if int_day>29:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=29:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of February")
                    else: 
                        str_calc = str(calc-29)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of March")
            
            elif capital_month == "March":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!") 
                else:
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of March")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of April")
            
            elif capital_month == "April":
                if int_day>30:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=30:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of April")
                    else: 
                        str_calc = str(calc-30)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of May")
            
            elif capital_month == "May":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of May")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of June")
            
            elif capital_month == "June":
                if int_day>30:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=30:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of June")
                    else: 
                        str_calc = str(calc-30)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of July")
            
            elif capital_month == "July":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of July")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of August")
            
            elif capital_month == "August":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of August")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of September")
            
            elif capital_month == "September":
                if int_day>30:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=30:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of September")
                    else: 
                        str_calc = str(calc-30)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of October")
            
            elif capital_month == "October":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of October")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of November")
            
            elif capital_month == "November":
                if int_day>30:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=30:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of November")
                    else: 
                        str_calc = str(calc-30)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of December")
            
            elif capital_month == "December":
                if int_day>31:
                    final.set("") 
                    day_error.set("*Incorrect day!")
                else:
                    calc = int_day+28
                    if calc<=31:
                        str_calc = str(calc)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next menstruation starts on the "+str_calc+" of December")
                    else: 
                        str_calc = str(calc-31)
                        if len(str_calc) == 1:
                            if "1" in str_calc:
                                str_calc = str_calc+"st"
                            elif "2" in str_calc:
                                str_calc = str_calc+"nd"
                            elif "3" in str_calc:
                                str_calc = str_calc+"rd"
                            else:
                                str_calc = str_calc+"th"
                        else: 
                            if "1" is not str_calc[0]:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"st"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"nd"
                                elif "3" is str_calc[1]:
                                    str_calc = str_calc+"rd"
                                else:
                                    str_calc = str_calc+"th"
                            else:
                                if "1" is str_calc[1]:
                                    str_calc = str_calc+"nth"
                                elif "2" is str_calc[1]:
                                    str_calc = str_calc+"th"
                                else:
                                    str_calc = str_calc+"nth"
                        day_error.set("")
                        month_error.set("")
                        final.set("Your next mentruation starts on the "+str_calc+" of January")
            
        else:
            final.set("")
            month_error.set("*Incorrect month")
    except:
        day_error.set("* Incorrect day")

day_month = LabelFrame(main, text="Start Date")
day_month.grid(row=0, column=0, padx=20, pady=5, columnspan=5)

day_error = StringVar()
month_error = StringVar()
final = StringVar()

day_label = Label(day_month, text="Day:")
day_label.grid(row=0, column=0, padx=5, sticky=W)

day_entry = Entry(day_month, width=6, highlightcolor="sky blue", highlightthickness=0.5)
day_entry.grid(row=0, column=1, padx=6, sticky=E)
day_entry.bind('<Return>', answer)


error_labeld = Label(day_month, textvariable=day_error, fg="red")
error_labeld.grid(row=1, column=0, pady=5, padx=5, sticky=W, columnspan=3)

error_labelm = Label(day_month, textvariable=month_error, fg="red")
error_labelm.grid(row=1, column=3, pady=5, padx=5, sticky=W, columnspan=2)

monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthvar = StringVar(day_month)
monthvar.set(monthlist[0])
month_label = Label(day_month, text="Month:")
month_label.grid(row=0, column =2, padx=5, sticky=W)
month_menu = ttk.Combobox(day_month, textvariable=monthvar, values=monthlist)
month_menu.grid(row=0, column=3, padx=5, sticky=E)
month_menu.bind('<Return>', answer)



result_msg = Message(main, textvariable = final, width=200, justify=LEFT)
result_msg.grid(row=2, column=0, sticky=W, columnspan=5, padx=10, rowspan=3)


result = Button(main, text="Calculate", bg="white", highlightcolor="sky blue", relief=GROOVE, highlightbackground="sky blue", highlightthickness=2)
result.grid(row=5, column=0, columnspan=5, pady=10)
result.bind('<Button-1>', answer)
result.bind('<Return>', answer)

main.mainloop()
