# Natural Disasters And Their Impact Across The World
<br>

Suppose, Bob is working for an international humanitarian organization. He is trying to see where to allocate funds for earthquake diaster relief. He wants to explore historical data of how earthquakes affected different countries. This helps him to decide which countries are most effected by earthquakes every year. While using our Dash app, he noticed that in terms of absolute deaths per year due to earthquakes, China and India appeared to be highest every single year. However, while exploring the percentage that eqarthquakes contribute to the annual death rate, he discovered that Haiti was the highest due to the small population of the country. He also discovered that earthquakes have had an increasing impact on the country in recent years. From this data, Bob was able to make the informed decision that it is best to provide monetary support to Haiti instead. Due to the insightfulness of this Dash application, Bob nominated it to be the "App of the Year". Many people started using this app to grow insight of how earthquakes effect different regions in the world. The app ends up getting improved and wins a Nobel Prize. Please read our full proposal [here](https://github.com/UBC-MDS/DSCI_532_group_201_milestone_1/blob/master/proposal.md).

## Sketch
<html>
  <img src = "images/sketch_v1.png" />
<html>

## Natural Disaster Dash App
[Here]() is the link to the deployed app on Heroku.

### Functionality of the Dash App
The world map and associated line chart section provides impact of earthquake events at the global level from 1990 to 2017. When a year is selected by dragging the slider bar, log death rates for all countries are encoded on the map through a color scale where darker colours represent more severe events in that particular year. Death rate is calculated as annual number of deaths caused by earthquake divided by total number of deaths and log scale is used to properly display all levels of severity. A mouseover interaction is added to the world map so that users have the option to view the actual number of deaths instead of a relative death rate. When users click on a country of interest, the line graph should show the historical trend of death rates for that country. Users can take a look at the logged death rate for a year by hovering the mouse. By default, no country should be selected when there's no click seletion.