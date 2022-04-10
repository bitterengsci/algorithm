
<!-- TOC -->

- [1. ML基础概念类](#1-ml基础概念类)
  - [1.1. Reguarlization](#11-reguarlization)
  - [1.2. Metric](#12-metric)
  - [1.3. Loss & Optimization](#13-loss--optimization)
- [2. DL基础概念类](#2-dl基础概念类)
- [3. ML模型类](#3-ml模型类)
  - [3.1. Regression:](#31-regression)
- [4. Convolution](#4-convolution)
  - [4.1. Clustering and EM:](#41-clustering-and-em)
  - [4.2. Decision Tree](#42-decision-tree)
  - [4.3. Ensemble Learning](#43-ensemble-learning)
  - [4.4. Generative Model](#44-generative-model)
  - [4.5. Logistic Regression](#45-logistic-regression)
  - [4.6. 其他模型](#46-其他模型)
- [5. Data Processing](#5-data-processing)
- [6. implementation & derivation](#6-implementation--derivation)
- [7. NLP/RNN相关](#7-nlprnn相关)
- [8. CNN/CV相关](#8-cnncv相关)
- [9. VAE, GANs](#9-vae-gans)
- [10. Loss Function & Optimization](#10-loss-function--optimization)
- [11. Detection](#11-detection)
- [12. 项目经验类](#12-项目经验类)
- [13. 关于准备考ML 概念的面试的一些建议](#13-关于准备考ml-概念的面试的一些建议)
- [14. Pytorch Example](#14-pytorch-example)
- [ToDo List](#todo-list)

<!-- /TOC -->

# 1. ML基础概念类
overfitting/underfiting:
- underfitting means large training error, large generalization error; overfitting means small training error, large generalization error
- overfitting means training loss is small and testing loss is large, small regularization
- overfit means complex model, underfit means over-simplified model.
- overfitting: model is tailored to a particular dataset and is unable to generalise to other datasets

bias/variance trade off
- A set of predictive models whereby models with a lower bias in parameter estimation have a higher variance of parameter estimates across samples, and vice versa.
- linear/logistic regression: underfitting—high bias, overfitting—high variance
- high bias, low variance (underfitting: model too simple, model miss relevant relations between features and target output)
- high variance, low bias (overfitting: model modelled random noise in the training data)

Bias Variance Decomposition: Error = Bias ** 2 + Variance + Irreducible Error


How to overcome/prevent Overfitting:
1. Regularization 
  - L1 regularization (lasso penalty) favours few non-zero coefficients   λ∑∣θ∣
    - L1 also performs vairable selection and yield sparse models.
  - L2 regularization (ridge/Tikhonov penalty) favours small coefficients	 λ∑θ2
    - L2 more sensitive to outliers; gradient exploding issue
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

## 1.1. Reguarlization
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


## 1.2. Metric
Confusion Matrix
- A breakdown of predictions into a table showing correct predictions (the diagonal) and the types of incorrect predictions made (what classes incorrect predictions were assigned)

Precision (Positive Predictive Value) = true positive / (true positive + false positive)
- measure of exactness
Recall (True Positive rate, sensitivity) = true positive / (true positive + false negative)
- measure of completeness

F/F1-Score: weighted average of precision and recall 2 * (P * R) / (P + R)
- consider both FP and FN

True Negative Rate/Specificity = TN / (FP + TN)
False Positive Rate = FP / (FP + TN)
Accuracy

ROC curve (receiver operating characteristic)
- showing the performance of a classification model at all classification thresholds
- x-axis: FP rate, y-axis: TP rate  (TPR vs. FPR at different classification thresholds)
- often used as a proxy for the trade-off between the sensitivity of the model (true positives) vs the fall-out or the probability it will trigger a false alarm (false positives). --> precision and recall trade-off
- The curves of different models can be compared directly in general or for different thresholds.
- The area under the curve (AUC) can be used as a summary of the model skill

Precision-Recall Curve
- a plot of precision (y-axis) and recall (x-axis) for different thresholds

AUC (Area Under the ROC Curve)
- an aggregate measure of performance across all possible classification thresholds
- A model whose predictions are 100% wrong has an AUC of 0; one whose predictions are 100% correct has an AUC of 1.
- scale invariant. It measures how well predictions are ranked, rather than their absolute values.
- classification-threshold invariant. It measures the quality of the model's predictions irrespective of what classification threshold is chosen.

Type I error is a false positive, Type II error is a false negative. 
- Type I error means claiming something has happened when it hasn’t
- Type II error means that you claim nothing is happening when in fact something is. 
- e.g., Type I error as telling a man he is pregnant, Type II error as you tell a pregnant woman she isn’t carrying a baby.


label 不平衡时用什么metric
分类问题该选用什么metric，and why
confusion matrix
AUC的解释 (the probability of ranking a randomly selected positive sample higher blablabla....)
Log-loss是什么，什么时候用logloss
还有一些和场景比较相关的问题，比如ranking design的时候用什么metric，推荐的时候用什么

stratified cross-validation
- split preserves the ratio of the categories on both the training and validation datasets
- applications: imbalanced dataset


## 1.3. Loss & Optimization
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


# 2. DL基础概念类

bias term in DNN: shift the activation function

DNN为什么要有bias term, bias term的intuition是什么
什么是Back Propagation

Epoch
- Epoch: one pass through the whole training set
- Batch: examples processed together in one pass (forward and backward)
- Iteration: number of training examples / Batch size
- If there are N training samples and use B batch size, then it takes N/B iterations to complete on epoch

Gradient Vanishing & Exploding
- Vanishing:
    - activation function squishes a large input space into a small one (e.g., sigmoid 0 to 1); large change in the input results in small change in the output --> derivative small
    - use other activations, like ReLU (not cause a small derivative)
    - residual network
    - batch normalization (normalize the input) 
        - if batchsize = 1?
        - multiple publications have shown BN performance degrade for batch_size under 32, and severely for <= 8.
    - use more complex RNN
- Exploding: gradient becomes very large, preventing the algorithm from converging
    - gradient clipping (clip by value, clip by norm)
    - use LSTM

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
    - gradient vanish problem, time-consuming to compute exponentials, not symmetric w.r.t. the origin
2. Hyperbolic Tangent tanh: (e^x – e^-x) / (e^x + e^-x)
    - -1.0 ~ +1.0, f(z) saturates at -1 or 1
    - gradient vanish problem
    - faster than sigmoid, symmetric w.r.t. the origin
3. Rectified Linear Unit ReLU
    - discontinuity at 0 but has sub-gradient
    - outperform the sigmoid function
    - gradient will not vanish when z is very large, but gradient becomes 0 when z becomes negative, which may still lead to vanishing gradient problem (partially solve vanishing problem); neuron dies in negative
    - leaky relu: f(z)=0.01z, z<0; z, z>0
    - Parametric ReLU    f(z)=az, z<0; z, z>0    (learning parameter a in training)
    - Exponential Linear unit  f(z)=a(e^z﹣1), z<0; z, z≥0
4. maxout: max(w1x+b1, w2x+b2)   a piecewise-linear function

Softmax: e^x / sum(e^x)


为什么需要non-linear activation functions?
- 对于神经网络来说，网络的每一层相当于f(wx+b)=f(w'x)，对于线性函数，其实相当于f(x)=x，那么在线性激活函数下，每一层相当于用一个矩阵去乘以x，那么多层就是反复的用矩阵去乘以输入。根据矩阵的乘法法则，多个矩阵相乘得到一个大矩阵。所以线性激励函数下，多层网络与一层网络相当。比如，两层的网络f(W1*f(W2x))=W1W2x=Wx。
- 非线性变换是深度学习有效的原因之一。原因在于非线性相当于对空间进行变换，变换完成后相当于对问题空间进行简化，原来线性不可解的问题现在变得可以解了。

神经网络中激活函数的真正意义？一个激活函数需要具有哪些必要的属性？还有哪些属性是好的属性但不必要的？
- (1) 非线性：即导数不是常数。这个条件是多层神经网络的基础，保证多层网络不退化成单层线性网络。这也是激活函数的意义所在。
- (2) 几乎处处可微：可微性保证了在优化中梯度的可计算性。传统的激活函数如sigmoid等满足处处可微。对于分段线性函数比如ReLU，只满足几乎处处可微（即仅在有限个点处不可微）。对于SGD算法来说，由于几乎不可能收敛到梯度接近零的位置，有限的不可微点对于优化结果不会有很大影响[1]。
- (3) 计算简单：非线性函数有很多。极端的说，一个多层神经网络也可以作为一个非线性函数，类似于Network In Network[2]中把它当做卷积操作的做法。但激活函数在神经网络前向的计算次数与神经元的个数成正比，因此简单的非线性函数自然更适合用作激活函数。这也是ReLU之流比其它使用Exp等操作的激活函数更受欢迎的其中一个原因。
- (4) 非饱和性（saturation）：饱和指的是在某些区间梯度接近于零（即梯度消失），使得参数无法继续更新的问题。最经典的例子是Sigmoid，它的导数在x为比较大的正值和比较小的负值时都会接近于0。更极端的例子是阶跃函数，由于它在几乎所有位置的梯度都为0，因此处处饱和，无法作为激活函数。ReLU在x>0时导数恒为1，因此对于再大的正值也不会饱和。但同时对于x<0，其梯度恒为0，这时候它也会出现饱和的现象（在这种情况下通常称为dying ReLU）。Leaky ReLU和PReLU的提出正是为了解决这一问题。
- (5) 单调性（monotonic）：即导数符号不变。这个性质大部分激活函数都有，除了诸如sin、cos等。个人理解，单调性使得在激活函数处的梯度方向不会经常改变，从而让训练更容易收敛。
- (6) 输出范围有限：有限的输出范围使得网络对于一些比较大的输入也会比较稳定，这也是为什么早期的激活函数都以此类函数为主，如Sigmoid、TanH。但这导致了前面提到的梯度消失问题，而且强行让每一层的输出限制到固定范围会限制其表达能力。因此现在这类函数仅用于某些需要特定输出范围的场合，比如概率输出（此时loss函数中的log操作能够抵消其梯度消失的影响）、LSTM里的gate函数。
- (7) 接近恒等变换（identity）：即约等于x。这样的好处是使得输出的幅值不会随着深度的增加而发生显著的增加，从而使网络更为稳定，同时梯度也能够更容易地回传。这个与非线性是有点矛盾的，因此激活函数基本只是部分满足这个条件，比如TanH只在原点附近有线性区（在原点为0且在原点的导数为1），而ReLU只在x>0时为线性。这个性质也让初始化参数范围的推导更为简单。额外提一句，这种恒等变换的性质也被其他一些网络结构设计所借鉴，比如CNN中的ResNet和RNN中的LSTM。
- (8) 参数少：大部分激活函数都是没有参数的。像PReLU带单个参数会略微增加网络的大小。还有一个例外是Maxout，尽管本身没有参数，但在同样输出通道数下k路Maxout需要的输入通道数是其它函数的k倍，这意味着神经元数目也需要变为k倍；但如果不考虑维持输出通道数的情况下，该激活函数又能将参数个数减少为原来的k倍。
- (9) 归一化（normalization）：这个是最近才出来的概念，对应的激活函数是SELU，主要思想是使样本分布自动归一化到零均值、单位方差的分布，从而稳定训练。在这之前，这种归一化的思想也被用于网络结构的设计，比如Batch Normalization。


Different optimizers (SGD, RMSprop, Momentum, Adagrad，Adam) 的区别

Batch vs SGD
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

Normalization
- batch normalization
- layer normalization
- instance normalization
- group normalization


# 3. ML模型类

## 3.1. Regression:
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

# 4. Convolution
Convolutional Block
- convolute (inner product) a filter on image in sliding window

CNN on images
- preserve, encode the spatial information
- translation-invariant (sliding window)

Receptive Field

Maxpooling: reduce computations by reducing the size of featuremap after pooling

Residual Network

Batch Normalization
- normalize the inputs of each layer
- BN保证每一层的输入分布稳定，可以使得训练加速，也可以帮助减少梯度消失和梯度爆炸的现象

Why small kernels are preferred?
- several small kernels than few larger ones to get the same receptive field and capture more spatial context, but with less parameters and computations
- more smaller kernels, more activations for more discriminative mapping being learned

矩阵乘法AxB, A的尺寸为mxn, B的尺寸为nxp, AxB的每个元素需要进行n次乘法和n-1次加法

基于二次准则函数的H-K算法


## 4.1. Clustering and EM:
K-means clustering (explain the algorithm in detail; whether it will converge, 收敛到global or local optimums;  how to stop)

EM算法是什么
GMM是什么，和Kmeans的关系


## 4.2. Decision Tree
How regression/classification DT split nodes?
How to prevent overfitting in DT?
How to do regularization in DT?


## 4.3. Ensemble Learning
Bagging: (Bootstrap Aggregating): reduce model variance through averaging
* build weak learners in parallel
  - Bootstraping (train separate weak learners on each Bootstrap sample)
  - Aggregating results: classification uses majority votes; regression used averaging.
- 和神经网络中dropout效果类似


Decision Stump
* Trees that only contain one decision for classification


Random Forest: homogenous ensemble learning of decision trees
* built using Bagging (each decision tree as a parallel estimator)
- pros: a whitebox model (easy to understand, interpretable, visualizable); not require normalization; 
- cons: need uncorrelated decision trees (Bootstrapping plays a key role in creating uncorrelated decision trees.)
will random forest help reduce bias or variance/why random forest can help reduce variance?


Boosting:
* build weak learners in serial/sequential to create a strong learner
- but adaptively re-weight training data prior training each new weak learner, in order to get a higher weight to previously misclassified examples


(discrete) Adaptive Boosting (AdaBoost)
* boosting the performance of decision trees for binary classification
* Algorithm:
    - (1) Each instance in the training dataset is weighted initially as w(i) = 1/N
    - (2) For m = 1 to M
        - Fit a classfier Gm(x) to the training data using weights w(i)
        - Compute error errorm = Σ w(i) * I(yi ≠ Gm(xi)) / Σ w(i) 
        - Compute αm = log((1 - errorm) / errorm)
        - Update w(i) = w(i) * exp(αm * I(yi ≠ Gm(xi)))
    - (3) Final prediction sign(Σ αm * Gm(x))
- pros: fast, simple; robust to overfit; can be used with text or numeric data
- cons: sensitive to noise and outlier; weak classifiers being too weak may lead to low margins and overfitting
```python
def compute_error(y, y_pred, w_i):
    '''
    Calculate the error rate of a weak classifier m. Arguments:
    y: actual target value
    y_pred: predicted value by weak classifier
    w_i: individual weights for each observation
    '''
    return (sum(w_i * (np.not_equal(y, y_pred)).astype(int))) / sum(w_i)

def compute_alpha(error):
    '''
    Calculate the weight of a weak classifier m in the majority vote of the final classifier. This is called
    alpha in chapter 10.1 of The Elements of Statistical Learning. Arguments:
    error: error rate from weak classifier m
    '''
    return np.log((1 - error) / error)

def update_weights(w_i, alpha, y, y_pred):
    ''' 
    Update individual weights w_i after a boosting iteration. Arguments:
    w_i: individual weights for each observation
    y: actual target value
    y_pred: predicted value by weak classifier  
    alpha: weight of weak classifier used to estimate y_pred
    '''  
    return w_i * np.exp(alpha * (np.not_equal(y, y_pred)).astype(int))
```


Gradient Boosted Decision Trees (GBDT):
  - Also known as gradient boosting, multiple additive regression trees, stochastic gradient boosting, gradient boosting machines
* New models are created to predict the residuals or errors of prior models and then added together to make the final prediction
- Built using Boosting (decision trees connected in series) to minimize the error of previous tree
- Decision trees in GBDT are not fit to the entire dataset. Each tree fits to the residuals from the previous one. As a result, the overall accuracy and robustness of the model gradually increase.
- Support both regression and classification predictive modeling problems
- pros: do not need bootstrapping, no correlated trees; no need to create subsamples from the dataset


XGBoost
* a library implemented GBDT and engineered for efficiency of compute time and memory resources
    - Execution Speed + Model Performance
* Three main forms of gradient boosting are supported:
    - (1) Gradient Boosting algorithm also called gradient boosting machine including the learning rate
    - (2) Stochastic Gradient Boosting with sub-sampling at the row, column and column per split levels
    - (3) Regularized Gradient Boosting with both L1 and L2 regularization
* system feature
    - Parallelization of tree construction using all of your CPU cores during training
    - Distributed Computing for training very large models using a cluster of machines
    - Out-of-Core Computing for very large datasets that don’t fit into memory
    - Cache Optimization of data structures and algorithm to make best use of hardware
* Algorithm Features
    - Sparse Aware implementation with automatic handling of missing data values
    - Block Structure to support the parallelization of tree construction
    - Continued Training so that you can further boost an already fitted model on new data


Light GBM


## 4.4. Generative Model
和Discrimitive模型比起来，Generative 更容易overfitting还是underfitting


Naïve Bayes的原理，基础假设是什么


Linear/normal discriminant analysis (LDA) vs Quadratic discriminant analysis (QDA)
- conditional probability density function P(x|y=0) and P(x|y=1) are normal distributions N(μ0, Σ0) and N(μ1, Σ1)
- Bayes optimal solution is to predict points as being from the second class if the log of the likelihood ratios is bigger than some threshold T: (x - μ0)Σ0(x - μ0) + ln|Σ0| - (x - μ1)Σ1(x - μ1) - ln|Σ1| > T  (QDA)
- LDA: assume Σ0=Σ1, dot(w, x) > c where w = pow(Σ, -1) * (μ1 - μ0) and c = dot(w, (μ1 + μ0) / 2)
    - the criterion of an input x being in a class y is purely a function of the linear combination of the known observations.
- LDA is supervised, PCA is unsupervised; both are linear transformations; PCA finds the directions of maximal variance, LDA finds a feature subspace that maximizes class separability.


## 4.5. Logistic Regression
logistic regression vs svm（我想这个主要是想问两者的loss的不同以及输出的不同，一个是概率输出一个是score）
- both solves classification; SVM can solve regression too.
- loss
- output

LR大部分面经集中在logloss和regularization

Support Vector Machine (SVM)
- a classifier defined by a separating hyperplane(decision boundary), where same distance from the boundary point of both classes
- kernel tricks: a method of using a linear classifier to solve a non-linear problem; kernel transforms linearly inseparable data to linearly separable ones by mapping them into higher-dimensional space.

- SVM is based on geometrical properties of data; logistic regression is statistical.
- SVM less vulnarable to overfitting

- output SVM as a probability: 如何让SVM输出分类概率 
    - sigmoid-fitting
    - SVM + Logistic Regression blending

## 4.6. 其他模型

Principal component analysis (PCA)
- create new uncorrelated variables that successively maximize variance by solving an eigenvalue/eigenvector problem.
- reduce the dimensionality of dataset, increase interpretability while minimize information loss
- pros: no need of prior; reduce overfitting (by reduce #variables in the dataset); visualizable
- cons: data standardization is a prerequisite; information loss

t-SNE
- t-Distributed Stochastic Neighbor Embedding is an unsupervised, non-linear technique primarily used for data exploration and visualizing high-dimensional data.
- t-SNE gives you a feel or intuition of how the data is arranged in a high-dimensional space.

UMAP
- Uniform Manifold Approximation and Projection is a novel manifold learning technique for dimension reduction. 
- UMAP is constructed from a theoretical framework based in Riemannian geometry and algebraic topology. The result is a practical scalable algorithm that applies to real world data.


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


# 5. Data Processing
Data Augmentation
- synthesize new data by modifying existing data
- resize, horizontal/vertical flip, rotate, add noise, deform

imbalanced data (long-tail data, skewed class data)
- change performance metric
    - Kappa/Cohen’s kappa: Classification accuracy normalized by the imbalance of the classes in the data.
- resampling to even up the class
- collect more data, generate synthetic samples
    - Synthetic Minority Oversampling Technique: SMOTE uses KNN to create new instances
- bias the model to pay more attention to minority class by penalty
- balanced bagging classifier
- train the model with major classes, fine tune with minor.

problem with high-dim classification
* Curse of Dimensionality: number of training examples we need to cover the space densely, exponential in the dimensionality of the problem; we will never get enough examples; also computational burden
    - manual feature selection; PCA; multidimensional scaling; locally linear embedding
* N grows exponentially with D
* solution
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


# 6. implementation & derivation
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


# 7. NLP/RNN相关

Variants of RNN
- LSTM, GRU, end-to-end network, memory network


LSTM的公式是什么
why use RNN/LSTM

LSTM
- special RNN, but capable of leanring long-term dependencies
- nature of remembering information for a long periods of time
- forget gate, input gate, output gate

limitation of RNN
- gradient vanishing (use LSTM)
- training is difficult

GRU
- Gated Recurrent Units，是循环神经网络的一种
- GRU只有两个门（update和reset），LSTM有三个门（forget，input，output），GRU直接将hidden state传给下一个单元，而LSTM用memory cell把hidden state包装起来


Attention
* self attention mechanism allows the inputs to interact with each other, find out who they should pay more attention to; outputs are aggregates of interactions and attention scores
    - why attention

```python
# x is an embedding vector of inputs
querys = x @ w_query
keys = x @ w_key
values = x @ w_value

attention_scores = softmax(querys @ keys.T, dim=-1)  # softmax for normalization
# scaled attention_scores for back-propagation gradient stability
# attention_scores = softmax(querys @ keys.T / sqrt(d), dim=-1)        
# where d is the dimension of query vector
weighted_values = values * attention_scores
output = weighted_values.sum(dim=0)
```
* cross attention

Transformer
- attention to Transformer
* Multi-Head?
* encoder/decoder part?


Language Model的原理，N-Gram Model
What’s CBOW and skip-gram?
什么是Word2Vec， loss function是什么， negative sampling是什么

# 8. CNN/CV相关

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


CNN的关键层有:
①输入层，对数据去均值，做data augmentation等工作
②卷积层，局部关联抽取feature
③激活层，非线性变化
④池化层，下采样
⑤全连接层，增加模型非线性
⑥高速通道，快速连接
⑦BN层，缓解梯度弥散


CNN的特点以及优势
- CNN使用范围是具有局部空间相关性的数据，比如图像，自然语言，语音
- 局部连接：可以提取局部特征。
- 权值共享：减少参数数量，因此降低训练难度（空间、时间消耗都少了）。可以完全共享，也可以局部共享（比如对人脸，眼睛鼻子嘴由于位置和样式相对固定，可以用和脸部不一样的卷积核）
- 降维：通过池化或卷积stride实现
- 多层次结构：将低层次的局部特征组合成为较高层次的特征。不同层级的特征可以对应不同任务


# 9. VAE, GANs
Auto-Encoder
- used to learn a compressed form of given data
- data denoising, dimensionality reduction, image reconstruction, image colorization
  
GAN
- generator + discriminator



# 10. Loss Function & Optimization

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


optimizer
1. Stochastic Gradient Descent (SGD)
2. SGD with Momentum (= mass × velocity, cannot instantaneously change direction)
3. SGD with Nesterov momentum
4. AdaGrad
5. RMSProp
6. Adam(adaptive moments)


# 11. Detection
FPN RPN

1-stage detection
2-stage detection

rcnn fast-rcnn faster-rcnn
传统的detection主流方法是DPM(Deformable parts models)， 在VOC2007上能到43%的mAP，虽然DPM和CNN看起来差别很大，但RBG大神说“Deformable Part Models are Convolutional Neural Networks”（http://arxiv.org/abs/1409.5403）

CNN流行之后，Szegedy做过将detection问题作为回归问题的尝试（Deep Neural Networks for Object Detection），但是效果差强人意，在VOC2007上mAP只有30.5%。既然回归方法效果不好，而CNN在分类问题上效果很好，那么为什么不把detection问题转化为分类问题呢？

RBG的RCNN使用region proposal（具体用的是Selective Search Koen van de Sande: Segmentation as Selective Search for Object Recognition）来得到有可能得到是object的若干（大概10^3量级）图像局部区域，然后把这些区域分别输入到CNN中，得到区域的feature，再在feature上加上分类器，判断feature对应的区域是属于具体某类object还是背景。当然，RBG还用了区域对应的feature做了针对boundingbox的回归，用来修正预测的boundingbox的位置。

RCNN在VOC2007上的mAP是58%左右。RCNN存在着重复计算的问题（proposal的region有几千个，多数都是互相重叠，重叠部分会被多次重复提取feature），于是RBG借鉴Kaiming He的SPP-net的思路单枪匹马搞出了Fast-RCNN，跟RCNN最大区别就是Fast-RCNN将proposal的region映射到CNN的最后一层conv layer的feature map上，这样一张图片只需要提取一次feature，大大提高了速度，也由于流程的整合以及其他原因，在VOC2007上的mAP也提高到了68%。

探索是无止境的。Fast-RCNN的速度瓶颈在Region proposal上，于是RBG和Kaiming He一帮人将Region proposal也交给CNN来做，提出了Faster-RCNN。Fater-RCNN中的region proposal netwrok实质是一个Fast-RCNN，这个Fast-RCNN输入的region proposal的是固定的（把一张图片划分成n*n个区域，每个区域给出9个不同ratio和scale的proposal），输出的是对输入的固定proposal是属于背景还是前景的判断和对齐位置的修正（regression）。Region proposal network的输出再输入第二个Fast-RCNN做更精细的分类和Boundingbox的位置修正。

Fater-RCNN速度更快了，而且用VGG net作为feature extractor时在VOC2007上mAP能到73%。个人觉得制约RCNN框架内的方法精度提升的瓶颈是将dectection问题转化成了对图片局部区域的分类问题后，不能充分利用图片局部object在整个图片中的context信息。

可能RBG也意识到了这一点，所以他最新的一篇文章YOLO（http://arxiv.org/abs/1506.02640）又回到了regression的方法下，这个方法效果很好，在VOC2007上mAP能到63.4%，而且速度非常快，能达到对视频的实时处理（油管视频：https://www.youtube.com/channel/UC7ev3hNVkx4DzZ3LO19oebg），虽然不如Fast-RCNN，但是比传统的实时方法精度提升了太多，而且我觉得还有提升空间。


Bounding-Box regression
- bounding box (x, y, w, h), x, y are center coordinates
- BB regression 先平移, 后尺度缩放


Selective Search
- (1)一种过分割手段，将图像分割成小区域 (1k~2k 个)
- (2)查看现有小区域，按照合并规则合并可能性最高的相邻两个区域。重复直到整张图像合并成一个区域位置
    优先合并以下四种区域:
    ①颜色（颜色直方图）相近的
    ②纹理（梯度直方图）相近的
    ③合并后总面积小的: 保证合并操作的尺度较为均匀，避免一个大区域陆续“吃掉”其他小区域 
    ④合并后, 总面积在其BBOX中所占比例大的： 保证合并后形状规则
- (3)输出所有曾经存在过的区域，所谓候选区域

非极大值抑制（NMS）
- 抑制不是极大值的元素，搜索局部的极大值。这个局部代表的是一个邻域，邻域有两个参数可变，一是邻域的维数，二是邻域的大小
- 在目标检测中用于提取分数最高的窗口
    (1)从最大概率矩形框F开始，分别判断A~E与F的重叠度IOU是否大于某个设定的阈值
    (2)假设B、D与F的重叠度超过阈值，那么就扔掉B、D；并标记第一个矩形框F，是我们保留下来的
    (3)从剩下的矩形框A、C、E中，选择概率最大的E，然后判断E与A、C的重叠度，重叠度大于一定的阈值，就扔掉；并标记E是我们保留下来的第二个矩形框

anchor
- 使用一个3*3的卷积核，在最后一个feature map上滑动，当滑动到特征图的某一个位置时，以当前滑动窗口中心为中心映射回原图的一个区域(注意 feature map 上的一个点是可以映射到原图的一个区域的，相当于感受野起的作用)，以原图上这个区域的中心对应一个尺度和长宽比，就是一个anchor了
- fast rcnn 使用3种尺度和3种长宽比（1:1；1:2；2:1），则在每一个滑动位置就有 3*3 = 9 个anchor



IOU:
2 cases:
- 2 points: x1 = 1 and x2 = 3, the distance is x2 - x1 = 2
- 2 pixels of index: i1 = 1 and i2 = 3, the segment from pixel i1 to i2 contains 3 pixels, l = i2 - i1 + 1

```python
def IOU(box1, box2): #[x1, y1, x2, y2], [x3, y3, x4, y4]

    # check if intersect
    if box1[2] < box2[0] or box1[0] > box2[2]: # check x, x2 < x3 | x1 > x4
        return 0
    if box1[3] < box2[1] or box1[1] > box2[3]: # check y
        return 0

    # find intersection
    x1, y1 = max(box1[0], box2[0]), max(box1[1], box2[1])
    x2, y2 = min(box1[2], box2[2]), min(box1[3], box2[3])
    i_area = (x2 - x1) * (y2 - y1)

    # find sum of areas
    b1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    b2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

    # iou = intersection / (sum_of_areas - intersection)
    return i_area / (b1_area + b2_area - i_area) 


import torch
import torchvision.ops.boxes as bops

box1 = torch.tensor([box1], dtype=torch.float)
box2 = torch.tensor([box2], dtype=torch.float)
iou = bops.box_iou(box1, box2)


# Vectorized IOU
def vec_IOU(boxes1, boxes2): # both [N, 4]
    assert(boxes1[:, 2:] > boxes1[:, :2]).all()
    assert(boxes2[:, 2:] > boxes2[:, :2]).all()

    area1 = (boxes1[:, 2] - boxes1[:, 0]) * (boxes1[:, 3] - boxes1[:, 1])
    area2 = (boxes2[:, 2] - boxes2[:, 0]) * (boxes2[:, 3] - boxes2[:, 1])

    # Intersection
    top_left = np.maximum(boxes1[:, :2], boxes2[:, :2])      # [[x, y]]
    bottom_right = np.minimum(boxes1[:, 2:], boxes2[:, 2:])  # [[x, y]]
    wh = bottom_right - top_left
    
    # clip: if boxes not overlap then make it zero
    intersection = wh[:, 0].clip(0) * wh[:, 1].clip(0)

    # Union 
    union = area1 + area2 - intersection

    return intersection / union
```

       
# 12. 项目经验类
训练好的模型在现实中不work

深度学习中有什么加快收敛/降低训练难度的方法?
- 瓶颈结构 bottleneck
- 残差 residual block
- 学习率、步长、动量
- 优化方法
- 预训练

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



# 13. 关于准备考ML 概念的面试的一些建议
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


Gradient descent: an optimization algorithm used to find the values of parameters of a function that minimizes a cost function. It is to be used when the parameters cannot be found analytically.

  3）Gradient descent 解释原理，什么是 mini batch GD, stachastic GD, Adam
  4）NN 里面 gradient descent怎么计算，是convex的吗，能保证最优解吗，（不能保证）怎么解决
  5）Regression 用什么loss? Classification 用什么loss， 多分类呢？分类的loss是convex的吗
  7）Random forest hyperparameter 怎么选
  8）Validation set 都用来干嘛


MLE、MAP和贝叶斯估计
MLE，MAP，EM 和 point estimation 之间的关系是怎样的？


IOU、NMS
SVM的优缺点
随机森林的训练过程
优化方法SGD、Batch GD、Adadelta、Momentum对超参数的敏感程度
CNN中feature map维度计算、图中每一个特征点在原图的感受野大小
Segmatch


模型压缩与加速 mobilenet v1、mobilenet v2、shufflenet
MobileNet V2

目标分割、目标检测（one stage、two stage），YOLO三代的发展，小目标检测
Mask-RCNN vs YOLO


# 14. Pytorch Example
```python
import torch
import math

# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = torch.sin(x)

# Prepare the input tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)

# Use the nn package to define our model and loss function.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)
loss_fn = torch.nn.MSELoss(reduction='sum')

# Use the optim package to define an Optimizer that will update the weights of
# the model for us. Here we will use RMSprop; the optim package contains many other
# optimization algorithms. The first argument to the RMSprop constructor tells the
# optimizer which Tensors it should update.
learning_rate = 1e-3
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
for t in range(2000):
    # Forward pass: compute predicted y by passing x to the model.
    y_pred = model(xx)

    # Compute and print loss.
    loss = loss_fn(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())

    # Before the backward pass, use the optimizer object to zero all of the
    # gradients for the variables it will update (which are the learnable
    # weights of the model). This is because by default, gradients are
    # accumulated in buffers (i.e, not overwritten) whenever .backward()
    # is called. Checkout docs of torch.autograd.backward for more details.
    optimizer.zero_grad()

    # Backward pass: compute gradient of the loss with respect to model parameters
    loss.backward()

    # Calling the step function on an Optimizer makes an update to its parameters
    optimizer.step()
```

Pytorch Inference
```python
torch.set_grad_enabled(False)

model.eval()

with torch.no_grad():
    ...
```


# ToDo List
SVM 
- hyperplane dimension NxM?
- computational trick


Faster RCNN vs MaskRCNN
