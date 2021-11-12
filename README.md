# Women representaion in the Medias

## Abstract
Discriminations against women have been the burning subject for the last 3 to 5 years. Raping scandals like the Weistein gate in 2017, questions about the salary differences lifted by famous Hollywoodien actricess Jennifer Lawrence in 2016, debate about the disappearance of women that are more than 40 in the movies, and the #MeToo scandal paved the way for changes in our society about the women status. In 2019, in Switzerland, the first feminist strike in 40 years took place. They asked for salary equallity, the right to be a mother and to work at the same time, they denonced the marital violences (according to amnesty international, in Switzerland, a women die under the blows of their compagnon  every two weeks) and want a new definition of rape that will protect the women more. 
Moreover, last year, the sexism is brought to light on the EPFL campus by the #PayeTonEPFL group where thousand of people, and in majority women, testify about time where they felt discriminated. The number of testimony about sexual harassement, raping, and discrimination was appailing. 
These scandals motivated us to dig deaper into the subject of sexism into the medias. 


## Research questions
We want to study the evolution of the problem through time, studying different criterias: type of newspaper, ages, and a selection of specific subjects covered like economics, finance, science, politics or people, news... 
Furthermore, we want to see the evolution of mentalities "before" and "after" those movements, by studying how women are represented before and after. Is it more a representation based on how they look or a representation based on their speech. 
Finally, one of the aspect we want to study is who is speaking about women. Do women journalist quote more women or is it the men? 
To conclude, the questions we want to find answers to are:
Are women and men equally represented in the medias? And if it so, are they also equally quoted in all fields? Can we observe changes between 2015 and 2020, because of movements such as #metoo? Who quotes women and who quotes men?


## Additional datasets
We used the parquet to improve our dataset, to increase the information we have about the speaker and we get the general field of activity to group their occupation. We also search for the name and the gender of the author of the article. To determine the gender, we use an additionnal dataset that we found on the UC Irvine Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Gender+by+Name#) containing almost 150k names with their associated gender. Moreover, to see where we could have emergence of gates about sexism, we search for the dates of the feminism movements. Finally, we obtain the general topic of the article. 

## Methods
- First, we will compare the proportion of women and men quoted per year. 
- Then we will observe, using the date of the feminist events, whether it has an impact of the portion of women and men quoted or not and what are the subject they cover. We have then to group the different quotation by the topic they cover using the article they came from. We can use for that the library newspaper3k to retrieve the text of the article and then LDA to find the topic. For example, when the topic is about sexism, what is the gender more frequent for the speaker of the quotation and the author of the article. 
- To determine the gender of the author, we use a naive Bayes classifier from NLTK that we trained with the additional dataset mentioned above. The approach for finding the author and his/her gender are not completely erro-free as some urls are invalid or restricted, some of the extracted names are not real names, and the classifier isn't optimized, but it allows us to process to large amount of data that we have. 
- We will also retrieve the quotes about these event through keywords like #metoo, Weinstein, Polanski. We will find the context of the words found and also of the quotation itself through the article. 
- We will also find the partition of the speaker through their age between men and women. We will group the speaker by gender and by age by making intervals and then compare the percentage of presence of the different age group.  
- We will finally try to find how women are represented through the quotes and on which basis they are badly represented, if they are seen negatively. 

## Timeline
1) Find the topic of each articles
2) Group the occupations under a more specific label
3) Starting of the statistic analysis
4) Plots of our results
5) Creation of the website

