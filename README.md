# Master Thesis
This repository represents the codebase for Machine Learning and Data Science experiments related to my master thesis.

## Instructions

#### 1. Installing Dependencies

##### Global installation
If you want to install the dependencies globally or are already sourced into your desired environment.
```
conda create pyml36 librosa
```
##### Anaconda
If you are using Anaconda as environment manager for Python.

###### CPU-Only
```
conda create pytorch torchvision cpuonly -c pytorch
```

###### Cuda accelerated (recommended)

```
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
```

#### 2. Running the python notebook

