# South-Africa-tax-revenue-spending

I load a CSV file containing South African government spending data, then build a horizontal bar chart showing total spending for each functional classification.

What my code does
I import pandas for reading and working with the CSV, seaborn for styling the chart, and matplotlib.pyplot for drawing it.

I read the file tax_spending (1).csv into a DataFrame called data.

I create an empty dictionary called spending. It will store each spending category as the key and its total spending as the value.

I start a counter at 0 and loop through the rows, stopping three rows before the end: data.shape[0] - 3. This avoids processing the last three rows, which are probably totals or notes rather than normal categories.

Inside the loop, I take the category name from the 'R billion' column and use it as the dictionary key.

I select columns from position 2 up to, but not including, the second-last column using data.iloc[counta][2:-2], convert the values to floats, and add them together.

I store that total in spending[key].

Finally, I use plt.barh() to draw horizontal bars: the dictionary keys become the y-axis labels and the values become the bar lengths.

I add axis labels, a title, a dashed grid, and display the chart with plt.show().

<img width="1920" height="959" alt="tax_rev" src="https://github.com/user-attachments/assets/74f4ccf1-80d1-4c98-9d1c-6858b1752215" />
