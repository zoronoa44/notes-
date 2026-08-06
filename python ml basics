# 🐍 Week 4 — Basic ML with Python
### Complete Notes

---

# DAY 1 — NumPy

## What is NumPy?
- NumPy = **Numerical Python**
- ML ka foundation — har model andar se NumPy operations use karta hai
- Normal Python list se **250x faster**

## Why not normal lists?
```python
# Python list — ugly 😭
result = [a[i] * b[i] for i in range(len(a))]

# NumPy — clean 🔥
result = a * b
```

## ndarray — Core of NumPy
```
1D → [1, 2, 3]              → ek line of numbers
2D → [[1,2],[3,4]]          → table / matrix
3D → [[[1,2],[3,4]],...]    → cube
```

## Important Attributes
| Attribute | Meaning |
|-----------|---------|
| `.shape`  | (rows, columns) |
| `.ndim`   | number of dimensions |
| `.size`   | total elements |
| `.dtype`  | data type |

## Key Operations
```python
import numpy as np

arr = np.array([1,2,3,4,5])

# Vectorized ops
arr * 2          # [ 2  4  6  8 10]
arr ** 2         # [ 1  4  9 16 25]

# Statistics
np.mean(arr)     # average
np.std(arr)      # spread
np.sum(arr)      # total

# Matrix multiply
np.dot(A, B)     # ML ka core operation 🔥

# axis
np.mean(matrix, axis=0)  # column wise
np.mean(matrix, axis=1)  # row wise
```

## Boolean Indexing (Filtering)
```python
arr = np.array([10, 25, 30, 45, 50])
arr[arr > 30]    # [45 50] — filter karo
```

## Reshape
```python
arr.reshape(2, 3)   # 1D → 2D
arr.reshape(-1, 2)  # auto calculate rows
```

## Why Matrix Multiply matters?
```
Neural Networks = matrix multiplications ka stack
Input × Weights = Predictions
```

---

# DAY 2 — Pandas

## What is Pandas?
- Real data handle karne ka tool
- NumPy se better for mixed data types
- Missing values handle karta hai

## Two Building Blocks
```
Series    → 1D (ek column)
DataFrame → 2D (poori table)
```

## Loading Data
```python
df = pd.read_csv('file.csv')           # CSV
df = pd.read_csv('file.tsv', sep='\t') # TSV
```

## Essential Commands
```python
df.head()          # pehle 5 rows
df.tail()          # aakhri 5 rows
df.shape           # (rows, columns)
df.info()          # data types + missing
df.describe()      # statistics summary
df.isnull().sum()  # missing values count
```

## Selecting Data
```python
df["Age"]              # ek column
df[["Age", "Name"]]   # multiple columns
df.loc[0:4]           # label based
df.iloc[0:5, 0:3]     # index based
df[df["Age"] > 30]    # condition based
```

## Missing Values
```python
# fill karo
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna(df["City"].mode()[0], inplace=True)

# drop karo
df.drop("Cabin", axis=1, inplace=True)  # column drop
df.dropna()                              # rows drop
```

### Rule of Thumb
```
missing < 20%  → fill karo
missing > 50%  → drop karo
```

## Important Operations
```python
df["col"].value_counts()          # frequency count
df.groupby("Sex")["Age"].mean()   # group analysis
df.sort_values("Age")             # sort
df["New"] = df["A"] + df["B"]    # new column
```

## Pandas → NumPy
```python
arr = df["Age"].dropna().to_numpy()
# Pandas clean karta hai → NumPy math karta hai 🔥
```

## fit vs transform
```
fit_transform() → training data pe (seekho + convert)
transform()     → new data pe (sirf convert) ✅
```

---

# DAY 3 — What is ML?

## Traditional vs ML
```
Traditional:
Rules + Data → Output
(tum rules likhte ho)

Machine Learning:
Data + Output → Rules
(model khud rules seekhta hai) 🔥
```

## 3 Types of ML

### 1. Supervised Learning
```
→ Labeled data hota hai (answers diye hue)
→ Model seekhta hai → predict karta hai

Examples:
✅ Email → Spam/Not Spam
✅ Symptoms → Disease
✅ House size → Price
```

### 2. Unsupervised Learning
```
→ No labels (koi answers nahi)
→ Model khud patterns/groups dhundta hai

Examples:
✅ Customer segmentation
✅ Network anomaly detection
✅ Document clustering
```

### 3. Reinforcement Learning
```
→ Agent + Environment
→ Sahi action = Reward ✅
→ Galat action = Punishment ❌
→ Agent seekhta hai maximize rewards

Examples:
✅ YouTube recommendations
✅ Self driving cars
✅ Game AI
```

## ML Vocabulary
| Term | Meaning |
|------|---------|
| Dataset | data ka collection |
| Features | input columns (X) |
| Label | answer column (y) |
| Model | jo machine ne seekha |
| Training | model ko sikhana |
| Testing | model check karna |
| Accuracy | % sahi predictions |

## ML Workflow
```
Raw Data
    ↓
Clean Data (Pandas)
    ↓
Features + Label select
    ↓
Train/Test Split
    ↓
Model Train
    ↓
Model Test
    ↓
Accuracy Check
```

---

# DAY 4 — First ML Model

## Train/Test Split — Why?
```
Problem:
Agar poora data sikhane mein diya →
Check kaise karein model seekha ya nahi?

Solution:
80% → Training (sikhao)
20% → Testing  (check karo)

Analogy:
80% syllabus practice → 20% mock test
Mock test mein naye questions hote hain ✅
```

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# random_state=42 → har baar same split
```

## Decision Tree
```
Ek tree banata hai — questions puchta hai:

Petal length < 2.5?
├── Yes → Setosa 🌸
└── No  → Petal width < 1.8?
          ├── Yes → Versicolor 🌺
          └── No  → Virginica 🌻
```

## First Model — Iris Dataset
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)      # seekho

predictions = model.predict(X_test)  # predict karo
print(accuracy_score(y_test, predictions))
```

## Key Methods
```
fit()     → model ko sikhao
predict() → naye data pe apply karo
```

## LabelEncoder — Text → Numbers
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['encoded'] = le.fit_transform(df['text_column'])
# "Yes/No" → 1/0
# ML models numbers chahte hain, strings nahi 💀
```

---

# DAY 5 — ML + Security 🔐

## Why ML for Security?
```
Traditional:
Rule: "port 4444 = suspicious"
Hacker: uses port 4445 → rule fail 💀

ML:
Normal traffic pattern seekha
Kuch unusual → ALERT 🚨
Hacker koi bhi port use kare → pakad lega 🔥
```

## Anomaly Detection
```
Normal  = jo usually hota hai ✅
Anomaly = jo unusual hai = suspicious 🚨

Examples:
→ Bank: achanak Dubai mein transaction 🚨
→ Network: 10,000 requests/sec suddenly 🚨
→ Login: 3am Russia se login 🚨
```

## Isolation Forest
```
Forest  = bohot saare decision trees
Isolate = anomaly ko alag karna

Logic:
Normal point  → bheed mein hai → isolate karna mushkil
               → zyada cuts chahiye

Anomaly point → akela hai → isolate karna easy
               → kam cuts chahiye 🎯

Kam cuts = anomaly 🚨
```

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.05)
model.fit(data)

predictions = model.predict(data)
#  1 = normal ✅
# -1 = anomaly 🚨

anomalies = data[predictions == -1]
```

## Defence in Depth
```
Ek model = bypassable 💀

Real world:
Layer 1 → Isolation Forest    (anomaly)
Layer 2 → Behaviour Analysis  (pattern change)
Layer 3 → Threat Intelligence (known attacks)
Layer 4 → Human Analyst       (final call) 🧠
```

## Security Use Cases
```
Network Intrusion → packet size, frequency, ports
User Behaviour    → login time, location, files
Malware Detection → API calls, memory, file ops
Financial Fraud   → amount, location, time
```

---

# DAY 6 — Spam Detector 📧

## Problem
```
ML models = numbers samajhte hain
Text      = numbers nahi hai 💀

Solution:
Text → Numbers → Model ✅
```

## CountVectorizer
```
Har unique word = ek column
Har email = ek row
Word count = number

"free money now" + "meeting tomorrow"

         free  meeting  money  now  tomorrow
Email 1    1      0       1     1      0
Email 2    0      1       0     0      1
```

## Naive Bayes
```
Naive      = word order ignore karta hai
Multinomial = word counts use karta hai

Logic:
"free" → 90% spam emails mein tha
"free" aaya → spam hone ki probability high 🚨
```

## Complete Flow
```python
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])  # text → numbers

model = MultinomialNB()
model.fit(X, labels)                          # train

# new email check
result = model.predict(vectorizer.transform(["free money"]))
```

## fit vs transform — Important!
```
Training data:
→ fit_transform() ← vocabulary seekho + convert ✅

New/Test data:
→ transform() only ← same vocabulary use karo ✅
→ fit_transform() GALAT ❌ → naya vocabulary = mismatch
```

## Security Connection
```
Spam detector   → phishing emails
Same concept    → malware code detection
SIEM tools      → suspicious log messages
```

---

# WEEK 4 — COMPLETE SUMMARY

## What You Built
```
✅ NumPy operations — ML ka foundation
✅ Pandas — real data cleaning
✅ First ML model — Iris classifier
✅ Anomaly detector — network security
✅ Spam detector — 5574 real messages
✅ 3+ projects on GitHub 🔥
```

## Key Connections
```
Pandas    → data clean karo
NumPy     → math karo
sklearn   → models banao
All three → ek saath ML pipeline 🔥
```

## ML Types — Quick Reference
```
Supervised     → labeled data → predict karo
Unsupervised   → no labels → patterns dhundo
Reinforcement  → reward/punishment → seekho
```

## Common Mistakes to Avoid
```
❌ fit_transform() new data pe
❌ shape mismatch ignore karna
❌ missing values bina handle kiye model chalana
❌ test data training mein dalna (data leakage)
✅ always: clean → split → train → test → evaluate
```

---

*Week 4 Complete 🔥 — NumPy + Pandas + ML Basics + AI Security Foundation*
