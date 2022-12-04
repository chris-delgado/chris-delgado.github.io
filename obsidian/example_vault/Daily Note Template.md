---
Highlight: ""

Reflections:
- ""

Calories: 0
NoJunkFood: 1
Protein: 0
PushUps: 0
ChinUps: 0
SaturatedFat: 0
Sleep: 9
Walk: 0 
Weight: 0
---
| [[Daily Note]] | **PREVIOUS DAY** | [[<%tp.date.yesterday()%>]] | **NEXT DAY** | [[<%tp.date.tomorrow()%>]] |
| -------------- | ---------------- | -------------- | ------------ | -------------- |
# <%tp.date.now()%>
```dataview
TABLE WITHOUT ID
	Highlight
WHERE file = this.file
LIMIT 10
```
```dataview
TABLE WITHOUT ID
	Reflections
WHERE file = this.file
FLATTEN Reflections
LIMIT 50
```
```dataview
TABLE WITHOUT ID
	file.link AS Projects,
	Areas AS Area,
	dateformat(Deadline, "yyyy-MM-dd") AS "Deadline",
	dateformat(file.mday,"yyyy-MM-dd") AS "Last Update"
FROM outgoing([[Projects]])
WHERE date(Start) != null
AND date(Start) <= date(<%tp.date.now()%>)
AND (date(End) = null or date(End) = date(<%tp.date.now()%>))
Sort file.mday
LIMIT 50
```
```dataview
TABLE WITHOUT ID
	file.link as "Notes Created Today",
	file.outlinks[0] AS Parent,
	dateformat(file.ctime, "t") AS Time
WHERE file.cday = date(<%tp.date.now()%>)
AND file.link != [[<%tp.date.now()%>]]
SORT file.ctime DESC
LIMIT 100
```