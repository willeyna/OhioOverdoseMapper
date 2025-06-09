# Tracking the Spatiotemporal Spread of the Ohio Overdose Epidemic with Topological Data Analysis README

## /Data 
* ohio_drugdeaths.csv -- contains county latitude, longitude, and drug induced death information from 2017 until 2024 
* yearly_demographic_data.csv -- contains all county demographic information

## /MapperHTML 
* ohio_spatiotemporal.HTML -- Mapper graph created using county latitude, longitude, and time. No death information is included in the filter function. Used for Figure 3.
* cumulative_deaths.HTML -- Mapper graph created using county latitude, longitude, time, and cumulative death count. Used for Figures 1 and 4.
* normalized_cumulative_deaths.html -- Mapper graph created using county latitude, longitude, time, and population-normalized cumulative death count. Used for Figures 5 and 6.
* demographic_visualization.html -- Mapper graph created by projecting onto time along with all of the demographic features discussed. Used to create Figures 7-11.
* demographic_and_cumulative_deaths.html -- Mapper graph created by projecting onto time, the demographic features, and cumulative deaths. Used to create Figure 12.
* demographic_and_normalized_deaths.html -- Mapper graph created by projecting onto time, the demographic features, and normalized cumulative deaths. Used to create Figure 13.

## MapperPlot.py
Script used for creation of the Mapper plots shown in /MapperHTML from the data files in /Data. 
By changing the lines in the script specifying which features to project onto as well as the input data file one can recreate the provided Mapper plots. 
