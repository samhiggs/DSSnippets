# Python Snippets For Data Science

## COVID19: Wear Mask, Keep distance, Stay Home, Stay Safe

**Thank you for using these snippets, hope they make your coding faster, welcome your feedback!!!**


<h3>
 - <span style="color:#8E0000;">Classification Snippets included</span>  <br>
 - Clustering, Dimensionality Reduction, Association Rules(Recommender Systems),Deep Learning, Reinforcement Learning etc.. will come soon.
</h3>
 
<h2 style="color:#8E0000;">  

[Get all great Python and Azure extension here](https://marketplace.visualstudio.com/items?itemName=SunilYadav.dspysnippets)
</h2>

<ol style="color:#8E0000; font-weight:bold;font-size:25px;">TRICKS &#x1F514;
<li style="color:#8E0000; font-weight:bold;font-size:22px;">For Machine learning start type `ml` list of available snippets will appear then navigate to desired snippet</li>
</ol>

## Snippets Naming Convention<sup>*<sup>

- Machine Learning (Using [scikit-learn](https://scikit-learn.org/stable/)) for most of snippets
  - Supervised Machine Learning
    - Snippets will start with `ml`
    - If it is for `Regression` then `-r` suffix will be added
    - If it is for `Classification` then `-c` suffix will be added
    - Final will approach for example:
      - `-slr` ==> Linear Regression - Single Variable
      - `-mlr` ==> Linear Regression - Multiple Variables
    - -nb will create a notebook snippet, no nb will generate python script

**So for simle linear regression snippet will be `ml-r-slr`. See available snippets below**

- Pandas
  - Snippets will start with `p`
- Cell Creation in Python file
  - Snippets will start with `c`

*List of available snippets:*

-----------------------------------------------------------------------------------------------------------

## Machine Learning Snippets

### Regression

| Snippet Key | Description                   |
| ----------- | ----------------------------- |
| ml-r-slr-nb    | Simple Linear Regression      |
| ml-r-mlr-nb    | Multiple Linear Regression    |
| ml-r-ply-nb    | Polynomial Regression         |
| ml-r-svr-nb    | SVM Regressor with RBF kernel |
| ml-r-dtr-nb    | Decision Tree Regressor       |
| ml-r-rfr-nb    | Random Forest Regressor       |

### Classification

| Snippet Key | Description                                 |
| ----------- | ------------------------------------------- |
| ml-c-lr-nb     | Logistic Regression Classification          |
| ml-c-knn-nb    | K-Nearest Neighbors (K-NN) Classification   |
| ml-c-svm-nb    | Support Vector Machine (SVM) Classification |
| ml-c-ksvm-nb   | Kernel SVM Classification                   |
| ml-c-gnb-nb    | Gaussian Naive Bayes                        |
| ml-c-mnb-nb    | Multinomial Naive Bayes                     |
| ml-c-dtc-nb    | Decision Tree Classification                |
| ml-c-rfc-nb    | Random Forest Classification                |
| ml-c-txt-nb    | Random Forest Text Classification                |

## [Pandas Dataframe](https://pandas.pydata.org/pandas-docs/stable/index.html) snippets

| Snippet Key | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| pd          | Import `numpy`, `pandas` and create a data frame from csv file |
| pp          | Above + `matplotlib.pyplot`                                    |
| ps          | Above + `seborn`                                               |

## [Python File/Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py) snippets

| Snippet Key | Description                           |
| ----------- | ------------------------------------- |
| c           | Create Cell (# %%)                    |
| cc          | Create Markdown cell(# %% [markdown]) |

## Miscelanious

| Snippet Key    | Description |
| -----------    | ----------- |
| r              | Ref Line    |
| ds-c           | generate classification dataset |
| ds-r           | generate regression dataset |

-----------------------------------------------------------------------------------------------------------

## Requirements

You must be in python file.

## Extension Settings

NA

## Known Issues

NA

## Release Notes

### 0.0.0.3-4

Adding snippets for [Python File/Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py) snippets

### 0.0.0.2

Message added in readme file

### 0.0.0.1

Initial release of Python Snippets For Data Science

-----------------------------------------------------------------------------------------------------------
Credits:

- <sup>*</sup>Many (not all) Naming conventions and code flow are inspired from [udemy](https://www.udemy.com/) course [Machine Learning A-Z™: Hands-On Python & R In Data Science] (https://www.udemy.com/course/machinelearning/), as I learned from it found very intuitive  - Though we don't have any business deal ;)
