# Project 10 – Food Waste Monitoring System

## Case Study 53

### Project Description
The Food Waste Monitoring System is a Python-based program designed to monitor food preparation and consumption over several days. It compares the number of meals prepared, meals served, and leftover meals. The program calculates the food wastage percentage for each day and identifies days when wastage exceeds the acceptable limit.

### Objectives
- To record the number of meals prepared each day.
- To calculate the number of leftover meals.
- To calculate the food wastage percentage.
- To identify days with excessive food wastage.
- To encourage better food management and reduce waste.

### Assumptions
- The number of meals prepared must be greater than zero.
- Meals served and leftover meals cannot be negative.
- Meals served plus leftover meals should equal meals prepared.
- An acceptable wastage limit of 20% is used as a sample assumption.
- If the wastage percentage exceeds 20%, the day is classified as having high food wastage.

### Concepts Used
- Variables and data types
- Lists
- Arithmetic operators
- Conditional statements
- Loops
- Input validation
- Percentage calculation

### Formula

**Food Wastage Percentage = (Leftover Meals / Prepared Meals) × 100**

### Sample Output 1 – Normal Food Wastage
```text
FOOD WASTE MONITORING SYSTEM

Day 1
Meals Prepared: 100
Meals Served: 90
Leftover Meals: 10
Wastage Percentage: 10.0%
Status: Acceptable Wastage

Day 2
Meals Prepared: 120
Meals Served: 100
Leftover Meals: 20
Wastage Percentage: 16.67%
Status: Acceptable Wastage

Day 3
Meals Prepared: 150
Meals Served: 110
Leftover Meals: 40
Wastage Percentage: 26.67%
Status: High Food Wastage
```

### Sample Output 2 – Food Wastage Summary
```text
FOOD WASTE SUMMARY

Total Meals Prepared: 370
Total Meals Served: 300
Total Leftover Meals: 70
Overall Wastage Percentage: 18.92%

Days Exceeding Acceptable Limit:
Day 3

Food Waste Monitoring Completed.
```

### Project Files
- `main.py` – Python source code
- `README.md` – Project documentation
- `output-screenshots/` – Program output screenshots

### Conclusion
The Food Waste Monitoring System helps track food preparation, consumption, and leftovers across multiple days. It calculates wastage percentages and identifies days with excessive food waste. This project demonstrates the use of Python programming concepts to solve a real-world problem and supports better food management.
