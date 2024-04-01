# Results

## 25/03/2024

### NB - 40k size

#### all: 

{'accuracy': 0.904625, 'f1': 0.9044251932117491, 'precision': 0.9045102173212911, 'recall': 0.904625, 'confusion_matrix': array([[1817,   67,  111,   52],
       [  21, 1924,   12,   10],
       [  59,   17, 1740,  170],
       [  77,   21,  146, 1756]]), 'best_params': {}}

### text and tokens:

{'accuracy': 0.90625, 'f1': 0.9060497362386052, 'precision': 0.9060131772958145, 'recall': 0.90625, 'confusion_matrix': array([[1825,   65,  109,   48],
       [  24, 1923,    9,   11],
       [  62,   13, 1745,  166],
       [  87,   18,  138, 1757]]), 'best_params': {}}

### entities:

{'accuracy': 0.301625, 'f1': 0.20236541079088105, 'precision': 0.5700431432380205, 'recall': 0.301625, 'confusion_matrix': array([[  33, 1972,   10,   32],
       [   1, 1931,    8,   27],
       [   4, 1807,   79,   96],
       [   7, 1581,   42,  370]]), 'best_params': {}}

### Embeds:

{'accuracy': 0.900375, 'f1': 0.9001754048431471, 'precision': 0.9002720823557113, 'recall': 0.900375, 'confusion_matrix': array([[1814,   68,  111,   54],
       [  20, 1922,   12,   13],
       [  64,   20, 1721,  181],
       [  73,   21,  160, 1746]]), 'best_params': {}}

### no ner:

{'accuracy': 0.903875, 'f1': 0.9036569269056173, 'precision': 0.9037067168247837, 'recall': 0.903875, 'confusion_matrix': array([[1816,   68,  111,   52],
       [  21, 1924,   12,   10],
       [  61,   17, 1737,  171],
       [  80,   21,  145, 1754]]), 'best_params': {}}


## 27/03/2024

### NB - 40k

#### All features

{'accuracy': 0.894625, 'f1': 0.8943349932664348, 'precision': 0.894309369030074, 'recall': 0.894625, 'confusion_matrix': array([[1819,   83,  100,   45],
       [  22, 1920,   13,   12],
       [  63,   18, 1699,  206],
       [  84,   19,  178, 1719]]), 'best_params': {}, 'time': 34.89687442779541}

#### text and tokens

{'accuracy': 0.89675, 'f1': 0.8964542874845637, 'precision': 0.8964006023298475, 'recall': 0.89675, 'confusion_matrix': array([[1820,   82,  101,   44],
       [  22, 1920,   13,   12],
       [  66,   17, 1716,  187],
       [  94,   16,  172, 1718]]), 'best_params': {}, 'time': 6.520312070846558}

#### entities

{'accuracy': 0.298375, 'f1': 0.19730812003999837, 'precision': 0.5184803674947036, 'recall': 0.298375, 'confusion_matrix': array([[  38, 1961,   16,   32],
       [   4, 1922,    7,   34],
       [   4, 1820,   52,  110],
       [   8, 1567,   50,  375]]), 'best_params': {}, 'time': 0.7184696197509766}

#### embeddings

{'accuracy': 0.89175, 'f1': 0.8914349845519445, 'precision': 0.891388269185095, 'recall': 0.89175, 'confusion_matrix': array([[1813,   84,  101,   49],
       [  26, 1916,   16,    9],
       [  66,   19, 1683,  218],
       [  83,   23,  172, 1722]]), 'best_params': {}, 'time': 26.22289800643921}

#### no er

{'accuracy': 0.895, 'f1': 0.894707443184342, 'precision': 0.8946807730938828, 'recall': 0.895, 'confusion_matrix': array([[1819,   83,  101,   44],
       [  23, 1920,   14,   10],
       [  63,   18, 1702,  203],
       [  85,   19,  177, 1719]]), 'best_params': {}, 'time': 33.66146731376648}


### LR

#### all features

{'accuracy': 0.89675, 'f1': 0.896433635274754, 'precision': 0.8964773276887752, 'recall': 0.89675, 'confusion_matrix': array([[1809,   81,   95,   62],
       [  21, 1921,   12,   13],
       [  73,   17, 1690,  206],
       [  79,   21,  146, 1754]]), 'best_params': {'classifier__C': 0.1, 'classifier__penalty': 'l2', 'classifier__solver': 'liblinear'}, 'time': 17979.420502901077}

#### text and tokens

{'accuracy': 0.892875, 'f1': 0.8925242560296233, 'precision': 0.8926486116935399, 'recall': 0.892875, 'confusion_matrix': array([[1806,   82,   97,   62],
       [  22, 1918,   13,   14],
       [  69,   23, 1675,  219],
       [  76,   29,  151, 1744]]), 'best_params': {'classifier__C': 0.1, 'classifier__penalty': 'l2', 'classifier__solver': 'liblinear'}, 'time': 13111.028271913528}

#### entities

{'accuracy': 0.29925, 'f1': 0.19864595577564048, 'precision': 0.5014962276186938, 'recall': 0.29925, 'confusion_matrix': array([[  41, 1961,   13,   32],
       [   4, 1920,    7,   36],
       [   9, 1820,   47,  110],
       [  14, 1562,   38,  386]]), 'best_params': {'classifier__C': 10.0, 'classifier__penalty': 'l1', 'classifier__solver': 'liblinear'}, 'time': 1789.4881656169891}

#### embeddings

{'accuracy': 0.89525, 'f1': 0.894914149916059, 'precision': 0.8950304127240184, 'recall': 0.89525, 'confusion_matrix': array([[1802,   85,   95,   65],
       [  19, 1923,   11,   14],
       [  72,   17, 1686,  211],
       [  78,   22,  149, 1751]]), 'best_params': {'classifier__C': 0.1, 'classifier__penalty': 'l2', 'classifier__solver': 'liblinear'}, 'time': 11989.5702521801}

#### no ner

{'accuracy': 0.89675, 'f1': 0.8964505816391909, 'precision': 0.8965493900613543, 'recall': 0.89675, 'confusion_matrix': array([[1804,   80,   94,   69],
       [  21, 1923,   11,   12],
       [  72,   16, 1691,  207],
       [  78,   19,  147, 1756]]), 'best_params': {'classifier__C': 0.1, 'classifier__penalty': 'l2', 'classifier__solver': 'liblinear'}, 'time': 17553.760464668274}

### dtc

#### all features

{'accuracy': 0.772125, 'f1': 0.7719130635750178, 'precision': 0.7717283971404898, 'recall': 0.772125, 'confusion_matrix': array([[1610,  120,  180,  137],
       [ 120, 1705,   62,   80],
       [ 165,   73, 1419,  329],
       [ 144,   97,  316, 1443]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 2}, 'time': 937.1630198955536}

#### text and tokens

{'accuracy': 0.76475, 'f1': 0.76415846431765, 'precision': 0.7638631278529681, 'recall': 0.76475, 'confusion_matrix': array([[1591,  139,  155,  162],
       [ 107, 1717,   47,   96],
       [ 183,   84, 1382,  337],
       [ 156,   96,  320, 1428]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 5}, 'time': 398.36433386802673}

#### entities

{'accuracy': 0.297875, 'f1': 0.19664970603438572, 'precision': 0.48558346253784396, 'recall': 0.297875, 'confusion_matrix': array([[  41, 1961,   13,   32],
       [   4, 1922,    7,   34],
       [  10, 1820,   48,  108],
       [  17, 1565,   46,  372]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 2}, 'time': 1450.9381716251373}

#### embeddings

{'accuracy': 0.77, 'f1': 0.7701868109659573, 'precision': 0.7704857385740805, 'recall': 0.77, 'confusion_matrix': array([[1573,  126,  181,  167],
       [ 106, 1683,   89,   89],
       [ 184,   62, 1421,  319],
       [ 148,   84,  285, 1483]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 2}, 'time': 480.0716848373413}

#### no ner

{'accuracy': 0.77, 'f1': 0.7698793496446737, 'precision': 0.7698128318506936, 'recall': 0.77, 'confusion_matrix': array([[1590,  124,  175,  158],
       [ 105, 1713,   67,   82],
       [ 184,   80, 1404,  318],
       [ 133,   78,  336, 1453]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 2}, 'time': 882.4388146400452}

### rf

#### all features

{'accuracy': 0.86, 'f1': 0.8595654554842549, 'precision': 0.8599864252186806, 'recall': 0.86, 'confusion_matrix': array([[1735,  109,  112,   91],
       [  20, 1879,   25,   43],
       [  80,   36, 1634,  236],
       [  92,   70,  206, 1632]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 10, 'classifier__n_estimators': 300}, 'time': 8972.01698923111}

#### text tokens

{'accuracy': 0.86575, 'f1': 0.8653287278615654, 'precision': 0.8656051992489596, 'recall': 0.86575, 'confusion_matrix': array([[1751,   98,  109,   89],
       [  18, 1882,   24,   43],
       [  73,   33, 1662,  218],
       [ 100,   70,  199, 1631]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 10, 'classifier__n_estimators': 300}, 'time': 7141.373013019562}

#### entities

{'accuracy': 0.298625, 'f1': 0.19765672068204593, 'precision': 0.5087604745125152, 'recall': 0.298625, 'confusion_matrix': array([[  39, 1961,   14,   33],
       [   4, 1922,    7,   34],
       [   5, 1820,   51,  110],
       [  12, 1565,   46,  377]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 30, 'classifier__n_estimators': 100}, 'time': 26844.983500003815}


#### embeddings

{'accuracy': 0.856, 'f1': 0.8556104945609683, 'precision': 0.8560576018240348, 'recall': 0.856, 'confusion_matrix': array([[1714,  115,  116,  102],
       [  25, 1868,   21,   53],
       [  84,   34, 1633,  235],
       [  99,   67,  201, 1633]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 5, 'classifier__n_estimators': 300}, 'time': 5412.190613269806}

#### no ner

{'accuracy': 0.8595, 'f1': 0.8590878348200686, 'precision': 0.859477692828876, 'recall': 0.8595, 'confusion_matrix': array([[1733,  113,  107,   94],
       [  26, 1870,   24,   47],
       [  79,   38, 1639,  230],
       [  94,   70,  202, 1634]]), 'best_params': {'classifier__max_depth': None, 'classifier__min_samples_split': 5, 'classifier__n_estimators': 300}, 'time': 8259.034624576569}

### SVM

#### all features

{'accuracy': 0.8955, 'f1': 0.8952096290820164, 'precision': 0.8951712201691846, 'recall': 0.8955, 'confusion_matrix': array([[1815,   78,  100,   54],
       [  20, 1918,   15,   14],
       [  68,   19, 1698,  201],
       [  85,   23,  159, 1733]]), 'best_params': {'classifier__C': 10.0, 'classifier__kernel': 'rbf'}, 'time': 86679.54444026947}

#### text and tokens

{'accuracy': 0.894125, 'f1': 0.8938188057959462, 'precision': 0.8938285598035013, 'recall': 0.894125, 'confusion_matrix': array([[1809,   83,  102,   53],
       [  26, 1914,   15,   12],
       [  62,   20, 1707,  197],
       [  84,   30,  163, 1723]]), 'best_params': {'classifier__C': 10.0, 'classifier__kernel': 'rbf'}, 'time': 46512.35917901993}

#### entities

{'accuracy': 0.297875, 'f1': 0.19663690102220488, 'precision': 0.48972862072319195, 'recall': 0.297875, 'confusion_matrix': array([[  41, 1961,   13,   32],
       [   4, 1922,    7,   34],
       [  10, 1820,   48,  108],
       [  15, 1567,   46,  372]]), 'best_params': {'classifier__C': 1.0, 'classifier__kernel': 'linear'}, 'time': 8856.187222480774}

#### embeddings

{'accuracy': 0.8965, 'f1': 0.896255856655611, 'precision': 0.8964996935618826, 'recall': 0.8965, 'confusion_matrix': array([[1810,   77,   97,   63],
       [  18, 1918,   13,   18],
       [  67,   16, 1681,  222],
       [  76,   21,  140, 1763]]), 'best_params': {'classifier__C': 1.0, 'classifier__kernel': 'rbf'}, 'time': 37852.37515950203}

#### no ner

{'accuracy': 0.89525, 'f1': 0.895001463911527, 'precision': 0.8949747612660592, 'recall': 0.89525, 'confusion_matrix': array([[1812,   78,  100,   57],
       [  22, 1916,   15,   14],
       [  67,   16, 1698,  205],
       [  87,   19,  158, 1736]]), 'best_params': {'classifier__C': 10.0, 'classifier__kernel': 'rbf'}, 'time': 84298.38023805618}

### XGB

#### all features

{'accuracy': 0.879875, 'f1': 0.8796957852986587, 'precision': 0.8798308810890988, 'recall': 0.879875, 'confusion_matrix': array([[1779,   86,  107,   75],
       [  31, 1878,   27,   31],
       [  77,   20, 1669,  220],
       [  86,   43,  158, 1713]]), 'best_params': {'classifier__max_depth': 3, 'classifier__n_estimators': 300}, 'time': 2173.538975954056}

#### text and tokens

{'accuracy': 0.889875, 'f1': 0.8896889433718994, 'precision': 0.8896829855461148, 'recall': 0.889875, 'confusion_matrix': array([[1809,   75,   98,   65],
       [  31, 1889,   22,   25],
       [  78,   17, 1701,  190],
       [  74,   43,  163, 1720]]), 'best_params': {'classifier__max_depth': 9, 'classifier__n_estimators': 300}, 'time': 1788.5012366771698}

#### entities

{'accuracy': 0.283, 'f1': 0.1693506519156022, 'precision': 0.40631212870134764, 'recall': 0.283, 'confusion_matrix': array([[   9, 2000,   10,   28],
       [   0, 1932,    5,   30],
       [   3, 1869,   17,   97],
       [   9, 1654,   31,  306]]), 'best_params': {'classifier__max_depth': 7, 'classifier__n_estimators': 200}, 'time': 309.3082902431488}

#### embeddings

{'accuracy': 0.879875, 'f1': 0.8797589184132585, 'precision': 0.8800661984682107, 'recall': 0.879875, 'confusion_matrix': array([[1768,   84,  114,   81],
       [  30, 1875,   26,   36],
       [  74,   26, 1676,  210],
       [  78,   40,  162, 1720]]), 'best_params': {'classifier__max_depth': 3, 'classifier__n_estimators': 300}, 'time': 640.9990811347961}

#### no ner

{'accuracy': 0.879375, 'f1': 0.8793133841927336, 'precision': 0.879578101654579, 'recall': 0.879375, 'confusion_matrix': array([[1768,   82,  107,   90],
       [  32, 1868,   28,   39],
       [  75,   22, 1683,  206],
       [  87,   38,  159, 1716]]), 'best_params': {'classifier__max_depth': 3, 'classifier__n_estimators': 300}, 'time': 1864.937325000763}

### Gradient Boosting

#### all features

{'accuracy': 0.889375, 'f1': 0.8893318724844647, 'precision': 0.8895746440883865, 'recall': 0.889375, 'confusion_matrix': array([[1793,   73,  114,   67],
       [  30, 1889,   23,   25],
       [  65,   16, 1688,  217],
       [  81,   23,  151, 1745]]), 'best_params': {'classifier__learning_rate': 0.5, 'classifier__max_depth': 7, 'classifier__n_estimators': 200}, 'time': 38298.37958574295}

#### text and tokens

{'accuracy': 0.882375, 'f1': 0.8824304083678229, 'precision': 0.8826802234037825, 'recall': 0.882375, 'confusion_matrix': array([[1787,   76,  111,   73],
       [  34, 1865,   22,   46],
       [  74,   17, 1692,  203],
       [  81,   29,  175, 1715]]), 'best_params': {'classifier__learning_rate': 0.5, 'classifier__max_depth': 7, 'classifier__n_estimators': 200}, 'time': 21522.156162261963}

#### entities

{'accuracy': 0.287125, 'f1': 0.1776619746958957, 'precision': 0.46855574898943847, 'recall': 0.287125, 'confusion_matrix': array([[  19, 1989,   11,   28],
       [   4, 1926,    5,   32],
       [   4, 1853,   28,  101],
       [   6, 1637,   33,  324]]), 'best_params': {'classifier__learning_rate': 0.5, 'classifier__max_depth': 7, 'classifier__n_estimators': 200}, 'time': 3111.5610868930817}


