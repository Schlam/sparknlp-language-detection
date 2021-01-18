# Language Detection with SparkNLP

Two notebooks are contained here. 

**The first** shows an end-to-end cloud ETL pipeline on AWS
(from S3 to RDS).


**The second** shows how to predict the language
of unlabeled text data using a pretrained model from
[JohnSnowNLP](https://github.com/JohnSnowLabs/spark-nlp).
I belive this is a BERT model trained in a language-agnostic
on various NLI tasks, and later fine-tuned for language prediction.
*See the **ideas** section for ideas for the AI/NLP aspect of this project.*


**The third** (currently unfinished) part provides an
in-depth analysis of Airbnb data considering this new
"language" feature. If you can reasonably associate language
with a certian world region, the you could hopefully find answers like:

- Are international consumers a significant part of the usership in
certain cities?

- Are certain listings better at attracting people whose primary
language is not english?

- Are there patterns in sentiment across diffent languages/world regions?

This could power a number of design aspects at the platform level:

- Rank listings show to a visiting user according to their primary language
- Find listings that have extremely negative sentiment reviews
and rank them lower

Finally, this data can also be used by investors that seek to use Airbnb
as an alternative flow of income by informing certain questions:

- Are there differences in spending habits for international users?
- Are there ways to name/describe your listing that make them appeal
to a wider audience?

## Hardship

Apparently, the sofware versions that play well
with postgresql are not the same versions that
play well with `sparknlp`. Combining the NLP pipeline with the
visualization could be a way to avoid having to load language results
back into postgres. However, that would be more of a patch than a fix, and
would make the language data unretrievable.

### Ideas

Use [LaBSE](https://ai.googleblog.com/2020/08/language-agnostic-bert-sentence.html) to generate more
powerful analytics on the text data.
