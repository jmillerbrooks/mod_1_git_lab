# Module 1 Final Project - Microsoft Movie Analysis

## Introduction

This Readme lays out the details of Module 1 Final Project for Jake Miller Brooks and Bobby Williams.

## Summary

We were tasked with analyzing the data available in the "Data" folder of this repository, in order to provide guidance for Microsoft's potential entry into the movie business. We sought to answer the following three questions:
1) On average, which if any genres are more profitable by either a Return on Investment Percentage, or gross margin?
2) What studios or other stakeholders are more profitable within the genres we are seeking to identify?
3) What spend levels indicate the best possibility of showing a profit, and how much should Microsoft expect to spend on a typical project?

## Repository Contents

- Original data are in the <a href="https://github.com/jmillerbrooks/mod_1_git_lab/Data">Data</a> folder
- Image files of our plots are in the <a href="https://github.com/jmillerbrooks/mod_1_git_lab/plot_images">plot_images</a> folder
- A copy of our cleaned data in .pkl format is in the <a href="https://github.com/jmillerbrooks/mod_1_git_lab/cleaned_data">cleaned_data</a> folder, it was saved as pkl due to both size and formatting of one of the columns as list type which is not possible to preserve in csv format.
- Our main technical notebook summarizing our analysis is in the home directory of this repository
- A copy of our slide deck in pdf format is in the main folder of this repository
- Additional working notebooks used to produce our final product are in <a href="https://github.com/jmillerbrooks/mod_1_git_lab/additional_notebooks/">additional_notebooks</a>

## Data

The datasets we used from the data folder are:
- tn.movie_budgets
- imdb.title.basics
- bom.movie_gross

### Combined Sets
From the above datasets we first combined tn.movie_budgets and imdb.title.basics to combine budget and genre information into one dataframe. This combined dataframe was merged again with bom.movie_gross in order to include studio information as well.

## Data science process steps

We first took a few steps to clean our data. Many entries present in the tn movie budgets set are not present in imdb, we used an inner join to drop these entries.  Additionally, we had missing values for runtime minutes, but did not use this variable in our analysis, so left these entries in place. You can find our cleaning work in the documents labeled 'Joined_EDA_with_ratios.ipynb' and 'data_prep' in <a href="https://github.com/jmillerbrooks/mod_1_git_lab/additional_notebooks/">this repo.</a> Our main changes were changing dollar values represented as strings to numeric, creating a profit column from budget and gross, creating an ROI column, and extracting year from release_date.

We next took a look at distributions of genre, profit, and budget, and created visualizations to present our findings. All of our visualizations are in the technical notebook in the main folder of this repository, and you can find a summary of our results in the visualizations included in the Results section below.

## Results

The heatmap below gives a high level overview of average profitability by genre. Action, Adventure, Animation, Fantasy, and Sci-Fi appear to perform most consistently well over the last 10 years.
![Genre Heatmap](https://github.com/jmillerbrooks/mod_1_git_lab/blob/master/plot_images/heatmap_genre.png)

The most profitable studios in each of the top five genres we identified are shown below.
![Genre Studio Bar Chart Comparison](https://github.com/jmillerbrooks/mod_1_git_lab/blob/master/plot_images/bar_chart_top_fives_studios.png)

The distribution of production budgets is found below.
![Budgets for Top Five Genre Films Violinplot](https://github.com/jmillerbrooks/mod_1_git_lab/blob/master/plot_images/top_five_genres_budget_violinplot.png)

The ROI plotted against production budget, with color corresponding to genre, and worldwide profit mapped to size. Green horizontal line indicates break-even point, and blue vertical line indicates the recommended spending floor.
![Budget vs. ROI bubble plot](https://github.com/jmillerbrooks/mod_1_git_lab/blob/master/plot_images/bad_bubble.png)

## Future improvement ideas

- Determine which studios have the highest ROI vs Production Budget

- Understand the effects that the Directors, Writers, and Cast have on ROI

- Obtain data from additional resources to ensure accuracy and to provide more insightful analysis




