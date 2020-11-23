from karateclub.dataset import GraphReader
import networkx as nx
import matplotlib.pyplot as plt

reader = GraphReader("twitch")

engb = nx.read_gml('L:\Github Repos\playground\TwitchSocialNetworks\TwitchDataENGB.gml')
graph = nx.path_graph(engb)

nx.draw(graph)
plt.draw()  # pyplot draw()



# y = reader.get_target()
# from karateclub import Diff2Vec

# model = Diff2Vec(diffusion_number=2, diffusion_cover=20, dimensions=16)
# model.fit(graph)
# X = model.get_embedding()

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# from sklearn.metrics import roc_auc_score
# from sklearn.linear_model import LogisticRegression

# downstream_model = LogisticRegression(random_state=0).fit(X_train, y_train)
# y_hat = downstream_model.predict_proba(X_test)[:, 1]
# auc = roc_auc_score(y_test, y_hat)
# print('AUC: {:.4f}'.format(auc))