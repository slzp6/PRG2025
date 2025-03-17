""" p6_23.py """

#
# Make sure to install pycaret
# https://pycaret.org/
#

# pylint: disable=pointless-string-statement
'''
from pycaret.classification import *
from pycaret.datasets import get_data

data = get_data('iris')

s = ClassificationExperiment()
s.setup(data, target='species', session_id=42)

best = s.compare_models()

s.evaluate_model(best)

pred_holdout = s.predict_model(best)

new_data = data.copy().drop('species', axis=1)
predictions = s.predict_model(best, data=new_data)

s.save_model(best, 'p6_23_best_pipeline_oop')

'''
