# Module 1 Final Project - Microsoft Movie Analysis

## Introduction

This Readme lays out the details of Module 1 Final Project for Jake Miller Brooks and Bobby Williams.

## Summary

We were tasked with analyzing the data available in the "Data" folder of this repository, in order to provide guidance for Microsoft's potential entry into the movie business. We sought to answer the following three questions:
- 1) On average, which if any genres are more profitable by either a Return on Investment Percentage, or gross margin?
- 2) What studios or other stakeholders are more profitable within the genres we are seeking to identify?
- 3) Are there different tiers of investment that Microsoft could approach this from? What spend levels appear to indicate the best possibility of showing a profit, and how much should Microsoft expect to spend on a typical project?

## Repository Contents

- Original data are in the Data folder
- Image files of our plots are in the plot_images folder
- A copy of our cleaned data in .pkl format is in the cleaned_data folder, it was saved as pkl due to both size and formatting of one of the columns as list type which is not possible to preserve in csv format.
- Our main technical notebook summarizing our analysis is in the home directory of this repository
- A copy of our slide deck in pdf format is in the presentation folder
- Additional working notebooks used to produce our final product are in additional_notebooks

## Data

The datasets we used from the data folder are:
- tn.movie_budgets
- imdb.title.basics
- imdb.title.crew
- imdb.name.basics
- bom.movie_gross

### Combined Sets
From the above datasets we first combined tn.movie_budgets and imdb.title.basics to combine budget and genre information into one dataframe. This combined dataframe was merged again with bom.movie_gross in order to include studio information as well.

## Data science process steps

DESCRIBE PROCESS HERE

## Results

The heatmap below gives a high level overview of average profitability by genre. Action, Adventure, Animation, Fantasy, and Sci-Fi appear to perform most consistently well over the last 10 years.
![Genre Heatmap]
(https://github.com/jmillerbrooks/mod_1_git_lab/blob/master/plot_images/heatmap_genre.png)



## Future improvement ideas

DESCRIBE FUTURE IMPROVEMENT HERE


### Readme Content

- [ ] Readme includes...
  - [ ] Data science process steps
  - [ ] Future improvement ideas
  - [ ] Repository navigation
  - [ ] Reproduction instructions
  - [ ] Links to presentation and sources
