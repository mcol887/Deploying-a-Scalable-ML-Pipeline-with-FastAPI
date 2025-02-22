# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model created by Morgan Cole on 2/21/2025. This is a RandomForestClassifier Model. 
## Intended Use
The intended use of this model is determining someone that makes over $50,000 per yeaar based on the following categories (columns): age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex

## Evaluation Data
Training data is 80% of the original dataset, the remaining 20% is used to evaluate the data. 
## Metrics
Precision: 0.7222 | Recall: 0.6194 | F1: 0.6669 

## Ethical Considerations
There are other factors that may affect an individual's salary, such as job performance. Factors like these can affect an individual's salary - however they can not be measured as they are subjective. 
## Caveats and Recommendations
I reccomend using a more recent census for more accurate results for the current time period. This data is from the 1994 census, whereas using a more current dataset would take into consideration inflation. 