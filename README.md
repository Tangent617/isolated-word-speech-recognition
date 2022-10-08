# CMSC5707 Assignment 1

## Install requirements

Python libraries needed are listed in *requirements.txt*, to install them run:

```shell
pip install -r requirement.txt
```

## Run

### 4.c. the Fourier Transform of Seg1

```shell
cd 4\ Signal\ Analysis
python c.py
```

It'll show the figure of Seg1 after FFT and save it as *fourier_x.jpg*.

### 4.d. pre-emphasis signal of Seg1

```shell
cd 4\ Signal\ Analysis
python d.py
```

It'll show the wave of Seg1 and Pem_Seg1 and save them in one picture as *Pem_x.jpg*.

### 4.e. LPC-10 parameters

```shell
cd 4\ Signal\ Analysis
python e.py
```

It'll output the LPC data in a file called *lpc10.txt*.

### 5. a speech recognition system

```shell
cd 5\ speech\ recognition\ system
python rec.py
```

Wait for a minute or two.

It'll output the confusion matrix table in *confusion matrix.csv*, and show a picture of it which saves as *confusion matrix.jpg*.

A lower score means a higher probability, and is shown in the picture with a darker color.