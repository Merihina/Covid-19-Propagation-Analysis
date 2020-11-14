import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

total_population=7776372558 #Total today
#csv reading
confirmed=pd.read_csv(r'time_series_covid19_confirmed_global_iso3_regions.csv')
recovered=pd.read_csv(r'time_series_covid19_recovered_global_iso3_regions.csv')
death=pd.read_csv(r'time_series_covid19_deaths_global_iso3_regions.csv')
#confirmed.head(5)
#print(confirmed.to_string())
# applying groupby() function to group the data  on Country/Region  value.*
#print("grouped by region")
#grouped_confirmed= confirmed.groupby('Country/Region')
#print(grouped_confirmed.first().to_string())
#Total confirmed cases
recent_date=4/7/20
total_cases = confirmed['4/7/20'].sum()
percent_infected=(total_cases/total_population)*100
print('total cases is ',total_cases,'which represent',percent_infected ,'% of the world population')

total_death=death['4/7/20'].sum()
percent_death=(total_death/total_cases)*100
print('Total deceaded is',total_death,'Which represents',percent_death,'% of the total cases ')
total_recovered=recovered['4/7/20'].sum()
percent_recovered=(total_recovered/total_cases)*100
print('Total recovered is ',total_recovered,'which represents',percent_recovered,"% of the total cases")
total_infected=total_cases-total_recovered
percent_infected=(total_infected/total_cases)*100
print('Total infected is',total_infected,'Which represents',percent_infected,'% of the total cases ')
# Pie chart, where the slices will be ordered and plotted counter-clockwise:

x = [total_infected, total_recovered, total_death]
plt.pie(x, labels = ['Infected', 'Recovered','Dead'],colors = ['C9', 'C6','C5'], autopct = lambda x: str(round(x, 2)) + '%', pctdistance = 0.7,explode=(0, 0.1, 0),shadow=True)
plt.title("Corona cases in the world")
plt.show()

#Cases scatter in the world chart
#fig = px.scatter_geo(confirmed, lat=confirmed['Lat'], lon=confirmed['Long'],hover_name=confirmed['Country/Region'],size=confirmed['4/7/20'],projection='natural earth',template='plotly_dark')
#fig.show()


#Top 10 countries contaminated
# applying groupby() function to group the data  on Country/Region  value.
grouped_confirmed = confirmed.groupby(['Country/Region'])['4/7/20'].sum()
#print(grouped_confirmed.to_string())
test = grouped_confirmed.to_frame()
test = test.rename(columns={"Country/Region": "Country","4/7/20": "Cases"})
test = test.sort_values(by=['Cases'],ascending=False)
test = test.head(10).plot(kind='bar', color='purple')
plt.title("Top 10 infected countries")
plt.show()

#Top 10 countries Safest Contries
Safe_confirmed = confirmed.groupby(['Country/Region'])['4/7/20'].sum()
#print(grouped_confirmed.to_string())
Safe = Safe_confirmed.to_frame()
Safe = Safe.rename(columns={"Country/Region": "Country","4/7/20": "Cases"})
Safe = Safe.sort_values(by=['Cases'],ascending=True)
Safe = Safe.head(10).plot(kind='bar')
plt.title("Top 10 safest countries")
plt.ylabel("Number of cases")
plt.show()

#Top 10 countries dead from corona
#applying groupby() function to group the data  on Country/Region  value.
grouped_death = death.groupby(['Country/Region'])['4/7/20'].sum()
test2 = grouped_death.to_frame()
test2 = test2.rename(columns={"Country/Region": "Country","4/7/20": "DeadCounter"})
test2 = test2.sort_values(by=['DeadCounter'],ascending=False)
test2 = test2.head(10).plot(kind='bar',color='red')
plt.ylabel("Number of dead")
plt.title('Top 10 countries with deceaded poeple from Corona')
plt.show()

#Top 10 countries recovered from corona
# applying groupby() function to group the data  on Country/Region  value.
grouped_recovered = recovered.groupby(['Country/Region'])['4/7/20'].sum()
test3 = grouped_death.to_frame()
test3 = test3.rename(columns={"Country/Region": "Country","4/7/20": "HealingCounter"})
test3 = test3.sort_values(by=['HealingCounter'],ascending=False)
test3 = test3.head(10).plot(kind='bar',color='green')
plt.title("Top 10 countries with healed poeple from Corona")
plt.legend("Healing cases")
plt.show()


#USA evolution :
usa_confirmed=confirmed[confirmed["Country/Region"] == 'US']
#print(usa_confirmed.to_string())
col_start=confirmed.columns.get_loc('1/22/20')
col_end=confirmed.columns.get_loc('4/7/20')
data_usa=usa_confirmed.iloc[:1,col_start:col_end]
usa_restored=recovered[recovered["Country/Region"] == 'US']
col_start=recovered.columns.get_loc('1/22/20')
col_end=recovered.columns.get_loc('4/7/20')
data_usa_r=usa_restored.iloc[:1,col_start:col_end]
usa_dead=death[death["Country/Region"] == 'US']
col_start=death.columns.get_loc('1/22/20')
col_end=death.columns.get_loc('4/7/20')
data_usa_d=usa_dead.iloc[:1,col_start:col_end]
#print(data_usa)
print(data_usa.iloc[0])
figure = data_usa.iloc[0].plot.area(stacked=False,label='Infected',color='purple')
figure2 = data_usa_r.iloc[0].plot.area(stacked=False,label='Recovered',color='green')
figure3 = data_usa_d.iloc[0].plot.area(stacked=False,label='Dead',color='red')
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend(loc='best')
plt.title("Evolution of Corona in the USA")
plt.show()

#Global Evolution
global_confirmed = confirmed.drop(['Province/State', 'Country/Region', 'Lat', 'Long','ISO 3166-1 Alpha 3-Codes', 'Region Code', 'Region Name','Sub-region Code', 'Sub-region Name', 'Intermediate Region Code','Intermediate Region Name'],axis=1)
global_recovered = recovered.drop(['Province/State', 'Country/Region', 'Lat', 'Long','ISO 3166-1 Alpha 3-Codes', 'Region Code', 'Region Name','Sub-region Code', 'Sub-region Name', 'Intermediate Region Code','Intermediate Region Name'],axis=1)
global_death = death.drop(['Province/State', 'Country/Region', 'Lat', 'Long','ISO 3166-1 Alpha 3-Codes', 'Region Code', 'Region Name','Sub-region Code', 'Sub-region Name', 'Intermediate Region Code','Intermediate Region Name'],axis=1)

global_confirmed = global_confirmed.sum()
global_recovered = global_recovered.sum()
global_death = global_death.sum()

fig1 = global_confirmed.plot.area(stacked=False, color="purple", label='Confirmed')
fig2 = global_recovered.plot.area(stacked=False, color="green", label='Recovered')
fig3 = global_death.plot.area(stacked=False, color="red", label='Dead')
plt.legend()
plt.title("Global evolution of corona cases ")
plt.show()


#China Evolution
china_cases = confirmed.drop(['Province/State', 'Lat', 'Long','ISO 3166-1 Alpha 3-Codes', 'Region Code', 'Region Name','Sub-region Code', 'Sub-region Name', 'Intermediate Region Code','Intermediate Region Name'],axis=1)
china_cases = china_cases[china_cases['Country/Region']=='China'].groupby(['Country/Region']).sum()
china_cases = china_cases.iloc[0]

china_recovered = recovered.drop(['Province/State', 'Lat', 'Long','ISO 3166-1 Alpha 3-Codes', 'Region Code', 'Region Name','Sub-region Code', 'Sub-region Name', 'Intermediate Region Code','Intermediate Region Name'],axis=1)
china_recovered = china_recovered[china_recovered['Country/Region']=='China'].groupby(['Country/Region']).sum()
china_recovered = china_recovered.iloc[0]

china_death = death.drop(['Province/State', 'Lat', 'Long','ISO 3166-1 Alpha 3-Codes', 'Region Code', 'Region Name','Sub-region Code', 'Sub-region Name', 'Intermediate Region Code','Intermediate Region Name'],axis=1)
china_death = china_death[china_death['Country/Region']=='China'].groupby(['Country/Region']).sum()
china_death = china_death.iloc[0]

fig4 = china_cases.plot.area(stacked=False, color="purple", label='Confirmed')
fig5 = china_recovered.plot.area(stacked=False, color="green", label='Recovered')
fig6 = china_death.plot.area(stacked=False, color="red", label='Dead')
plt.legend()
plt.title("Evolution of Corona in China")
plt.show()


#Tunisia Evolution
tun_confirmed=confirmed[confirmed["Country/Region"] == 'Tunisia']
#print(tun_confirmed.to_string())
col_start=confirmed.columns.get_loc('1/22/20')
col_end=confirmed.columns.get_loc('4/7/20')
data_tun=tun_confirmed.iloc[:1,col_start:col_end]

tun_restored=recovered[recovered["Country/Region"] == 'Tunisia']
col_start=recovered.columns.get_loc('2/22/20')
col_end=recovered.columns.get_loc('4/7/20')
data_tun_r=tun_restored.iloc[:1,col_start:col_end]

tun_dead=death[death["Country/Region"] == 'Tunisia']
col_start=death.columns.get_loc('1/22/20')
col_end=death.columns.get_loc('4/7/20')
data_tun_d=tun_dead.iloc[:1,col_start:col_end]
#print(data_tun)
#print(data_tun.iloc[0])

fig,ax = plt.subplots()
figure4 = data_tun.iloc[0].plot.area(stacked=False,label='Infected',color='purple')
figure5 = data_tun_r.iloc[0].plot.area(stacked=False,label='Recovered',color='green')
figure6 = data_tun_d.iloc[0].plot.area(stacked=False,label='Dead',color='red')
ax.set_xlabel("Date")
ax.set_ylabel("Cases")
ax.legend(loc='best')
plt.title("Evolution of Corona in Tunisia")
plt.show()

#---------------------------------------------------------
#END OF GEOGRAPHY, WE USE OTHER CSV FOR DEMOGRAPHIC
#---------------------------------------------------------

#Main Data used a little of data because don't found CSV

#CSV import for Demographic
Canada_cases=pd.read_csv(r'individual-level-cases.csv')
Canada_mortal=pd.read_csv(r'individual-level-mortality.csv')
Korea_info=pd.read_csv(r'PatientInfo.csv')
Gender=pd.read_csv(r'TimeGender.csv')
Age=pd.read_csv(r'TimeAge.csv')

#China Corona Age retribution :
Confirmed_age = Age.drop(['date','time','deceased'],axis=1)
Death_age = Age.drop(['date','time','confirmed'],axis=1)

Confirmed_age = Confirmed_age.groupby(['age'])['confirmed'].sum()
Death_age = Death_age.groupby(['age'])['deceased'].sum()

figure = Confirmed_age.plot(kind='barh',color='Yellow',edgecolor='orange')
plt.title("China cases by Age")
plt.legend(loc='best')
plt.show()

figure = Death_age.plot(kind='barh',color='gray',edgecolor='black')
plt.title("China death by Age")
plt.legend(loc='best')
plt.show()

#China Corona Sex retribution :
Confirmed_gender = Gender.drop(['date','time','deceased'],axis=1)
Death_gender = Gender.drop(['date','time','confirmed'],axis=1)

Confirmed_gender = Confirmed_gender.groupby(['sex'])['confirmed'].sum()
Death_gender = Death_gender.groupby(['sex'])['deceased'].sum()

figure = Confirmed_gender.plot(kind='bar',color=('pink','blue'),edgecolor=('blue','pink'))
plt.title("China cases by Gender")
plt.show()

figure = Death_gender.plot(kind='bar',color=('red','black'),edgecolor=('black','red'))
plt.title("China death by Gender")
plt.show()

plt.pie(Death_gender, labels = ['Male', 'Female'],colors = ['pink','blue'], autopct = lambda x: str(round(x, 2)) + '%', pctdistance = 0.7,explode=(0, 0))
plt.title("Percentage Infection Gender in China")
plt.show()

plt.pie(Confirmed_gender, labels = ['Male', 'Female'],colors = ['red','black'], autopct = lambda x: str(round(x, 2)) + '%', pctdistance = 0.7,explode=(0, 0))
plt.title("Percentage Death Gender in China")
plt.show()


#Korean Corona Status propagation method
Infection = Korea_info.drop(['global_num', 'sex', 'birth_year', 'age', 'country', 'province', 'city', 'disease', 'infected_by', 'infection_order', 'contact_number', 'symptom_onset_date', 'confirmed_date', 'released_date', 'deceased_date', 'state'],axis=1)
Infection['patient_id'] = 1
Infection = Infection.groupby(['infection_case'])['patient_id'].sum()

figure = Infection.plot(kind='barh',color='turquoise',edgecolor='pink')
plt.title("Case of infection")
plt.legend("Cases")
plt.show()

#Study For Canada
Robin = Canada_cases.drop(['case_id', 'provincial_case_id', 'health_region', 'province', 'country', 'date_report', 'report_week', 'locally_acquired', 'case_source', 'additional_info', 'additional_source', 'method_note'],axis=1)
#Traveled / Cases in Canada
canada_travel = Robin.drop(['age','sex'],axis=1)
canada_travel['travel_history_country'] = 1
canada_travel = canada_travel.groupby(['travel_yn'])['travel_history_country'].sum()
traveled=370
not_traveled=558
x = [traveled,not_traveled]
plt.pie(x, labels = ['traveled', 'didnt travel'],colors = ['orange','brown'], autopct = lambda x: str(round(x, 2)) + '%', pctdistance = 0.7,shadow=True)
plt.title("Traveled or not cases")
plt.show()



#Destination / Cases in Candada
canada_travel = Robin.drop(['age','sex'],axis=1)
canada_travel['travel_yn'] = 1
canada_travel = canada_travel.groupby(['travel_history_country'])['travel_yn'].sum().sort_values(ascending=False)
figure = canada_travel.head(15).plot(kind='bar',color=('white','darkblue','C3','C4','C5','C6','C7','C8','C9','C1','C2','yellow','gray','pink','turquoise'))
plt.title("Province of corona to Canada")
plt.legend(loc='best')
plt.show()
