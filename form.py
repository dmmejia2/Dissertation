import Tkinter
from Tkinter import *

fields = [
    "Active_School_Zone",
    "Active_School_Zone_Fl",
    "At_Intrsct_Fl",
    "City_ID",
    "Cmv_Involv_Fl",
    "Cnty_ID",
    "CompositeIndex",
    "CompositeSum",
    "Crash_Date",
    "Crash_Fatal_Fl",
    "Crash_ID",
    "Crash_Sev_ID",
    "Crash_Time",
    "Day_of_Week",
    "Death_Cnt",
    "Harm_Evnt_ID",
    "Light_Cond_ID",
    "Non_Injry_Cnt",
    "Nonincap_Injry_Cnt",
    "Poss_Injry_Cnt",
    "Road_Constr_Zone_Fl",
    "Road_Constr_Zone_Wrkr_Fl",
    "Rpt_Block_Num",
    "Rpt_Hwy_Num",
    "Rpt_Rdwy_Sys_ID",
    "Rpt_Street_Name",
    "Rr_Relat_Fl",
    "Rural_Fl",
    "Schl_Bus_Fl",
    "Surf_Cond_ID",
    "Surf_Type_ID",
    "Sus_Serious_Injry_Cnt",
    "Thousand_Damage_Fl",
    "Tot_Injry_Cnt",
    "Wthr_Cond_ID",
]


def show_entry_fields():
    j = 0
    for item in entry:
        if(item.get()!=""):
            query_element = '"'+fields[j]+'"' +":" + '"'+item.get()+'",'
            print(query_element)

        j += 1
    # print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
entry = list(())
i = 0
k = 0
for value in fields:
    Label(master, height=1, text=value).grid(row=i, column=0)
    e = Entry(master)
    e.grid(pady=.1, row=i, column=1)
    entry.append(e)
    i += 1

# Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Submit Query', command=show_entry_fields).grid(row=i, column=1, sticky=W, pady=4)

mainloop( )




'''


fields = [

    "Active_School_Zone",
    "Active_School_Zone_Fl",
    "At_Intrsct_Fl",
    "Bridge_Detail_ID",
    "City_ID" 
    "Cmv_Involv_Fl",
    "Cnty_ID",
    "CompositeIndex",
    "CompositeSum",
    "Crash_Date",
    "Crash_Fatal_Fl",
    "Crash_ID",
    "Crash_Sev_ID",
    "Crash_Speed_Limit",
    "Crash_Time",
    "Day_of_Week",
    "Death_Cnt",
    "Harm_Evnt_ID",
    "Intrsct_Relat_ID",
    "Investigat_Arrv_Time",
    "Investigat_Notify_Time",
    "Latitude",
    "Light_Cond_ID",
    "Located_Fl",
    "Longitude",
    "Non_Injry_Cnt",
    "Nonincap_Injry_Cnt",
    "NormalizedIndex",
    "Poss_Injry_Cnt",
    "Road_Constr_Zone_Fl",
    "Road_Constr_Zone_Wrkr_Fl",
    "Road_Relat_ID",
    "Road_Type_ID",
    "Rpt_Block_Num",
    "Rpt_Hwy_Num",
    "Rpt_Outside_City_Limit_Fl",
    "Rpt_Rdwy_Sys_ID",
    "Rpt_Road_Part_ID",
    "Rpt_Sec_Block_Num",
    "Rpt_Sec_Hwy_Num",
    "Rpt_Sec_Rdwy_Sys_ID",
    "Rpt_Sec_Road_Part_ID",
    "Rpt_Sec_Street_Name",
    "Rpt_Street_Name",
    "Rr_Relat_Fl",
    "Rural_Fl",
    "Schl_Bus_Fl",
    "Surf_Cond_ID",
    "Surf_Type_ID",
    "Sus_Serious_Injry_Cnt",
    "Thousand_Damage_Fl",
    "Toll_Road_Fl",
    "Tot_Injry_Cnt",
    "Traffic_Cntl_ID",
    "Unkn_Injry_Cnt",
    "Wthr_Cond_ID",
]


fields = [

    "Active_School_Zone",
    "Active_School_Zone_Fl",
    "At_Intrsct_Fl",
    "Bridge_Detail_ID",
    "City_ID" 
    "Cmv_Involv_Fl",
    "Cnty_ID",
    "CompositeIndex",
    "CompositeSum",
    "Crash_Date",
    "Crash_Fatal_Fl",
    "Crash_ID",
    "Crash_Sev_ID",
    "Crash_Speed_Limit",
    "Crash_Time",
    "Day_of_Week",
    "Death_Cnt",
    "Entr_Road_ID",
    "FHE_Collsn_ID",
    "Harm_Evnt_ID",
    "Intrsct_Relat_ID",
    "Investigat_Arrv_Time",
    "Investigat_Notify_Time",
    "Latitude",
    "Light_Cond_ID",
    "Located_Fl",
    "Longitude",
    "Non_Injry_Cnt",
    "Nonincap_Injry_Cnt",
    "NormalizedIndex",
    "Obj_Struck_ID",
    "Othr_Factr_ID",
    "Phys_Featr_1_ID",
    "Phys_Featr_2_ID",
    "Pop_Group_ID",
    "Poss_Injry_Cnt",
    "Report_Date",
    "Road_Cls_ID",
    "Road_Constr_Zone_Fl",
    "Road_Constr_Zone_Wrkr_Fl",
    "Road_Relat_ID",
    "Road_Type_ID",
    "Rpt_Block_Num",
    "Rpt_CRIS_Cnty_ID",
    "Rpt_City_ID",
    "Rpt_Hwy_Num",
    "Rpt_Outside_City_Limit_Fl",
    "Rpt_Rdwy_Sys_ID",
    "Rpt_Road_Part_ID",
    "Rpt_Sec_Block_Num",
    "Rpt_Sec_Hwy_Num",
    "Rpt_Sec_Rdwy_Sys_ID",
    "Rpt_Sec_Road_Part_ID",
    "Rpt_Sec_Street_Name",
    "Rpt_Street_Name",
    "Rr_Relat_Fl",
    "Rural_Fl",
    "Schl_Bus_Fl",
    "Surf_Cond_ID",
    "Surf_Type_ID",
    "Sus_Serious_Injry_Cnt",
    "Thousand_Damage_Fl",
    "Toll_Road_Fl",
    "Tot_Injry_Cnt",
    "Traffic_Cntl_ID",
    "Unkn_Injry_Cnt",
    "Wthr_Cond_ID",
]

'''