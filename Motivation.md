# Motivation for Toxic Comment Clasification

## Full Text

Online communication is happening at every second all over the globe. The amount of postings and comments grew in the last years to a number one will have a hard time to measure ot imagine in football fields. On Facebook alone, an average of 4.75 billion items are shared by users every day (according to: [this blog](https://blog.wishpond.com/post/115675435109/40-up-to-date-facebook-facts-and-stats)), and this does not imclude comments. With the pandemic being yet another impetus within this development, people's life online makes a big part of their day-to-day communication. Because of its global availability and its independence from time and space, the internet also became one of the main stages for the discussion we - as the human race in total or in subsocieties of it - want to have. 

While the main benefits of the internet can be pinned down to free speech and anonymity, the evolution of the internet shows that these merits are also part of its biggest drawback: toxic trolls who conquer the comment sections to prevent these discussions from evolving due to people leaving these conversations prematurely as a consequence of toxic behaviour of their opposites. At this point, it is the job of content moderators to keep an eye on people's manners in the publich space. Because of the sheer amount of postings and comments every day, this job has become a Sisyphean task. Additionally, one should not forget that there is a human being behind this moderation whose day to day life consists of reviewing cruel, racist, homophobic, sexist and misogynist content. Reports on facebook's content reviewers suffering from PTSB gives us a hint of the effects of this kind of work on the human health (Check out this [video](https://www.youtube.com/watch?v=cHGbWn6iwHw) of a former employee of facebook talking about the effect the work had on his life). As a direct consequence if this, many news platforms disabled discussions for certain topics completely, taking away the potential of fruitful discussions about topics that need to be discussed.

Starting at this dilemma, researchers at Google and Jigsaw created [Perspective API](https://www.perspectiveapi.com): a tool for AI supported content moderation. This tool is the result of a number of kaggle competitions set up to tackle this problem. While the first competition was set up to give a [toxicity rating to comments](https://www.kaggle.com/c/jigsaw-toxic-severity-rating), the follow up aimed at [classifying](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) them according to the origin of toxicity. Further competitions asked for a solution to [counter bias in the models](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification) and to apply the same model to [multilingual purposes](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification). 

The goal of this project is to build a machine learning model that is not only able to detect toxicity in comments but also to classify them according to the origin of their toxicity. The model is supposed to label toxic comments as obscene, severe toxic, insult, identity hate or threat. 


## TLDR-Version

- immense number of comments every day
- toxic trolls who conquer the discussion boards hinder online discussions
- content moderators not being able to moderate all of it anymore leads to disabling of discussions due to high cost
- this is where AI comes in to filter out toxic comments before they can be posted
- reserachers at Google and Jigsaw published Perspective API: a tool for AI supported content moderation
- result of kaggle competitions 
- goal of our model: build a classifier to label comments according to the origin of their toxicity