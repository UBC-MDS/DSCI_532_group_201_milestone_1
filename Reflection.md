# Reflections

## Areas where our app does well:
- The colors used is very good. It is color-blind people friendly.
- Font size is good. It is of readable size.
- Axis labels are well choosen, they are very representative of what is being plotted.
- Line width is very good, can see from a distance.
- Plot sizes are good, they take up the majority of the screen.
- Plots are simple and to the point, answers the research question very directly.

## Limitations of our app:
- Some countries in the world map plot have missing data, they appear as blank. This makes the overall plot kind of confusing.
- Only earthquakes analyzed, it is not descriptive of all natural disasters in the world. 
- Log scale of bottom left changes with the year. This makes it hard to compare the severity of earthquakes between countries using color. Since the same color can mean two different numbers.
- On this dashboard we focuses on visualizing impacts of earthquakes rather than providing a comprehensive view of all natural disasters due to data limitation. If we had enough country-level data, we could have created a more informative dashboard on which users are able to navigate to a certain disaster of interest.
- If time permitted, we could have included more detailed information on the dashboard, for example about some significant events, to provide users more context around this natural disaster topic as opposed to just presenting the graphs.

  
## Future Improvements and Additions:
- Can add data about other disasters, and see if differnt types of natural diasters are correlated to each other.
- Upon selecting a type of natural disaster, the plot on the top right would change accordingly to reflect that disaster type.
- Can apply LOESS (locally estimated scatterplot smoothing) or LOWESS (locally weighted scatterplot smoothing) to help plot the trend of a type of diaster over time.
- Change the log scale of the bottom left graph to be fixed.
- Can add outlines to every country, this resolves concern of countries with no data.

## How Issues were addressed:
- Issue #1: Work Flow
  - sgauravm proposed workflow for this project
  - Everyone agreed
  - Issue resolved
- Issue #2: World Map and Associated Line Chart
  - jasmineqyj posted what she has done
  - singh-karanpal asked: "If it is possible can we make one country selected by default?"
  - jasmineqyj tried to resolve issue, but Altair package was bugged and issue persisted.
  - jasmineqyj gave up.
  - Issue resolved
- Issue #3: Adding plots to app.py
  - singh-karanpal posted the Dash application python file
  - jasmineqyj and singh-karanpal conversed about the formatting for the app
  - Issue resolved
- Issue #4: Death rate at country level is going beyond 1(needs to be less than 1)
  - sgauravm posted issue
  - Issue resolved
