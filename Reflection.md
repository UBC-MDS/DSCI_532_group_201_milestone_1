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
- Issue #8: TA comments:
  - Rewrote the README.md description
  - Paragraph outlining major features and interactivity added.
  - Modified team contract as per suggestion
  - Wrote specific research question in point form


## New Updates After Milestone 2:

###  High-Level summary of changes made (priority ordering from high to low):

Overall strategy:
  - We in order to spend the limited number of hours before the clock ticks 18:00 on Saturday, we decided that it was best to implement changes that were most obvious visually first. We want to first focus on implementing visual changes since they require the least time and will produce the best results for the reader. We will save technical changes for later since they require a lot of time and our ADHD readers might not even see them.

- Fix font size (fixed over multiple commits, please look into commit history if you're interested):
  - Justification: This is the highest because the old font was not readable and also takes the least time to do.

- Fix description (fixed over multiple commits, please look into commit history if you're interested):
  - Justification: We realized that people don't know what is going on in our app, so we added the description to help what each plot does.

- Changed axis for bottom plot to log axis (fixed over multiple commits, please look into commit history if you're interested):
  - Justification: We wanted to bring more meaning to the axis of the plot. The old one was confusing since no one thinks in a log numbers. So we converted the numbers back to decimal while keeping the log scale.

- Added data source and contributing authors (fixed over multiple commits, please look into commit history if you're interested):
  - Justification: We realized that it was important for the reader to know where the data is coming from, so we added the data source. We also realized that it was important for the reader to know who made this glorious app, so we all added our names to the bottom of this page. This is especially important with the high traffic that this app is going to receive.

- Updated plot titles (fixed over multiple commits, please look into commit history if you're interested):
  - Justification: We realized that although the existing titles were OK, we wanted even BETTER titles. We brainstormed for hours of better titles that will spark divine intuition upon the reader. Take a look for yourself.

- Issue [#31](https://github.com/UBC-MDS/DSCI_532_group_201_natural_disasters/issues/31): Summary of peer feedbacks
  - Reflecting on a few comments regarding possible implementations to the map and associated line graph
  - (2) Log-scaled y-axis instead of log-scaling the data which is harder to interpret for users
  - (3) Colour legend for the map did not seem necessary so was taken out
  - (4) The '_' could not be removed as it's a default when using geo-pandas dataframe in altair
  - (8) Font sizes for x,y-axis titles and main titles changed and tick marks for the years rotated for better readability 


OUR WISH LIST:
- If we had ALL the time in the world, there are (in no specific order):
  - Adding a colourful but yet not distracting background to the app, this might help to make our app look more visually pleasing. 
- Find a way to set a default year and country for our app.
- Rename the slider label
- Use a different world map with outlines for countries, this makes the app look prettier.


High-level summary of the feedback:
- Overall impression: People were ecstatic when they saw our app, who doesn't want to see the impact of earthquakes on countries right?
- Issues brought up: most of the issues brought up were regarding visuals. A lot of them were regarding the same thing. Some issues were technical, but most were regarding the scale of the bottom chart.

Reflection on the usefulness of the feedback you received:
- Usability of the app: My peers used the app like it was intended. Keeping it simple worked in our favour. 
- The things we heard were similar across reviewers. The theme is regarding better visuals.
- Things in our Wishlist were things that we could not change because we did not have enough time. However some are because the Altair package is straight garbage, I mean, even the instructors don't use it for making plots in their lectures. I wonder why.
- By being a 'fly-on-the-wall' I was able to see the psychological strain on the people I was paired with. I was able to learn what the expression of a person who is forced to understand something that they have no innate desire to know looks like. Useful? Just about as useful as writing this reflection document.
- The reflections did yield a better app. That's for sure. Did we have to go through the pain in order to achieve it? Probably not.
