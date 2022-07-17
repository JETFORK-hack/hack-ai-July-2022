"""
WSGI config for hackathon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

application = get_wsgi_application()



import os
from catboost import CatBoostClassifier
import pandas as pd
import fasttext
import nmslib
import razdel
import joblib, pickle
from hackathon import settings

# папка с необходимыми файлами для обучения модели
path = os.path.join(settings.BASE_DIR, 'eprf/ml/')

russian_stopwords = open(os.path.join(path, 'stopwords-ru.txt'), 'r').read().split('\n')
prod_name_clf = joblib.load(os.path.join(path, 'product_group.pkl'))
anomaly_detector = CatBoostClassifier()
anomaly_detector.load_model(os.path.join(path, 'anomaly_detector.model'))
reg_clf = fasttext.load_model(os.path.join(path, 'reglament_predictor.model'))
ved_thes = pd.read_csv(os.path.join(settings.BASE_DIR, 'resources', 'veds', 'ved_dict.csv'), sep=';')

for code_col in ["GRUPPA", "TOV_POZ", "SUB_POZ", "VED", "RAZDEL"]:
    ved_thes.loc[ved_thes[code_col].notna(), code_col] = \
        ved_thes.loc[ved_thes[code_col].notna(), code_col].astype(int).astype(str)
with open(os.path.join(path, 'ved_dict.pickle'), "rb") as handle:
    ved_dict = pickle.load(handle)

pmi_hist = pd.read_csv(os.path.join(path, 'pmi_features.csv'), sep=';')
pmi_hist[pmi_hist.columns[:5]] = pmi_hist[pmi_hist.columns[:5]].astype(str)
index = nmslib.init(method='napp', space='cosinesimil')
index.loadIndex(os.path.join(path, 'index_ved'), load_data=True)
indexed_data_dict = joblib.load(os.path.join(path, 'index_map.pkl'))
ft_model_v2 = fasttext.load_model(os.path.join(path, 'fb_model_v2.bin'))


def tokenize_with_razdel(text):
    tokens = [token.text for token in razdel.tokenize(text)]

    return tokens


vectorizer = joblib.load(os.path.join(path, 'vectorizer.pkl'))

IDXS = ["Номер продукции"]
FEATURES = ["Технические регламенты", "Группа продукции", "RAZDEL", "GRUPPA", "TOV_POZ"]

map_path = os.path.join(settings.BASE_DIR, 'resources/datasets/', 'db_file.csv')
df_map = pd.read_csv(map_path, sep=";").drop("Unnamed: 0", axis=1)
df_map[["product_number", "GRUPPA", "TOV_POZ", "SUB_POZ"]] = \
    df_map[["product_number", "GRUPPA", "TOV_POZ", "SUB_POZ"]].astype(str)
df_map["Аномалия"] = df_map["outlier"].replace(0, "Нет").replace(1, "Да")
