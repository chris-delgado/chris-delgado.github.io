[[Monthly Reviews]]

# November 2022
## Highlights
```dataview
TABLE 
	Highlight
FROM [[Daily Note]]
WHERE file.cday >= date(2022-11-01)
AND file.cday <= date(2022-11-30)
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
AND date(End) >= date(2022-11-01)
AND date(End) <= date(2022-11-30)
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
startDate: 2022-11-01
endDate: 2022-11-30
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
startDate: 2022-11-01
endDate: 2022-11-30
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
startDate: 2022-11-01
endDate: 2022-11-30
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
startDate: 2022-11-01
endDate: 2022-11-30
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
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Minimum: {{min()}}\\nMaximum: {{max()}}\\nMedian: {{median()}}\\nAverage: {{average()}}"
\`\`\`
</div><div style='width: 50%; float: left; text-align: right'>\n
\`\`\`tracker
searchType: frontmatter
searchTarget: Weight
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Minimum: {{min()}}\\nMaximum: {{max()}}\\nMedian: {{median()}}\\nAverage: {{average()}}"
\`\`\`
</div>`)
```

```tracker
searchType: frontmatter
searchTarget: Walk
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Total Miles Walked: {{sum()}}"
```
```tracker
searchType: frontmatter
searchTarget: PushUps
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Total Push Ups: {{sum()}}"
```
```tracker
searchType: frontmatter
searchTarget: ChinUps
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Total Chin Ups: {{sum()}}"
```
```tracker
searchType: frontmatter
searchTarget: Protein
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Average Daily Protein (g): {{average()}}"
```
```tracker
searchType: frontmatter
searchTarget: SaturatedFat
startDate: 2022-11-01
endDate: 2022-11-30
summary:
    template: "Average Daily Saturated Fat (g): {{average()}}"
```
