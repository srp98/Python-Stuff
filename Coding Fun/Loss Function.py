from keras.losses import binary_crossentropy, cosine_proximity
from keras import backend as K
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math

# Loss Function Calculation
y = K.variable(np.array([[1], [0], [1], [1]]))
y_pred = K.variable(np.array([[0.5], [0.6], [0.7], [0.8]]))
err = K.eval(binary_crossentropy(y, y_pred))
cp = K.eval(cosine_proximity(y, y_pred))

print(err)
print(cp)
print(y.shape)
print(y_pred.shape)

err = np.reshape(err, (4, 1))
cp = np.reshape(cp, (4, 1))

print(err.shape)
print(cp.shape)

# Cosine Similarity, Tf-idf
documents = {'the sky is blue',
             'the sun is bright',
             'the sun in the sky is bright',
             'we can see the shining sun, the bright sun'}

tf_idf_vectorizer = TfidfVectorizer()
tf_idf_matrix = tf_idf_vectorizer.fit_transform(documents)
print(tf_idf_matrix, tf_idf_matrix.shape)
print(cosine_similarity(tf_idf_matrix[0:1], tf_idf_matrix))

# Example Cosine_Sim
cos_sim = 0.52305744
angle_in_radians = math.acos(cos_sim)
print(math.degrees(angle_in_radians))
