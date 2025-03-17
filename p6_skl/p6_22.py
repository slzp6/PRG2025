""" p6_22.py """

#
# Make sure to install pycaret
# https://pycaret.org/
#

# pylint: disable=pointless-string-statement
'''

from pycaret.classification import *
from pycaret.datasets import get_data

data = get_data('iris')

s = setup(data, target='species', session_id=42)

best = compare_models()

evaluate_model(best)

pred_holdout = predict_model(best)

new_data = data.copy().drop('species', axis=1)
predictions = predict_model(best, data=new_data)

save_model(best, 'p6_22_best_pipeline_func')

'''
