Title: The Best and Worst States to Have a Heart Attack
Tags: R, data analysis, Coursera
Slug: the-best-and-worst-states-to-have-a-heart-attack
Author: Brian Aaron
Summary: Using Medicare.gov data, the author analyzes the best and worst states in the country to have a heart or experience heart failure.


I wanted to use the data to see which states had on average the lowest mortality scores, the fewest people died, and which states had the highest mortality scores, 
the most people died. I was also curious if 'law of small numbers' might be at work. In small samples, extreme things can happen and their cause is randomness not 
something exceptional about the group. In other words, will extremely high scoring states just be small states with few hospitals (because if they had more hospitals 
then the additional hospitals would have just brought them closer to average).

The data for this analysis come from the csv file titled, 'Out Come of Care Measures 9-29-2014.' I will use the 30-day death (mortality) measures for the analysis.
On the [Medicare.gov/30-day unplanned readmission and death measures page](http://www.medicare.gov/hospitalcompare/data/30-day-measures.html),
the 30-day death (mortality) measures are defined as follows:

>The 30-day death (mortality) measures are estimates of deaths from any cause within 30 days of a hospital admission, for patients hospitalized with one of 
>several primary diagnoses. Deaths can be counted in the measures regardless of whether the patient dies while still in the hospital or after discharge. 
>CMS chose to measure death within 30 days instead of inpatient deaths to use a more consistent measurement time window because length of hospital stay 
>varies across patients and hospitals. Also, mortality over longer time periods (such as 90 days) may have less to do with the care received in the hospital 
>and more to do with other complicating illnesses, patients’ own behavior, or care provided to patients after hospital discharge. Hospital Compare reports 
>on the following 30-day mortality measures:
>
>30-day death rate for heart attack (acute myocardial infarction [AMI]) patients
>30-day death rate for heart failure (HF) patients
>30-day death rate for pneumonia patients

In other words, did you die 30 days after receiving care?

One would think though that if you had a heart attack, maybe you were just old or unhealthy, so you would die anyway. The data has been adjusted for this. 
From the [Medicare.gov/30-day unplanned readmission and death measures page](http://www.medicare.gov/hospitalcompare/data/30-day-measures.html), the following
information is given for rish adjustment:

>To make comparison of hospital performance fair and level the playing field, the 30-day unplanned readmission and (death) mortality measures adjust for patient 
>characteristics that may make death or unplanned readmission more likely, even if the hospital provided higher quality of care. These characteristics include 
>the patient’s age, past medical history, and other diseases or conditions (comorbidities) the patient had when they were admitted that are known to increase 
>the patient’s risk of dying or of having an unplanned readmission.

Okay, enough background. Let's get to the analysis. Here is the psuedocode for my algorithm:

```
        #Load the data into the data variable.
        
        #Coerce factors as neccesary to ensure states are characters and the 30-day stats are numeric.
        
        #Remove the hospitals that have NA for 30-day mortality rate for heart attack.
        
        #Split data by state, take the mean of the 30-day mortality data, and return averages to the averages vector
        
        #Place state abbreviations in states vector.
        
        #Count the hospitals per state and return it to the number_hosptals vector.
        
        #Combine the vectors into a dataframe.

        #Sort the dataframe by the average 30 day mortality scores
        
        #Print out the first and last five states in the dataframe.
```

Here are the results:
```
   States 30-day mortality heart attack Number of Hospitals
28     MT                      14.07500                   8
21     MA                      14.17414                  58
9      DE                      14.31667                   6
6      CO                      14.48182                  33
42     RI                      14.48182                  11
47     UT                      14.55625                  16

   States 30-day mortality heart attack Number of Hospitals
51     WA                      15.84545                  44
27     MS                      15.86176                  34
54     WY                      15.90000                   3
3      AR                      16.09375                  32
12     GU                      16.10000                   1
49     VI                      16.30000                   1
```

Regarding the best states, Massachusetts is the place to be. It had a very low score with a large number of hospitals. It would be hard to dispute that its score
is not representative. Delaware and Montana might have just gotten lucky.

As to the bottom five, I must admit that I expected to see Mississippi in the data. There also seem a substantial number of hospitals for Washington and Arkansas to 
truly know that neither of those places is a good place to have heart attack. Wyoming, Guam, and the Virgin Islands might have just had unlucky years.

On the whole, I was somewhat surprised at just how tight the range was for the data. 



