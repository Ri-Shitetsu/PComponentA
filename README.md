# PComponentA
A tool for principal component analysis

## Installation
``` sh
pip install PComponentA
```
This programme utilizes NumPy, Pandas and Matplotlib <br>
Please make sure you have them installed in your environment

# Usage
``` sh
% PComponentA [path_to_dataset.csv] [index_of_label_column] [principal_component_1] [principal_component_2]
```
Example : Plot a graph of principal component 1 against principal component 2 <br>
Dataset used : Iris Species (https://www.kaggle.com/datasets/uciml/iris) <br>
``` sh
% PcomponentA iris.csv -1 1 2
```
The programme will print the total number of principal components of the dataset and return a pop-up window of the graph
``` sh
Number of components : 2
```
![Sample](https://github.com/Ri-Shitetsu/PComponentA/blob/main/sample.png)



