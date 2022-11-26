---
layout: post
title: Key Takeaways from Naked Statistics by Charles Wheelan
image: "/posts/NakedStatistics.jpeg"
tags: [Books, Statistics]
---

# Naked Statistics - Key Takeaways
## The First Descriptive Task
- Find some measure of the middle of a set of data (central tendency)

## Standard Deviation
- Measure of how dispersed the data are from their mean
- Allows us to assign a single number to the dispersion around the mean

## Normal Distribution
- Data that are distributed normally are symmetrical around their mean in a bell shape that describes many common phenomena
- The beauty of the normal distribution is that we know exactly what proportion of observations lie within 
	- one standard deviation of the mean (68.2%)
	- two (95.4%)
	- three (99.7%)

## Percentages
- Useful, but also potentially confusing or even deceptive
- Numerator gives the size of the change in absolute terms
- Denominator puts this change into context by comparing it with our starting point
- Always gives the value of some figure relative to something else

### Percentage Points vs. Rates
- Rates are often expressed in percentages
- Rates are levied against some quantity
- Changes in rates can be described in vastly dissimilar ways:
	- The state income tax was increased by 2 percentage points (from 3% to 5%)
	- The state income tax has been raised by 67 percent

## Statistical Index
- A descriptive statistic made up of other descriptive statistics (e.g. NFL passer rating)
- It consolidates lots of complex information into a single number (both a pro and con)
- Any index is highly sensitive to the descriptive statistics that are cobbled together to build it and the weight given to each component

## Precision vs. Accuracy
- Precision reflects the exactitude with which you can express something
- Accuracy is a measure of whether a figure is broadly consistent with the truth
- If an answer is accurate, then more precision is usually better, but no amount of precision can make up for inaccuracy
- Precision can mask inaccuracy by giving us a false sense of certainty, either inadvertently or deliberately

## Unit of Analysis
- The entity being compared or described by statistics
- Example: One politician could use schools as his unit of analysis (60% of our schools are getting worse!) while another could use students (80% of our students had higher test scores!)

## Mean and Median Used for Nefarious Purposes
- The median is not sensitive to outliers, which can be misleading when outliers are highly relevant to your case
	- Example: 30% of patients cured entirely, but only increases median life expectancy by about 2 weeks (the mean life expectancy for people on this drug would look very impressive)
- From the standpoint of accuracy, the median versus mean question revolves around whether the outliers of a distribution distort what is being described, or are an important part of the message

## Correlation
- Measures the degree to which two phenomena are related to one another
- The power of correlation is that we can encapsulate an association between two variables in a single descriptive statistic: the correlation coefficient

### The Correlation Coefficient
Has two attractive characteristics:
1. Is a single number ranging from -1 to 1 (zero meaning that the variables have no meaningful association)
2. Has no units attached to it (can calculate correlation between two variables of different units)

## Bernoulli Trial
- a random experiment with exactly two possible outcomes, "success" and "failure", in which the probability of success is the same every time the experiment is conducted.
- aka binomial trial

## Probability of Independent Events
- The probability of two independent events BOTH happening is the product of their respective probabilities
- The probability of one independent event OR another event happening is the sum of their probabilities

## Expected Value
- The sum of all the different outcomes, each weighted by its probability and payoff

### Example
- Dice game where rolling a number gets you that many dollars
- expected value = 1/6 x (1+2+3+4+5+6) = 21/6 = 3.50
- If the cost to play the game is $3, then you should play the game

### Law of Large Numbers
- As the number of trials increases, the average of the outcomes will get closer and closer to its expected value

## The Monty Hall Problem
- Three doors with a highly desirable prize behind one and goats behind the other two
- After contestant chooses a door, Monty would open one of the two doors that the contestants had not picked, always revealing a goat
- Monty would then ask the contest if they would like to change their pick

### Should They Switch?
- Yes; the contestant has a 1/3 chance of winning if they stick with their initial choice and a 2/3 chance of winning if they switch

### Explanation
- You are effectively exchanging door 1 for doors 2 & 3

![Pasted image 20220508110513](https://user-images.githubusercontent.com/19756136/188918640-6ba4e764-ba1b-47ba-b2c9-238925e8275a.png)

## Longitudinal Study
- Collects information on a large group of subjects at many different points in time, such as once every two years

## Cross-Sectional Data Set
- A collection of data gathered at a single point in time

## The Central Limit Theorem
- The central limit theorems tells us that the sample means will be distributed roughly as a normal distribution around the population mean no matter what the distribution of the underlying population looks like
- The larger the number of samples, the more closely the distribution will approximate the normal distribution
- As a rule of thumb, the sample size must be at least 30 for the central limit theorem to hold true (a larger sample is less likely to be affected by random variation)

## Standard Error
- Measures the dispersion of the sample means
- The standard error is the standard deviation of the sample means
- A large standard error means that the sample means are spread out widely around the population mean

## Hypothesis Testing 
- The starting assumption is the null hypothesis, which is the complement to the alternative hypothesis (if one is true, the other is not)
- Researchers often create a null hypothesis in hopes of rejecting it
- A 5% (.05) significance level is a common threshold used for rejecting the null hypothesis
	- Represents the upper bound for the likelihood of observing some pattern of data if the null hypothesis were true
- Includes two-tailed and one-tailed tests

## p-value
- The specific probability of getting a result at least as extreme as the one you've observed if the null hypothesis is true
- .05, .01, and .1 are all common thresholds

## Type I Error
- If our burden of proof for rejecting the null hypothesis is too low (e.g. .1), we are going to find ourselves periodically rejecting the null hypothesis when in fact it is true
- In other words, it involves WRONGLY rejecting a null hypothesis
- This is also known as a false positive
	- When you go to the doctor to get tested, the null hypothesis is that you don't have a disease
	- If you test positive for a disease but don't really have it, that's a Type I error

## Type II Error
- The higher the threshold for rejecting the null hypothesis, the more likely it is that we will fail to reject it when it should be rejected
- This is also known as a false negative

## Polling
- An inference about the opinions of some population that is based on the views expressed by a sample drawn from that population
- The power of polling stems from the central limit theorem
- An important difference between a poll and other forms of sampling is that the sample statistic we care about is not a mean but a percentage
- A bigger sample makes for a shrinking standard error, which is how large national polls can be very accurate
- Bad results typically stem from a biased sample, bad questions, or both

### Margin of Error
- If we want to be more confident of polling results, we have to be less ambitious about what we are predicting

## Regression Analysis
- Statistical tool that allows us to quantify the relationship between a particular variable and an outcome that we care about while controlling for other factors
- Seeks to find the best fit for a linear relationship between two variables

### Ordinary Least Squares
- OLS fits the line that minimizes the sum of the squared residuals and gives us the best description of a linear relationship between two variables
- The result is the regression equation

#### Regression Equation (y = a + bx)
- y is the dependent variable, because it depends on other factors
- x is the explanatory variable(s) (sometimes called independent or control variable)
- b is known as a regression coefficient (example: the coefficient on height)
- The sign on the regression coefficient tells us the direction of the independent variable's association with the dependent variable
- The size of the regression coefficient tells us how big the observed effect is between the independent and dependent variables

### Multiple Variables
- When we include multiple variables in the regression equation, the analysis gives us an estimate of the linear association between each explanatory variable and the dependent variable while holding other dependent variables constant (or controlling for these factors)
- If it's a yes/no variable, we can use a binary/dummy variable to represent that in the equation

## t-distribution
- A series, or family, of probability density functions that vary according to the size of our sample
- More dispersed than the normal distribution and with fatter tails
- The more data in the sample, the more "degrees of freedom", and the closer the t-distribution gets to converging to the normal distribution

### t-statistic
- The ratio of the observed coefficient to the standard error of the coefficient
- When the t-statistic is sufficiently large, we can reject the null hypothesis at some level of statistical significance
- The fewer degrees of freedom, the fatter the tails of the t-distribution, and the higher the t-statistic will have to be to reject the null hypothesis at some given level of significance

## Program Evaluation
- Process by which we seek to measure the causal effect of some intervention (the treatment)

### Approaches for Isolating a Treatment Effect
- Randomized, controlled experiments
- Natural experiment
- Nonequivalent control
	- Sometimes the best available option for studying treatment effect is to create nonrandomized treatment and control groups
	- The hope is that the two groups are broadly similar even though circumstances have not allowed the statistical luxury of randomizing
- Difference in differences
	- First, examine the before and after data
	- Second, compare that data over the same period to a similar group that did not implement any treatment/program
- Discontinuity analysis
	- Compare the outcomes for some group that barely qualified for an intervention/treatment with the outcomes for a group that just missed the cutoff for eligibility and did not receive the treatment
