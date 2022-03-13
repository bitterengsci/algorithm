

# ML基础概念类
overfitting/underfiting:
- underfitting means large training error, large generalization error; overfitting means small training error, large generalization error
- overfitting means training loss is small and testing loss is large, small regularization
- overfit means complex model, underfit means over-simplified model.
- overfitting: model is tailored to a particular dataset and is unable to generalise to other datasets

bias/variance trade off
- A set of predictive models whereby models with a lower bias in parameter estimation have a higher variance of parameter estimates across samples, and vice versa.
- linear/logistic regression: underfitting—high bias, overfitting—high variance
- high bias (model miss relevant relations between features and target output—underfitting)
- high variance (model modelled random noise in the training data—overfitting)

Bias Variance Decomposition: Error = Bias ** 2 + Variance + Irreducible Error


How to overcome/prevent Overfitting:
1. Regularization 
  - L1 regularization (lasso penalty) favours few non-zero coefficients   λ∑∣θ∣
  - L2 regularization (ridge/Tikhonov penalty) favours small coefficients	 λ∑θ2
  - Mixed L1/L2 regularization (elastic net)  λ1∑∣θ∣+λ2∑θ2
  - L^p regularization (penalty on parameters)
2. early stopping: interrupt training when its performance on the validation set starts dropping
3. Max-norm: for each neuron the weight θ of the incoming connections are constrained such that  𝄁θ𝄁2≤r  (clipping)
  - compute 𝄁θ𝄁2 after each training step and clip θ if needed θ=θr/𝄁θ𝄁2
  - max-norm hyperparameter r increases the amount of regularization
4. dropout: at every training step, every neuron (input/hidden) has a probability of p of being temporarily dropped out
   ≈ an ensemble learning method
5. data augmentation: variation of input data; artificially boosting the size of training set
 by rotate, shift(translate), resize(scale), flip(reflect), or add different lighting conditions or noise that can be learnt
6. Stochastic Gradient Descent

Generative/Discrimitive:
- Generative models model the (actual) distribution of each class.
- given training data, Generative models generate new samples from same distribution, learn Pmodel(x)≈Pdata(x)
- Discriminative models learn the (hard or soft) decision boundary between the classes. 

Give a set of ground truths and 2 models, how do you be confident that one model is better than another?

## Reguarlization
Occam’s Razor: among competing hypotheses, the simplest is the best. 

L1 regularization (lasso penalty) 
- favours few non-zero coefficients   λ∑∣θ∣
- prior: Laplace distribution with mean zero and a scale parameter a function of λ

L2 regularization (ridge/Tikhonov penalty) 
- favours small coefficients	 λ∑θ2
- prior: a Gaussian with mean zero and standard deviation a function of λ
- Optimizing with respect to L2 norm corresponds to maximizing the (log-)likelihood of the data under a Gaussian prior. 

Lasso/Ridge的推导

Why L1 sparse: L2 penalties in some sense discourage sparsity by yielding diminishing returns as elements are moved closer to zero

为什么regularization works
为什么regularization用L1 L2，而不是L3, L4..

## Metric
Confusion Matrix
- A breakdown of predictions into a table showing correct predictions (the diagonal) and the types of incorrect predictions made (what classes incorrect predictions were assigned)

Precision (Positive Predictive Value)= true positive / (true positive + false positive)
- measure of exactness
Recall (True Positive rate, sensitivity) = true positive / (true positive + false negative)
- measure of completeness

F/F1-Score: weighted average of precision and recall 2 * (P * R) / (P + R)

True Negative Rate/Specificity
False Positive rate = FP / (FP + TN)
Accuracy

ROC curve (receiver operating characteristic)
- showing the performance of a classification model at all classification thresholds
- x-axis: FP rate, y-axis: TP rate  (TPR vs. FPR at different classification thresholds)


AUC (Area Under the ROC Curve)
- an aggregate measure of performance across all possible classification thresholds
- A model whose predictions are 100% wrong has an AUC of 0; one whose predictions are 100% correct has an AUC of 1.
- scale invariant. It measures how well predictions are ranked, rather than their absolute values.
- classification-threshold invariant. It measures the quality of the model's predictions irrespective of what classification threshold is chosen.

precision and recall, trade-off

label 不平衡时用什么metric
分类问题该选用什么metric，and why
confusion matrix
AUC的解释 (the probability of ranking a randomly selected positive sample higher blablabla....)
Log-loss是什么，什么时候用logloss
还有一些和场景比较相关的问题，比如ranking design的时候用什么metric，推荐的时候用什么

## Loss & Optomization
用MSE做loss的Logistic Rregression是convex problem吗
解释并写出MSE的公式, 什么时候用到MSE?
Linear Regression最小二乘法和MLE关系
什么是relative entropy/crossentropy

Kullback-Leiber Divergence
- intuition: 
- a measure of difference of 2 probability distributions (how close 2 distributions are)


Logistic Regression的loss是什么
Logistic Regression的 Loss 推导
SVM的loss是什么
Multiclass Logistic Regression然后问了一个为什么用cross entropy做cost function
Decision Tree split node的时候优化目标是啥


# DL基础概念类

bias term in DNN: shift the activation function

DNN为什么要有bias term, bias term的intuition是什么
什么是Back Propagation

Epoch
- one pass through the whole training set
- If there are N training samples and use B batch size, then it takes N/B iterations to complete on epoch

Gradient Vanishing & Exploding
- Vanishing:
    - activation function squishes a large input space into a small one (e.g., sigmoid 0 to 1); large change in the input results in small change in the output --> derivative small
    - use other activations, like ReLU (not cause a small derivative)
    - residual network
    - batch normalization (normalize the input)
    - use more complex RNN
- Exploding: gradient becomes very large, preventing the algorithm from converging
    - gradient clipping (clip by value, clip by norm)

Initialize all weights to be 0?
- constant initialization leads to same gradient propagated back everywhere (symmetric)

DNN和Logistic Regression的区别; 为什么DNN的拟合能力比Logistic Regression强? 
- Non-linearity introduced by activation functions

Hyperparameter tuning in DL: random search, grid search

prevent overfitting in DL: dropout, early stopping, data augumentation
- 什么是Dropout，why it works，dropout的流程是什么 (训练和测试时的区别)
- 什么是Batch Norm, why it works, BN的流程是什么 (训练和测试时的区别)

Activation Functions
1. Logistic/Sigmoid: 1 / (1 + exp(-x))
    - 0.0 ~ 1.0, f(z) saturates at 0 or 1, i.e., derivative becomes almost 0/megligible.
2. Hyperbolic Tangent tanh: (e^x – e^-x) / (e^x + e^-x)
    - -1.0 ~ +1.0, f(z) saturates at -1 or 1
    - 
3. Rectified Linear Unit 
    - discontinuity at 0 but has sub-gradient
    - outperform the sigmoid function
    - gradient will not vanish when z is very large, but gradient becomes 0 when z becomes negative, which may still lead to vanishing gradient problem
    - leaky relu: f(z)=0.01z, z<0; z, z>0
    - Parametric ReLU    f(z)=az, z<0; z, z>0    (learning parameter a in training)
    - Exponential Linear unit  f(z)=a(e^z﹣1), z<0; z, z≥0

Softmax: e^x / sum(e^x)

为什么需要non-linear activation functions

Different optimizers (SGD, RMSprop, Momentum, Adagrad，Adam) 的区别

Batch vs  SGD
- Stochastic gradient descent: approximate the gradient using current sample
- Mini-Batch: use a small batch of b samples
- Small batch size:
    - stalls at less accurate result, lower iteration cost
    - gradient may become sensitive to a single training sample
- Large batch size:
    - stalls at more accurate result, higher iteration cost
    - computation will become expensive and use more memory on GPU.

learning rate/step size
1. small step size: 
    - slower initial convergence, stalls at more accurate result
    - optimization may be slow
2. large step size: 
    - faster initial convergence, stalls at less accurate result
    - With a high learning rate, the optimization is faster but may bounce chaotically and not arrive at good local minima
	- With a very high learning rate, the optimization may diverge

Problem of Plateau, saddle point

When transfer learning makes sense?
- Transfer learning only works in deep learning if the model features learned from the first task are general.


# ML模型类
## Regression:
four principal assumptions for Linear Regression:
1. Linearity and additivity
2. statistical independence
3. homoscedasticity
4. normality

what will happen when we have correlated variables, how to solve
explain regression coefficient

what is the relationship between minimizing squared error and maximizing the likelihood

How could you minimize the inter-correlation between variables with Linear Regression?
if the relationship between y and x is no linear, can linear regression solve that

why use interaction variables


## Clustering and EM:
K-means clustering (explain the algorithm in detail; whether it will converge, 收敛到global or local optimums;  how to stop)

EM算法是什么
GMM是什么，和Kmeans的关系


## Decision Tree
How regression/classification DT split nodes?
How to prevent overfitting in DT?
How to do regularization in DT?


## Ensemble Learning
Bagging: (Bootstrap Aggregating): reduce model variance through averaging
- Bootstraping (train separate weak learners on each Bootstrap sample)
- Aggregating results: classification uses majority votes; regression used averaging.

Boosting:
- build weak learners in serial/sequential
- but adaptively re-weight training data prior training each new weak learner, in order to get a higher weight to previously misclassified examples

Random Forest: homogenous ensemble learning of decision trees
- bult using Bagging (each decision tree as a parallel estimator)
- pros: a whitebox model (easy to understand, interpretable, visualizable); not require normalization; 
- cons: need uncorrelated decision trees (Bootstrapping plays a key role in creating uncorrelated decision trees.)

gradient boosted decision trees (GBDT):
- built using Boosting (decision trees connected in series)
- to minimize the error of previous tree
- Decision trees in GBDT are not fit to the entire dataset. Each tree fits to the residuals from the previous one. 
- As a result, the overall accuracy and robustness of the model gradually increase.
- pros: do not need bootstrapping, no correlated trees; no need to create subsamples from the dataset

will random forest help reduce bias or variance/why random forest can help reduce variance


## Generative Model
和Discrimitive模型比起来，Generative 更容易overfitting还是underfitting


Naïve Bayes的原理，基础假设是什么


LDA/QDA是什么，假设是什么
- Latent Dirichlet allocation

Linear/normal discriminant analysis (LDA) vs Quadratic discriminant analysis (QDA)
- conditional probability density function P(x|y=0) and P(x|y=1) are normal distributions N(μ0, Σ0) and N(μ1, Σ1)
- Bayes optimal solution is to predict points as being from the second class if the log of the likelihood ratios is bigger than some threshold T: (x - μ0)Σ0(x - μ0) + ln|Σ0| - (x - μ1)Σ1(x - μ1) - ln|Σ1| > T  (QDA)
- LDA: assume Σ0=Σ1, dot(w, x) > c where w = pow(Σ, -1) * (μ1 - μ0) and c = dot(w, (μ1 + μ0) / 2)
    - the criterion of an input x being in a class y is purely a function of the linear combination of the known observations.


## Logistic Regression
logistic regression vs svm（我想这个主要是想问两者的loss的不同以及输出的不同，一个是概率输出一个是score）
- both solves classification; SVM can solve regression too.
- loss
- output

LR大部分面经集中在logloss和regularization，

SVM
- a classifier defined by a separating hyperplane(decision boundary), where same distance from the boundary point of both classes
- kernel tricks: a method of using a linear classifier to solve a non-linear problem; kernel transforms linearly inseparable data to linearly separable ones by mapping them into higher-dimensional space.

- SVM is based on geometrical properties of data; logistic regression is statistical.
- SVM less vulnarable to overfitting

- output SVM as a probability: 如何让SVM输出分类概率 
    - sigmoid-fitting
    - SVM + Logistic Regression blending

## 其他模型

Principal component analysis (PCA)
- create new uncorrelated variables that successively maximize variance by solving an eigenvalue/eigenvector problem.
- reduce the dimensionality of dataset, increase interpretability while minimize information loss
- pros: no need of prior; reduce overfitting (by reduce #variables in the dataset); visualizable
- cons: data standardization is a prerequisite; information loss


Kernel Method/Tricks
- best known member is SVM
- enable to operate in a high-dimensional, implicit feature space without computing the coordinates of the data in that space.
- why use kernel:
- pros: often computationally cheaper than explicit computation of the coordinates; 
- cons: 
- Radial basis function kernel exp( - sqrt((x1 - x2)^2) / 2 * σ^2)
- polynomial kernel: (x1^T * x2 + c) ** d


Explain KNN
!所有模型的pros and cons （最高频的一个问题）


# Data Processing
imbalanced data
- change performance metric
    - Kappa/Cohen’s kappa: Classification accuracy normalized by the imbalance of the classes in the data.
- resampling to even up the class
- collect more data, generate synthetic samples
    - Synthetic Minority Oversampling Technique: SMOTE uses KNN to create new instances
- bias the model to pay more attention to minority class by penalty
- balanced bagging classifier

problem with high-dim classification
- Curse of Dimensionality: number of training examples we need to cover the space densely, exponential in the dimensionality of the problem; we will never get enough examples; also computational burden
- N grows exponentially with D
- solution
    - LDA-type methods: Naive Bayes, Nearest Shrunken Centroid, Sparse LDA, regularized LDA
    - penalized logistic regression
    - large-margin methods (SVM)
    - classification tree (random forest)
    - boosting


missing data
- 60% observations missing, better discard it 
- mean, median, mode of the existing observations (dont use in time-series characteristics)
- multiple imputation and combine multiple analysis to produce an overall result
- mean among K Nearest Neighbors

Missing Time-Series Data
- last observation carried forward, next observation carried backward
- linear interpolation
- seasonal adjustment with linear interpolation


Feature Selection (~dimensionality reduction):
- wrapper: create many models with different subsets of features and select those features that result in the best performing model according to a performance metric. 
    - unconcerned with variable types, computationally expensive
- filter: evaluate the relationship between each input feature and the target variable (importance of feature)
- intrinsic: algorithms perform feature selection automatically as part of learning the model (penalized regression, LASSO; random forest)
- unsupervised: correlation


how to capture feature interaction


# implementation & derivation
```python
class FullyConnected:
    def __init__(self, inp_size, out_size):
        self.W = np.random.rand(inp_size, out_size)
        self.b = np.random.rand(1, out_size)

    def forward(self, x):
        self.inp = x
        return np.dot(self.inp, self.W) + self.b

    def backward(self, out_error, learning_rate):
        self.W -= learning_rate * (np.dot(self.inp.T, out_error))
        self.b -= learning_rate * out_error


class Convolution:
    def __init__(self):
        # we have [H0, W0, C0], C1, kernel_size, stride, pad, dilation.
        # H1 = floor((H0 - k + 2 * p) / s) + 1

    def forward(self,)

```

```python
# KNN --------------------------------------
def KNN(input, data, k=5):
    # input is (N, ), data is (B, N)
    input = np.expand_dims(input, axis=1)
    # Euclidean distance
    metrics = np.sqrt(np.sum(np.subtract(data, input.T) ** 2, axis=1))
    topk = np.argsort(metrics)[: k]
    return topk  # classfication by vote, regression by mean


# KMeans Clustering ------------------------
def get_centriods(data, assignment):
    # data is [B, N], assignment is a dict
    centriods = []
    for k in assignment:
        data_in_k = assignment[k]
        centriods.append(np.mean(np.array(data_in_k), axis=0))
    return centriods  # [K, N]


def assign(data, centriods):
    assignments = dict()
    for i in range(data.shape[0]):
        point = data[i, :]
        assignto = np.argsort(np.sum(np.subtract(point, centriods) ** 2, axis=1))[0]
        assignments[assignto] =  assignments.get(assignto, []) + [point]

    return assignments


def get_MSE(data, centriods, assignment):
    MSE = 0
    for k, vs in assignment.items():
        center = centriods[k]
        for v in vs:
            MSE += np.sum((v - center) ** 2)
    return MSE ** 0.5 / data.shape[0] 


def initialize_centriods(data, k):
    return data[:k, :]

def initialize_centriods_random(data, k):
    return np.random.rand(k, data.shape[1])


def KMeans(data, k=3):

    threshold=0.01
    early_stopping = 10

    centriods = initialize_centriods_random(data, k)
    print(centriods)
    assignment = assign(data, centriods)

    count = 0
    while get_MSE(data, centriods, assignment) > threshold \
        and count < early_stopping:

        centriods = get_centriods(data, assignment)
        assignment = assign(data, centriods)
        print(centriods[0])
        count += 1
```
手写softmax的backpropagation
给一个LSTM network的结构要你计算how many parameters

       
# 项目经验类
训练好的模型在现实中不work

Loss Inf/NaN:
- learning rate too high
- gradient exploding (add gradient clipping)
- divide by 0
- input contains NaN
- NaN running_mean or running_var in BatchNorm

生产和开发时候data发生了一些shift应该如何detect和补救

Data Shift: 
- covariate shift (shift in independent variables/input features)
    - change in the distribution of the input variables present in the training and test set. 
    - can be addressed by batch normalization
    - e.g train a cat classifier on the set of images containing white cats and other non-cat images, then it is applied on test of black cats.
- prior probability shift(shift in the target variable)
- concept shift(shift in the relationship between the independent and the target variable)

Training with limited annotation
- data annotation; data augumentation
- pre-training with synthenic data or some geometric constraints (homography transformation), like superpoint
- pretrained backbone/model, fine tune
- self-supervised learning; unsupervised learning
- distillation

假设有个model要放production了但是发现online one important feature missing不能重新train model 你怎么办

# NLP/RNN相关
LSTM的公式是什么
why use RNN/LSTM

LSTM
- special RNN, but capable of leanring long-term dependencies
- nature of remembering information for a long periods of time
- forget gate, input gate, output gate

limitation of RNN
- gradient vanishing (use LSTM)
- training is difficult

attention
- self attention mechanism allows the inputs to interact with each other, find out who they should pay more attention to; outputs are aggregates of interactions and attention scores
- why attention

```python
querys = x @ w_query
keys = x @ w_key
values = x @ w_value

attention_scores = softmax(querys @ keys.T, dim=-1)
weighted_values = values * attention_scores
output = weighted_values.sum(dim=0)
```
- cross attention
- attention to Transformer

Language Model的原理，N-Gram Model
What’s CBOW and skip-gram?
什么是Word2Vec， loss function是什么， negative sampling是什么

# CNN/CV相关

pooling
- reduce the dim of featuremaps, i.e., number of parameters to learn/computations.
- pooling layer summarises the features present in a region of the feature map generated by a convolution layer.
- maxpooling

conv layer是什么, 为什么用conv lay，

什么是equivariant to translation, invariant to translation

1x1 filter: used to reduce the dimension of depth channel, while not look at anything around itself.

ResNet 什么是skip connection
- ResNet34: conv7x7 + pool + 16 ResNet Blocks (some skip connection omitted) + avgpool + fc1000
- ResNet block: ReLU( conv3x3( ReLU( conv3x3(x) ) + x ) )
- ResNeXt: 
    - cardinality/group: a hyperparameter indicating the number of independent paths, to provide a new way of adjusting the model capacity
    - 'split-transform-merge' is usually done by pointwise grouped convlayer, which divides input into groups of feature maps and perform convolution respectively, their outputs are depth-concentrated and then fed into1 1x1 convlayer.

FPN RPN

1-stage detection
2-stage detection

# Loss Function

1. regression
MAE (L1)
MSE (L2)
smooth L1 loss
Huber loss

2. classification
0-1 loss
hinge loss
cross entropy


3. detection, segmentation
focal loss
triplet loss
contrastive loss
center loss
IOU loss

ArcFace loss

# 关于准备考ML 概念的面试的一些建议
1. 如果你简历上提到了一个模型，请确保你对这个模型有着深入全面的了解 （比如很多人可能简历里都提到了XgBoost，但是可能了解并不全面）
举个例子，我简历上提到了Graph Convolutional NN， 我面试的时候就被要求不用包手写一个简单的GCN。
2. 如果job description上提到了某些模型，最好对这些模型也比较熟悉。
3. 对你这个组的domain的相关模型要熟悉。
比如，你面一个明确做NLP的组，那么上述面经就过于基础了。
你或许还要知道 What is BERT， explain the model architecture；what is Transformer model， explain the model architecture；Transformer/BERT 比LSTM好在哪；difference between self attention and traditional attention mechanism；或许你还要知道一些简单的做distill的方法..或许根据组的方向你还要知道ASR, 或者Chat bot等等的方向的一些widely used的模型或者方法。
比如你面一个CTR的组，或许可能你大概至少要稍微了解下wide-and-deep
比如你面一个CV-segment的组，你或许可能要了解DeepMask，U-Net...等等..
你应该不一定需要知道最SOTA的模型，但是知道那些最广为运用的模型或许可能是必要的。




p-value
- probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- 

  3）Gradient descent 解释原理，什么是 mini batch GD, stachastic GD, Adam
  4）NN 里面 gradient descent怎么计算，是convex的吗，能保证最优解吗，（不能保证）怎么解决
  5）Regression 用什么loss? Classification 用什么loss， 多分类呢？分类的loss是convex的吗
  7）Random forest hyperparameter 怎么选
  8）Validation set 都用来干嘛