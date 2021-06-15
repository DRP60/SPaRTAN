# Run SPaRTAN in Python

## Introduction
This is the Python/Cython implementation of the SPaRTAN. In order to improve the running time performance, we convert some computationally intensive python modules into Cython modules.  All functionalities are integrated into the class SPaRTAN. This tutorial focuses on how to run the program using CITE-seq data. 

## System Requirements
SPaRTAN relies on the following dependencies:
```sh
    python (>= 3.7.0)
    Cython (>= 0.28.5)
    pandas (>= 1.0.0)
    numpy (>= 1.15.4)
    scikit-learn (>= 0.19.2)
    scipy (>= 1.1.0)
    matplotlib (>= 2.2.3)
```
Cython requires a C compiler to be present on the system (i.e. Visual Studios). Please see [Installing Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html) for a complete guide.

Our codes have been tested on Linux, Mac, and Windows systems. Please see Prerequisites.xlsx for each version of packages we tested on every operating system.

## Installation
There is a Cython extension module needed for running SPaRTAN. We have built the extensions under Windows(.pyx files) and Linux/Mac (.so files) system. You can download ones based on your operating system. If they are not compatible with your platform, then you need to build the Cython extension. The followings are the instruction on how to build the Cython extension:

- building necessary extension modules 
    
	1. Go to folder "PySPaRTAN", then execute the command:
	
	```sh
	python setup.py build_ext --inplace
	```
	
	 It will generate .so (Mac or Linux), or .pyd (Windows) files needed for the next steps. 
	 

## Usage
SPaRTAN model has 4 parameters spectrumA, spectrumB, rsL2 and lambda. Their values are determined by the user input data D, P, and Y. We use cross-validation to determine the best values for those parameters. Here we explain step by step:

**Load the data**

We are able to specify the dataset we want using the command line, when running SPaRTAN_run.py in the "tests" folder. The default options will run the sample data provided in the SPaRTAN package. 
```sh
python SPaRTAN_run.py --dataset_D name_of_dataset_D --dataset_P name_of_dataset_P --dataset_Y name_of_dataset_Y --input_dir path/to/input/directory/ --output_dir path/to/output/directory/
```
**Train the model with cross-validation**

Along with our file specifications when running SPaRTAN_run.py, we can also specify the training parameters for SPaRTAN. Below are the default values for the program. However, SpectrumA, SpectrumB, Lamda, and rsL2 can be any float value. Normalization can be 'l1', 'l2', or 'max'. Fold can be any integer. This is only useful if fold = 0, otherwise cross-validation will take place. 

```sh
 python SPaRTAN_run.py --spectrumA 1.0 --spectrumB 0.7 --lamda 0.001 --rsL2 0.001 --normalization l2 --fold 2
```

**Extract best parameters**

After the cross-validation, we will be informed of the best parameters, if we have --fold > 0. If fold is 0, the parameters provided will be used. If no parameters are provided and fold is set to 0, then the default parameters will be used. (Best Parameters shown in "Train the model with cross-validation")

```sh
python SPaRTAN_run.py --fold 0
...
lamda_best=0.001, rsL2_best=0.001, spectrumA_best=1.0,spectrumB_best=0.7
```

**Complete implementation  of cross-validation**

OPTIONAL: In SPaRTAN_run, there will be a section to declare all lamdas, rsL2s, spectrumAs, and spectrumBs. If desired, you can modify the valued in which are being cross-validated. 

```sh
lamdas = [0.001, 0.01, 0.1, 0.2, 0.3 ]
rsL2s = [0, 0.001, 0.01]
spectrumAs = [1]
spectrumBs = [0.5, 0.6, 0.7 ]
```

## Outputs

All outputs should be found in the specified output folder. If no output folder is specified, the data should be found in data/outputs. Three files should be found there:

projD.csv - a comma deliminated file containing a transcription factor by cell matrix
projY.csv - a comma deliminated file containing a cell by surface-protein matrix
W.csv - a comma deliminated file containing a transcription factor by surface-protein matrix
