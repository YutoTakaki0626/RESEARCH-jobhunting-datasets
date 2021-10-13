import os
import glob

import pandas as pd
import joblib

def dumpJoblib(fileName, obj):
    with open(fileName, mode="wb") as f:
        joblib.dump(obj, f, compress=3)
        
def loadJoblib(fileName):
    with open(fileName, mode="rb") as f:
        return joblib.load(f)

df = loadJoblib('Desktop/RESEARCH-jobhunting-datasets/data_label/00000_00499.joblib')
texts = df['tweet_full_text'].tolist()
df['label'] = 0

for i in range(500):
    print('-' ** 30)
    print(f'□　□　□ 現在{i}個目の作業です！！')
    print(f'ツイート本文：\n {texts[i]}')
    lbl = int(input('どのラベルに分類しますか'))
    df[i, 'label'] = lbl
    print('-' * 30)
