# Women representation in the Media

[Datastory](link)

## Abstract
Discriminations against women have been the burning subject for the last 3 to 5 years. Raping scandals like the Weinstein gate in 2017, questions about the salary differences lifted by famous Hollywoodien actress Jennifer Lawrence in 2016, the debate about the disappearance of women that are more than 40 in the movies, and the #MeToo scandal paved the way for changes in our society about the women status. In 2019, in Switzerland, the first feminist strike in 40 years took place. They asked for salary equality, the right to be a mother and to work at the same time, they denounced marital violence (according to amnesty international, in Switzerland, a woman dies under the blows of their companion every two weeks) and want a new definition of rape that will protect the women more. Moreover, last year, sexism is brought to light on the EPFL campus by the #PayeTonEPFL group where thousands of people, and in majority women, testify about a time where they felt discriminated against. The number of testimony about sexual harassment, raping, and discrimination was appalling. These scandals motivated us to dig deeper into the subject of sexism in the media.


## Research questions
We studied the evolution of the problem through time, with different criteria: raw numbers, speaker age, occupation fields and sentiment of the quote context. Furthermore, we want to see the evolution of mentalities "before" and "after" those movements, by studying how women are represented before and after. To conclude, the questions we want to find answers to are: are women and men equally represented in the media? If it is so, are they also equally quoted in all occupation fields? Can we observe changes between 2015 and 2020, because of movements such as #metoo? Are women and men quoted more in a positive, neutral or negative way ?


## Additional datasets
We used the provided speaker_attributes.parquet file to improve our dataset, to increase the information we have about the speaker. We also grouped the different occupations by categories. To this end, we parsed the wiki dumps to extract the categories of the occupations. Moreover, we used the article-centric version of the quotebank dataset to get the (text) context of the quotes. Additionally, to see where we could have the emergence of gates about sexism, we search for the dates of the feminist movements.

## Methods
•	First, we compared the proportion of women and men quoted per year.

•	Using the date of the feminist events, we observed whether it has an impact on the portion of women and men quoted or not.

•	We also found the repartition of the speakers according to their age for the two genders. We will group the speaker by gender and by age by making intervals and then compare the percentage of presence of the different age groups.

•	We used [VADER](https://github.com/cjhutto/vaderSentiment) to do the sentiment analysis of the context of the quotes.

•	Occupation categories extracted using the “subclass of” attribute of the occupations present in our dataset.


## Timeline
1.	Determine occupation categories
2.	Sentiment analysis
3.	Starting of the statistic analysis
4.	Plots of our results
5.	Creation of the website

## Contributions
•	Odile:
•	Pablo:
•	Prunelle:
•	Roxane:
