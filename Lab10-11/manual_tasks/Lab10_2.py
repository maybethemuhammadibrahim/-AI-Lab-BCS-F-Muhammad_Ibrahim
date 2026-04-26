import pandas as pd
from io import StringIO
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#sample data for task 2
data_2 = """word_freq,email_length,has_hyperlinks,sender_trusted,is_spam
15,500,1,0,1
2,150,0,1,0
20,800,1,0,1
1,120,0,1,0
12,450,1,0,1
3,200,0,1,0
18,600,1,0,1
4,180,1,1,0
25,900,1,0,1
2,100,0,1,0"""

df2 = pd.read_csv(StringIO(data_2))

X2 = df2[['word_freq', 'email_length', 'has_hyperlinks', 'sender_trusted']]
y2 = df2['is_spam']


#train model
model2 = LogisticRegression()
model2.fit(X2, y2)

#evaluate
predictions2 = model2.predict(X2)
accuracy = accuracy_score(y2, predictions2)
print(f"Model Accuracy: {accuracy:.2f}")

#deploy
def classify_incoming_email(features: list) -> str:
    """Classifies a new email given [word_freq, email_length, has_hyperlinks, sender_trusted]"""
    pred = model2.predict([features])[0]
    return "Spam" if pred == 1 else "Not Spam"

print(f"Classification of new email [10, 300, 1, 0]: {classify_incoming_email([10, 300, 1, 0])}")