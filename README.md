Project
Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:

# Women representaion in the Medias

## Abstract
During the last 5 years, a lot of feminist movements have emerged, like "PayeTonEPFL" on the campus. This gave us the will to dig deeper into the subject to see if it is general to all fields or specific to science.
 These movements highlighted the difference in representation between genders, especially in the medias. They claimed there were a difference between the occurrence of women  and men in the articles, on TV...
 We want to study the evolution of the problem through time, type of newspaper, ages, countries (newspaper origin) and a selection of specific subjects covered, like economics, finance, science, politics or people, news, publicity... 
 We want to see the evolution of mentalities "before" and "after" those movements, by comparing the partition of speak between gender, and see how women are represented before and after. We want to compare it with the men representation evolution through all these years and how they speak about women.
 

## Research questions
Are women and men equally represented in the medias? And if it so, are they also equally quoted in all fields? Can we observe changes between 2015 and 2020, because of movements such as #metoo? Who quotes women and who quotes men?


## Additional datasets
We used the parquet to improve our dataset, to increase the information we have about the speaker and we get the general field of activity to group their occupation. We also search for the name and the gender of the author of the article. Moreover, to see where we could have emergence of gates about sexism, we search for the dates of the feminism movements. Finally, we obtain the general topic of the article. 

## Methods
First, we will compare the proportion of women and men quoted per year. Then we will observe, using the date of the feminist events, whether it has an impact of the portion of women and men quoted or not and what are the subject they cover. We have then to group the different quotation by the topic they cover using the article they came from. Can can use for that the library newspaper to retrieve the text of the article and then LDA to find the topic. For example, when the topic is about sexism, what is the gender more frequent for the speaker of the quotation and the author of the article. We will also retrieve the quotes that spoke of these event and how they represented them though keywords like #metoo, Weinstein, Polanski. We will find the context of the words found and also of the quotation itself through the article. We will also find the partition of the speaker through their age between men and women. We will group the speaker by gender and by age by making intervals and then compare the percentage of presence of the different age group.  We will then try to find how women are represented through the quotes and on which basis they are badly represented, if they are seen negatively. For We will find the words that are the most associated with words like women using deep learning ? We will also partition the representation of the women and men according to their occupation. 

## Timeline
We need to group the topic of the article (and thus of the quotes) and the occupation of the speaker more generally to simplify the comparison between men and women. -> Need to specify this

## Useful dates : 
 October, 15 2017 : Malyssa Milano with #metoo -> Weinstein in US -> find keywords #metoo, Weinstein
 November 2017 in France #balancetonporc
 February 28 2017 for the Césars : Polansky awarded for best movie whereas he is accused of raping a girl -> keywords Polansky, Césars
 May, 22 2018 : Asia Argento at Cannes against Harvey Weinstein
 mots clé : harcèlement, sexism, rape, discrimination -> taboo ?
 
