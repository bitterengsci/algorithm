
# Steps
* Clarify Requirements
    - difficulty of the problem: Is Machine Learning required? Or traditional methods are good enough. How much more gain get from the model, compared with simple heuristics? 
    - performance: main goal? secondary goal? scale of the system? accuracy/latency required? data cost?
    - computation: resources limitation (phone? GPU server? cloud?)
    - Evaluation: how to evaluate the system in training/inferencing?
    - Personalization: one model for all users, or multiple? Base model trained on all data and fine-tune for each group?
    - Coupled/Interacted with other parts?
* data pipeline
    - Data engineers are responsible for ETL (Extract, Transform, Load) 
    - data availability
    - collect, annotate, clean
    - user data: feedback from user to improve the system online or periodically?
    - storage & compression: cloud, local, user device? what data structure? How often is the new data?
    - preprocessing:
        - feature engineering/extraction (importance of feature)
        - normalization
        - missing data, imbalance data
        - Is trainset and testset the same distribution?
        - How to combine data of different types? (texts vs numbers vs images)
        - bias: What biases might represent in the data? How would you correct the biases?
* modelling
    - model selection 
        - Occam's razor
        - 
    - loss function & metrics
    - train/evaluate models (hyperparameter tuning, scaling)
    - model testing, deploying, serving, monitoring, maintaining




problem statement → identify metrics → identify requirements → train & evaluate models → design high level system → scale the design


How would you build, train, and deploy a system that detects if multimedia and/or ad content violates terms or contains offensive materials? 
Design autocomplete and/or spell check on a mobile device
Design autocomplete and/or automatic responses for email
Design the YouTube recommendation system


How would you optimize prediction throughput for a RNN based model?
What loss function will you optimize and why?
What data will you collect to train your model and why?
How will you avoid bias and feedback loops?
How will you handle a corrupt model or an incorrect training batch?



What a Model can Do?
- automate (by taking action on the user’s behalf or by starting or stopping
a specific activity on a server)
- alert or prompt (by asking the user if an action should be taken or by
asking a system administrator if the traffic seems suspicious)
- organize, by presenting a set of items in an order that might be useful for a user (for
example, by sorting pictures or documents in the order of similarity to a query or
according to the user’s preferences)
- annotate (for instance, by adding contextual annotations to displayed information, or
by highlighting, in a text, phrases relevant to the user’s task)
- extract (by detecting smaller pieces of relevant information in a larger
input, such as named entities in the text: proper names, companies, or locations)
- recommend (by detecting and showing to a user highly relevant items in a
large collection based on item’s content or user’s reaction to the past recommendations)
- classify (by dispatching input examples into one, or several, of a predefined
set of distinctly-named groups)
- quantify (by assigning a number, such as a price, to an object, such
as a house)
- synthesize (by generating new text, image, sound, or another object similar
to the objects in a collection)
- answer an explicit question (“Does this text describe that image?” or
“Are these two images similar?”)
- transform its input (by reducing its dimensionality for visualization
purposes, paraphrasing a long text as a short abstract, translating a sentence into
another language, or augmenting an image by applying a filter to it),
- detect a novelty or an anomaly