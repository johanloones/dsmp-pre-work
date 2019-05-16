# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
#Load dataset using pandas read_csv api in variable df
df=pd.read_csv(path)

#Calculate the probability p(A)for the event that fico credit score is greater than 700. and store it in variable 'p_a'.
p_a=len(df[df['fico']>700])/len(df)

#Calculate the probability p(B) for the event that purpose == 'debt_consolation' and store it in variable 'p_b'.
p_b=len(df[df['purpose'] == 'debt_consolidation'])/len(df)

#Calculate the purpose == 'debt_consolidation' and store it in dataframe df1.
df1=df[df['purpose'] == 'debt_consolidation']

#Calculate the probablity p(B|A) for the event purpose == 'debt_consolidation' given 'fico' credit score is greater than 700 
#and store it in variable p_a_b.
p_a_b=len(df1[(df1['purpose'] == 'debt_consolidation') & df1['fico']>700])/len(df1)

#formula to check the independency P(A|B) == P(A)
#check the independency store it in variable result.
result=(p_a_b==p_b)

#Print result
print(result)

# code ends here


# --------------
# code starts here
#Calculate the probability p(A) for the event that paid.back.loan == Yes and store it in variable called prob_lp.
prob_lp=len(df[df['paid.back.loan']== 'Yes'])/len(df)

#Calculate the probability p(B) for the event that credit.policy == Yes and store it in variable prob_cs.
prob_cs=len(df[df['credit.policy']== 'Yes'])/len(df)

#Calculate ['paid.back.loan'] == 'Yes' and store it in variable new_df
new_df=df[df['paid.back.loan']== 'Yes']

#Calculate the probablityp(B|A) for the event paid.back.loan == 'Yes' given credit.policy == 'Yes' and store it in variable prob_pd_cs
prob_pd_cs=len(new_df[(new_df['paid.back.loan']== 'Yes') & (new_df['credit.policy']== 'Yes')])/len(new_df)

#Calculate the conditional probability where the formala is given below:
#P(A∣B)= P(B∣A).P(A)/P(B)
#Store the result of the event P(A|B) it in variable bayes
bayes=(prob_pd_cs*prob_lp)/prob_cs

#Print the bayes
print(prob_lp,prob_cs,prob_pd_cs,bayes)




# code ends here


# --------------
# code starts here
#Visualize the bar plot for the feature purpose.
print(df['purpose'].value_counts().plot(kind='bar'))
#Calculate the paid.back.loan == No and the store the result in dataframe df1
df1=df[df['paid.back.loan'] == 'No']

#Visualize the bar plot for the feature purpose where paid.back.loan == No
print(df1['purpose'].value_counts().plot(kind='bar'))


# code ends here


# --------------
# code starts here
#Calculte the median for installment and store it in variable inst_median.
inst_median=df['installment'].median()

#Calculate the mean for installmentand store it in variable inst_mean
inst_mean=df['installment'].mean()

#plot the histogram for installment
print(df['installment'].plot(kind='hist'))

#plot the histogram for log anual income
df['log.annual.inc'].plot(kind='hist')

# code ends here


