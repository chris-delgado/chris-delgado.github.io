---
layout: post
title: Key Takeaways from Supercharge Power BI by Matt Allington
image: "/posts/SuperchargePowerBI.jpeg"
tags: [Books, Power BI]
---
# Supercharge Power BI - Key Takeaways
## Highlights
- Filter propagation
- CALCULATE()
- Context Transition

## 1. Views
<img width="27" alt="Screenshot 2022-11-10 at 10 20 32 AM" src="https://user-images.githubusercontent.com/19756136/204647294-d25906b4-fd87-4b91-8fe1-50acd29f93d2.png">
From top to bottom: Report, Data, Model

## 2. Collie Layout Methodology
![Pasted image 20221110102221](https://user-images.githubusercontent.com/19756136/204647338-954b3788-fb41-4506-996d-745ac6d6a64b.png)
- Use the "Collie layout methodology" as the visual layout of your tables
- Always drag from the data table up to the lookup table when connecting keys

## 3. DAX
- Data Analysis Expressions
- A programming language that is used throughout Microsoft Power BI for creating calculated columns, measures, and custom tables

## 4. Measures
- A measure is a DAX formula that instructs Power BI to do a **calculation** on data
- Best practice is to store the measure in the table where the data comes from (e.g. right-click and select New Measure)
- Make measure names as long as they need to be to make it clear what they are
- Create a matrix first to get immediate feedback

## 5. Intellisense
- Typing functions into the formula bar triggers the IntelliSense tooltips to pop up

## 6. Filter Context
- Refers to any filtering that is applied to the data model in DAX
- Created by a visual and also by the CALCULATE() function

#### Initial Filter Context
- The initial filter context is the standard filtering coming from a matrix (or any other visual) **before** any possible modifications are applied from DAX formulas using CALCULATE()
- The natural filtering that is applied by a visual, which can come from the following areas: Rows, Columns, Slicers, Filters, & any other visual on the canvas

>Don't confuse the filter context coming from Rows in a matrix with row context.

## 7. Filter Propagation
![IMG_BC1F7353348F-1](https://user-images.githubusercontent.com/19756136/204647399-869e6baf-48d5-43da-8211-862516b15f6c.jpeg)
1. The initial filter context coming from the visual is applied to the underlying table(s) in the data model
2. The filter automatically propagates through the relationship(s) between the tables, flowing **downhill** to the connected tables, from the one side to the many side (from the lookup table to the data table)
3. The connected table is then also filtered just for the calculation of this one **single cell** in the visual
4. After automatic filter propagation has completed, then and only then does the measure get evaluated (e.g. the measure Total Sales = SUM(Sales[ExtendedAmount]))
5. This process is repeated for every single cell in the matrix, including subtotal and grand total

## 8. Data Tables
- aka fact tables or transaction tables
- Typically the largest tables loaded into Power BI
- No limitation on how often similar transactions can occur and be stored in a data table

## 9. Lookup Tables
- aka dimension tables, reference tables, or master data tables
- Tend to be smaller than data tables (with fewer rows) and often wider (more columns)
- Unlike data tables, lookup tables must have a key that uniquely identifies each row

## 10. Schemas
- **Star** schema: data table is located at the center of the star, lookup tables are shown as points on the star
- **Snowflake** schema: Multiple levels of lookup tables; common data structure in traditional transactional databases as it is the most efficient way to store the data

## 11. Why Snowflake Is Not the Best Data Structure in Power BI
- Every relationship comes at a cost (negative performance impacts)
- The structure is confusing to an end user building reports on your database design
- Power BI was built to be very efficient in the way it stores repetitive data in columns, particularly in smaller lookup tables

>Transactional databases and reporting databases are not the same, so don't try to use the table structure from your transactional system in Power BI.

## 12. Advice on Loading Your Own Data
- Keep your data tables long and skinny
- Get rid of extra columns of unnecessary data, particularly if a data table is very wide
- Move repeating attribute columns from a data table into lookup tables
- If you have lookup tables joined to other lookup tables, consider flattening them into a single, wider lookup table

## 13. Row Context
- Refers to the ability of a special iterating function or calculated column to be "aware" of which row it is acting on
- Row context only exists in certain DAX functions: 
	- X-functions
	- Calculated Columns
	- Filter()

#### Think of It This Way
1. The function/calculated column iterates through the table one row at a time
2. It selects the single value (intersection between the row and column)
3. Acts on the single value

>Regular measures can't do this; only functions that have row context and calculated columns

## 14. Avoid Too Many Calculated Columns
- Most common mistake Excel users make: using calculated columns in place of X-functions
- A calculated column is an iterator that iterates over the table in which it is placed and has row context just like SUMX()
- Big problem: calculated columns always evaluate every row and store the answer in the workbook as a value in the column in the table, which **takes up space**
	- Also, the compression applied to calculated columns is reportedly not as good as for imported columns, and the data could be **stored less efficiently**

#### Should Not Use Calculated Columns If...
- You can use a measure instead
- You can bring the data into a table directly from the source data
- You can create the column during data load by using Power Query

>You shouldn't write calculated columns unless you have no other option and you know why you need them.

## 15. The CALCULATE() Function
- The most important and powerful function in DAX
- **Only** function (along with CALCULATETABLE()) that has the ability to modify the filter context coming from your visuals
- Modifies an expression (e.g. a measure or other DAX formula) by applying/removing/modifying filters
- "Reruns" the built-in filter engine in Power BI (the one that makes filters automatically propagate from the lookup tables and flow downhill to the data tables)
- Syntax: `CALCULATE(expression, filter 1, filter 2, filter n...)`
- Can use two types of filters: simple and advanced

## 16. Simple Filters
- A simple (or raw) filter has a column name on the left and a value on the right
	- Customers[Gender] = "F"
	- Products[Color] = "Blue"
- Simple syntax is provided to allow beginners to use Power BI without having to first become DAX experts and is actually converted to a more complex formula under the hood

## 17. Advanced Filters
- Passed in the form of a table containing the values required for the filter
- This table can be either of the following:
	- A physical table
	- A function that returns a table (e.g. ALL(), VALUES(), FILTER())

## 18. Evaluation Context
- One of the hardest topics to understand and master in DAX
- Some DAX functions have filter context; DAX also has row context
- These are the two different types of **evaluation context**

## 19. Row Context Does Not Automatically Create Filter Context
Two very important points:
1. A row context does not automatically create a filter context
2. A row context does not follow relationships

## 20. Context Transition
- It is possible to turn the row context from a calculated column into a filter context through a process called context transition
- Simply **wrap** a calculated column's formula in a CALCULATE() function
	- When you do this, the row context that exists in the calculated column is transformed into an equivalent filter context
- This works anywhere that a row context exists (calculated columns and iterators like FILTER() and SUMX())

>This is the special case where no filters are needed inside CALCULATE() but instead CALCULATE() creates a new filter context from the row context by using context transition

## 21. The Hidden Implicit CALCULATE()
#### Three Calculated Column Examples
1. Total Sales Column 1 = SUM(Sales[ExtendedAmount])
2. Total Sales Column 2 = CALCULATE(SUM(Sales[ExtendedAmount]))
3. Total Sales Column 3 = [Total Sales]

#### Explanation of Each Example
1. With row context but no filter context
2. With a row context which is converted into an equivalent filter context through the process of context transition
3. Equivalent to #2 as the [Total Sales] measure has an implicit CALCULATE()

>*Every measure* has an implicit CALCULATE()

## 22. ALL()
- Removes all current filters from the current filter context
- You can pass either a table or column as the first parameter
- Returns a table (you can wrap COUNTROWS around it to see the number of rows)

#### As Advanced Filter Input
- Most common use of ALL is as an advanced filter input to CALCULATE
- Good for creating measures that are percentages of grand totals

## 23. FILTER()
- Syntax: FILTER(Table, myFilter)
- Most commonly used as an advanced filter inside CALCULATE
	- *Simple* filters in CALCULATE are actually calling FILTER under the hood
- Returns a virtual table that contains zero or more rows from the original table
- You can't put the table returned by FILTER into a matrix, but you can wrap it in other functions to obtain values

#### How Does It Work?
Is an iterator function (just like SUMX):
1. It creates a row context on the specified table and then 
2. iterates through each row to check the filter condition
3. Once the last row has been evaluated, FILTER returns a table that contains just the rows that passed the conditional check

#### Example: Calculating Lifetime Customer Purchases
```DAX
Customers with Sales Greater Than $5,000 = 
	CALCULATE(
		COUNTROWS(Customers),
		FILTER(
			Customers,
			[Total Sales] >= 5000
		)
	)
```

Here's what's happening within FILTER:
1. FILTER creates a row context for the Customers table and goes to the first row, applying the filter to a *single customer*
2. Because of the implicit CALCULATE() within [Total Sales], *context transition* occurs as the row context is converted into an equivalent filter context
3. Because of the context transition, the filter propagates from the Customers table to the Sales table, where the filter is applied to only *sales for this one customer*
4. The measure [Total Sales] is evaluated after the Sales table is filtered for this one customer
5. FILTER condition is then checked (pass, customer stays; fail, customer discarded from final table)
6. Repeat for every customer in the Customers table

## 24. Virtual Table Lineage
- Any virtual table object returned by a table function in DAX always retains a link to the data model fro the life of the evaluation of the measure or calculated column - this is called *lineage*
- Lineage only happens with virtual tables used inside DAX formulas such as measures and calculated columns
- The New Table Button creates a new, physical table stored in the data model which does not retain lineage to the table it came from

## 25. Time Intelligence
- Used to create relative measures

## 26. Rules for Using Inbuilt Time Intelligence Functions
- Must have a calendar table that contains a contiguous range of dates that covers every day in the period you are analyzing
- Every date must exist once and only once
- Only works on a standard calendar (Jan 1 - Dec 31st)

>If you can't meet these rules, you can build your own custom time intelligence functions using FILTER()

## 27. Turning Off Auto Date/Time
- Automatically creates time intelligence-like behavior for every table in your data model that has a date column
- Author recommends disabling this in options -> Current File -> Data Load (uncheck Auto Date/Time)

## 28. SAMEPERIODLASTYEAR()
- Returns a list of dates from the current filter context but time shifted back a year
- Similar functions include PREVIOUSMONTH(), PREVIOUSQUARTER(), and PREVIOUSDAY()

## 29. Changing Financial Year-Ending Dates
- Many of the inbuilt functions allow you to specify a different end-of-year date
- There is no need to specify a year, just day and month
- Example for financial year ending June 30: Total Sales FYTD = TOTALFYTD([Total Sales], 'Calendar'[Date], "30/6")
	- Can also use US date format of 6/30

>Calendar is a reserved word in Power BI. You must add single quotes when referencing a 'Calendar' table within your formulas.

## 30. Writing Your Own Time Intelligence Functions
#### Concept 1: Thinking "Whole of Table" When Thinking About Filter Context
- Think of the whole resulting virtual table when filtering is being applied
- If you include an ID column in your Calendar table (which you should!), you can reference those that remain in your filtered table

#### Concept 2: Knowing How to Use MIN() and MAX()
- Very common to use inside of FILTER()
- You can also use FIRSTDATE() and LASTDATE() if you prefer
- Whenever you use an aggregation function around a column in a DAX formula, it will *always* respect the initial filter context coming from the visual

>Custom time intelligence always uses some form of ALL('Calendar') to remove initial filter context. The FILTER() function therefore iterates through an unfiltered copy of the Calendar table. MIN() and MAX() operate in the initial filter context BEFORE the ALL() function removes it.

## Final Thoughts
- Good introduction/reference to Power BI and DAX
- Will need to read a lot of other books/blogs to learn the CALCULATE() function thoroughly
- Filter propagation and context transition are not an intuitive concepts and need practice to thoroughly assimilate
- File used for exercises in the book can be found [here](https://github.com/chris-delgado/chris-delgado.github.io/blob/main/pbi/SuperchargePowerBI.pbix)
- Source data tables are [here](https://github.com/chris-delgado/chris-delgado.github.io/blob/main/pbi/Adventure%20Works%202005.xlsx)
