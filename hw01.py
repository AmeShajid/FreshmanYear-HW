#Name: Ame Shajid
#Date: 1/16/23
#Purpose: Compute Gross pay and Net Pay
#Description: This program basically computes your net pay and gross pary with given hourly wage, hours worked, and weeks worked!

#introduction
print("Welcome to Gross and Net Pay Estimator")

#user will input Hourly Wage
HourlyWage = float(input("Enter Hourly Wage in Dollar: " "\n"))

#user will input Hours per Week
Hours= int(input("Enter Hours per week: " "\n"))

#users will input Weeks Per year worked
Weeks= int(input("Enter weeks per year Worked: " "\n"))

#output Gross Pay Information
#Gross pay Weekly
GrossPayWeekly = HourlyWage * Hours
#Gross pay Yearly
GrossPayYearly = HourlyWage * Hours * Weeks

#output Taxes and Deductions
#SocialSecurity Deduction
SocialSecurityTaxes = (GrossPayYearly * .06) 
#Medicare Deduction
MedicareTaxes = (GrossPayYearly - (GrossPayYearly * .06)) * .02
#IRS deduction
IRSTaxes = ((GrossPayYearly - (GrossPayYearly * .06)) - MedicareTaxes) * .12
#PA deduction
PAStatesTaxes =(((GrossPayYearly - (GrossPayYearly * .06)) - MedicareTaxes) - IRSTaxes) * .0307
#Phila Deduction
PhilaTaxes = ((((GrossPayYearly - (GrossPayYearly * .06)) - MedicareTaxes) - IRSTaxes) - PAStatesTaxes) * .0375
#Health Insurance Deduction
HealthInsurance = (396*12) 
print("")

#Net Pay Information
#Net pay answer
NetPay =((((((GrossPayYearly - (GrossPayYearly * .06)) - MedicareTaxes) - IRSTaxes) - PAStatesTaxes) - PhilaTaxes) - HealthInsurance)
#Percent of your Pay
Percent = (NetPay / GrossPayYearly) * 100
#Weekly amount
weekly =((((((GrossPayYearly - (GrossPayYearly * .06)) - MedicareTaxes) - IRSTaxes) - PAStatesTaxes) - PhilaTaxes) - HealthInsurance) / 50
#Hourly Amount
hourly =((((((GrossPayYearly - ((GrossPayYearly * .06)) - MedicareTaxes) - IRSTaxes) - PAStatesTaxes) - PhilaTaxes) - HealthInsurance) / 50) / 40

#Display Results
print("Gross Pay Information")
print(f"You will make ${GrossPayWeekly:.2f} per week")
print(f"You Will make ${GrossPayYearly:.2f} per year \n") 

#Display Taxes and Deductions
print("Taxes and Deductions")
print(f"You Will pay ${SocialSecurityTaxes:.2f} in social Security Taxes")
print(f"You will pay ${MedicareTaxes:.2f} in Medicare Taxes")
print(f"You Will pay ${IRSTaxes:.2f} in IRS Taxes")
print(f"You Will pay ${PAStatesTaxes:.2f} in PA State Taxes")
print(f"You Will pay ${PhilaTaxes:.2f} in Phila Taxes")
print(f"You Will pay ${HealthInsurance:.2f} for Health Insurance")
print("")

#Display Net Pay Information
print("Net Pay Information")
print(f"Your take home pay will be ${NetPay:.2f} per year")
print(f"This is an hourly take home pay of ${hourly:.2f}")
print(f"This is a weekly take home pay of ${weekly:.2f}")
print(f"Your Net pay is {Percent:.2f} percent of your Gross pay")
