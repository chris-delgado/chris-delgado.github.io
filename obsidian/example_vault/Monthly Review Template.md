[[Monthly Reviews]]

# <%moment().subtract(1, 'months').format('MMMM YYYY')%>
## Highlights
```dataview
TABLE 
	Highlight
FROM [[Daily Note]]
WHERE file.cday >= date(<%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>)
AND file.cday <= date(<%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>)
AND Highlight != null
SORT file ASC
LIMIT 50
```

## Completed Projects
```dataview
TABLE WITHOUT ID
	file.link AS Project,
	Areas AS Area,
	Goal,
	Outcome,
	Deliverable
FROM outgoing([[Projects]])
WHERE Status = "Complete"
AND date(End) >= date(<%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>)
AND date(End) <= date(<%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>)
SORT End ASC
LIMIT 100
```

## Health
```dataviewjs
let current = dv.current()

dv.paragraph(`<div> \
<div style='width: 50%; float: left;'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: NoJunkFood
datasetName: No Junk Food
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
month:
	color: tomato
	headerMonthColor: orange
	todayRingColor: tomato
\`\`\`
</div><div style='width: 50%; float: left;'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: Sleep
datasetName: Well Rested
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
month:
	color: lightblue
	headerMonthColor: blue
	todayRingColor: lightblue
\`\`\`
</div>`)
```

```dataviewjs
let dayOfMonth = moment().subtract(1, 'months').startOf('month')
let daysInMonth = dayOfMonth.daysInMonth()

let dateString = ''
for(var i = 0; i < daysInMonth; i++) {
	dateString += '"' + dayOfMonth.format('YYYY-MM-DD') + '" or '
	dayOfMonth.add(1, 'days')
}
dateString = dateString.slice(0, -4);
const pages = dv.pages(dateString)
dv.paragraph(`\`\`\`chart  
	type: line
	labels: ${pages.file.name} 
	series:
	- {title: Weight, data: ${pages.Weight}} 
\`\`\``)  
```

```dataviewjs
let current = dv.current()

dv.paragraph(`<div> \
<div style='width: 50%; float: left;'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: Calories
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
fixedScale: .75
line:
    title: Calories
    yAxisLabel: Calories
    lineColor: tomato
    xAxisLabel: ""
\`\`\`
</div><div style='width: 50%; float: left;'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: Weight
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
fixedScale: .75
line:
    title: Weight
    xAxisLabel: ""
    yAxisLabel: lbs
    lineColor: tomato
\`\`\`
</div>`)
```

```dataviewjs
let current = dv.current()

dv.paragraph(`<div> \
<div style='width: 50%; float: left; text-align: right'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: Calories
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Minimum: {{min()}}\\nMaximum: {{max()}}\\nMedian: {{median()}}\\nAverage: {{average()}}"
\`\`\`
</div><div style='width: 50%; float: left; text-align: right'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: Weight
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Minimum: {{min()}}\\nMaximum: {{max()}}\\nMedian: {{median()}}\\nAverage: {{average()}}"
\`\`\`
</div>`)
```

```tracker
searchType: frontmatter
searchTarget: Walk
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Total Miles Walked: {{sum()}}"
```
```tracker
searchType: frontmatter
searchTarget: PushUps
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Total Push Ups: {{sum()}}"
```
```tracker
searchType: frontmatter
searchTarget: ChinUps
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Total Chin Ups: {{sum()}}"
```
```tracker
searchType: frontmatter
searchTarget: Protein
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Average Daily Protein (g): {{average()}}"
```
```tracker
searchType: frontmatter
searchTarget: SaturatedFat
startDate: <%moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')%>
endDate: <%moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')%>
summary:
    template: "Average Daily Saturated Fat (g): {{average()}}"
```
