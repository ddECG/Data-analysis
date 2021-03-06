# Data analysis
Repository for data analysis for the DDA and DDSA data science challange. Our main goal for the challange is to use transfer learning from a large model, and apply it to a smaller dataset to predict a different outcome. We are working with the following datasets:
* **PTB-xl**: 21837 12-lead ECGs from 18885 patients. 
* **Code 15%**: TODO
* **Cardiovascular complications**: TODO

Depending on analysis apprach, data must likely all be converted to h5py format.

## Functions
#### Convert wfdb files contained within a folder to h5py
  ```python convert_hdf5.py INPUT_FOLDER OUTPUT_FILE```

# Datasets
### 1 - PTB-xl
**Analysis approach**
Several steps should be taken before analysis of the PTB-xl dataset.

Firstly, we should remove low quality ECGs (based on signal metadata), and also duplicate measurments (same patient).

After cleaning we must probably convert data to h5py binary format to be compatible with model.

**Data format**
* Data is formated as .dat binary files.
* Contains both 500hz and 200hz ECG measurments.
* Data is split in a bunch of ways in relation to quality of ECG (Folds)
  * Fold 9 + 10 underwent at least one human evaluation (High label quality)
  * Keep in mind when getting to cross-validation

**Additional data**
* ECG statements: A bunch of SCP-ECG statements
* Signal metadata: Stats related to:
  * Static noise
  * Burst noise
  * Baseline drift
  * Electrodes problems 
  * Extra beats

**Download raw data**
Raw data can be downloaded by:
### 4 - Code 15
**Analysis approach**
Great dataset with 12 lead ECGs. One can download pretrained models for age prediction.

**Data format**
* Is in the hdf5 format.
* wfdb can be converted to hdf5 by using the `convert_hdf5.py` function

**Download raw data**
TODO

### 3 - Cardiovascular complications
**Analysis approach**
This dataset is not particularly organised and needs alot of data cleaning to be comparable to other datasets.

**Download raw data**
Raw data can be downloaded by:
```
'wget -r -N -c -np https://physionet.org/files/cded/1.0.0/'
```
# Notes
### Data storage
Raw data should be stored as unpacked folders in the `'data-raw/'` folder. The following folder structures should be used:
* 'data-raw/ptb-xl/'
* 'data-raw/code-15/'
* 'data-raw/cadiovascular_complications/'
* 'data-raw/test/'

Edited data is stored in the `'data/'` folder. The following folders can be used.
* 'data/test/'

### Contributing
When writing or updating code, create a new branch. Best practice is to do the following:
1. Create new branch
2. Make edits/additions
3. Commit and push changes to github
4. Create Pull request on github
