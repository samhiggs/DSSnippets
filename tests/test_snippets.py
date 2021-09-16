import json
from sklearn.datasets import make_classification
import pandas as pd
from pathlib import Path
import shutil
import pytest

snippet_names = ['Pandas with Pyplot', 'Pandas with Sns', 'Create Pandas Dataframe', 'Create cell', 'Create Markdown Cell', 'Ref Line', 'Make Classification Dataset', 'Make Regression Dataset', 'Simple Linear Regression NB', 'Multiple Linear Regression NB', 'Polynomial Regression NB', 'SVM Regressor with RBF kernel NB', 'Decision Tree Regressor NB', 'Random Forest Regressor NB', 'Logistic Regression Classification NB', 'K-Nearest Neighbors (K-NN) Classification NB', 'Support Vector Machine (SVM) Classification NB', 'Kernel SVM Classification NB', 'Gaussian Naive Bayes NB', 'Multinomial Naive Bayes NB', 'Decision Tree Classification NB', 'Random Forest Classification NB', 'Simple Linear Regression ', 'Multiple Linear Regression', 'Polynomial Regression', 'SVM Regressor with RBF kernel', 'Decision Tree Regressor', 'Random Forest Regressor', 'Logistic Regression Classification', 'K-Nearest Neighbors (K-NN) Classification', 'Support Vector Machine (SVM) Classification', 'Kernel SVM Classification', 'Gaussian Naive Bayes', 'Multinomial Naive Bayes', 'Decision Tree Classification', 'Random Forest Classification', 'Text Classification']

data_path = 'tests/sample_data.csv'
def generate_data():
    if not Path(data_path).is_file(): 
        X,y = make_classification(
                    n_samples = 1000,
                    n_features = 5,
                    n_informative = 5,
                    n_redundant = 0,
                    n_classes = 2,
                )
        df = pd.DataFrame(data=X)
        df['label'] = y
        df.to_csv(data_path, index=False)

def parse_json_code(json_str, key):
    code_list = json_str[key]['body']
    code_str = '\n'.join(code_list) 
    code_str = code_str.replace("'$1'", f"'{data_path}'")
    return code_str

def test_valid_json():
    """Checks that the json was loaded correctly and dict contains correct keys"""
    with open('snippets/snippets.code-snippets') as json_file:
        data = json.load(json_file)
    assert set(snippet_names) == set(data.keys())

def test_rfc_snippet():
    generate_data()
    with open('snippets/snippets.code-snippets') as json_file:
        data = json.load(json_file)
    code_str = parse_json_code(data, 'Random Forest Classification')
    exec(code_str)
    assert Path('model/classifier.joblib').is_file()
    shutil.rmtree('model')


"""
If you want to redirect stdout for more granular tests:
"""
# from cStringIO import StringIO
# old_stdout = sys.stdout
# redirected_output = sys.stdout = StringIO()
# execfile('rf_text.py')
# sys.stdout = old_stdout

# print redirected_output.getvalue()