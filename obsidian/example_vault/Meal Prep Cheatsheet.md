[[Meal Prep]]

# Meal Prep Cheatsheet
```dataview
TABLE WITHOUT ID
	file.name AS Food,
	Ingredients,
	Steps
FROM outgoing([[Meal Prep]])
WHERE Ingredients != null and Steps != null
LIMIT 50
```