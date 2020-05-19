years= [2017,2018,2019]
revenue= [30000,40000,50000]

l1 = list(zip(years, revenue))
print(l1)
sales= dict(zip(years, revenue))
print(sales)
#--calculate the 15% profite margin from the sales data
profit ={k:v*0.15 for k,v in sales.items()}
print(profit)

visits = {'Monday': 5000,
          'Tuesday': 3000,
          'Wednesday': 4000,
          'Thursday': 4500,
          'Friday': 5000,
          'Saturday': 2000,
          'Sunday': 1500
          }

## YOUR CODE STARTS HERE
total_visits=0
for v in visits.values():
    total_visits = total_visits + v
print(visits)
print(total_visits)

percentage={k:(v / total_visits) * 100 for k,v in visits.items()}
print(percentage)