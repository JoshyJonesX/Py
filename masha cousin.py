# Constants
STA_WORK_WEEK_HRS = 39  # Standard hour working per week
STA_PAY_RATE = 35  # Standard pay rate per hour
OVER_TIME_PAY = 50  # 50 euro additional hour
VAT_RATE = 0.21  # 21% Vat Rate
TAX_EXCLUSIVE = 18000

# Assumed Constants
WORKED_WEEK = 52   # Weeks in a year

# Algorithm


# pay = STA_WORK_WEEK_HRS * STA_PAY_RATE
# gross_per_year = pay * 52
# annual_salary = gross_per_year
def computeGrossPay(h):
    if hours_worked >= 0:
        if hours_worked <= 39:
            standard_amount = hours_worked * STA_PAY_RATE
            grossPay = standard_amount
            ovr_time_amount = 0
        elif hours_worked >= 39:
            standard_amount = STA_WORK_WEEK_HRS * STA_PAY_RATE
            extra_hours = hours_worked - 39
            ovr_time_amount = extra_hours * 50 
            grossPay = standard_amount + ovr_time_amount
    return [standard_amount, grossPay, ovr_time_amount]


# Inputs
hours_worked = float(input("Enter hour of work this week: "))

pay = computeGrossPay((hours_worked))

standard_amount = pay[0]
gross_pay = pay[1]
ovr_time_amount = pay[2]

yearly_pay = gross_pay * WORKED_WEEK     # Annual Salary

if yearly_pay <= 18000:
    total_tax = 0
    net_pay = gross_pay
else:
    total_tax = gross_pay * VAT_RATE
    net_pay = gross_pay - total_tax

# Results

print("Hours Worked             :", hours_worked)
print("Standard pay amount      :", standard_amount)
print("Over-time pay amount     :", ovr_time_amount)
print("Gross Pay                :", gross_pay)
print("-------------------------------------------------------")
print("Total Tax                :", total_tax)
print("-------------------------------------------------------")
print("Net Pay                  :", net_pay)
