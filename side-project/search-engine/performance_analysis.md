# Task 3a. Performance analysis

---

## Description

The search engine is good if what the user wants to search appears in the search result and also not to include a lot of "irrelevant" results. At the same time you want the search to return the result quickly. For the final task, You are asked to evaluate and / or compare the performance of different searching strategies in terms of the search accuracy and/or time cost. Possible analyses are:
* If users always provide the exact title when searching for a show, what is the difference in the actual retrieval time between the search method from task 2 and the "naive" search method we had in problem set 9? And what is the average number of "unwanted" shows in the search result when using the search method from task 2?
* Do a simple experiment and see how the number of shows to return related to the number of terms provided by the user
* Use the terms related to a show from other sources (see below for more details) to search and see how likely we are still able to get the right shows

You are not restricted to do the analyses listed above and feel free to do any other analysis. You may want to use this task as an opportunity to show your `Pandas`/`Numpy` skills.

---

## Use show description from other sources in the second simulation

If you use terms from other sources for the analysis, it serves as a good place for you to demonstrate your proficiency on `Pandas`/`Numpy`, as you will need to merge different datasets together. You can google as much as you want if you are doing this analysis.

In terms of getting terms related to the show, one possible source is to use the show description from the IMDb data available [here](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset). Please only use the rows that are _useful_. For example, not all the shows in the IMBd dataset are in the Netflix data. The show with the same name in the IMDb dataset does not necessarily correspond to the show with the same name in the Netflix dataset. Also, sometimes both datasets may have exactly the same description.

---

## Things to show in the report

* Explain what analysis you want to do and show your analysis
* Display and interpret the results
* Based on the results, suggest some possible improvements for the search engine
