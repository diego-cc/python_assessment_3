# Python - Assessment 3

Three applications are included in this repository:

1. Colourful: A GUI application that displays random colours and their respective complements
2. A Magic 8-ball CLI application
3. A signal handler CLI application

## Cloning the project

```shell script
git clone https://github.com/diego-cc/python_assessment_3.git
```

## Installing packages

A conda environment was used for this project, which can be created by running the command below from the root project folder (`python_assessment_3`):

```shell script
conda env create -f environment.yml
```

Then, run the command below to activate your new environment:

```shell script
conda activate python_assessment_3
```

Alternatively, you may simply install the required packages through **pip**:

```shell script
pip install -r requirements.txt
```

## Running

From the root project folder (`python_assessment_3`), run in your terminal:

```shell script
python main.py
```

Alternatively, if you wish to run each program individually:

```shell script
python -m task_a.start
python -m task_b.start
python -m task_c.start
```
