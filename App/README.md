# Unemployment-Report



## setup

create and activate a vritual environment:

```sh
conda create -n unemployment-env python=3.9

conda activate unemployment-env

Install package dependencies: 
```sh
pip install -r requirements.txt
```

##Configuration
[Obtain an API Key] (https://www.alphavantage.co/support/#api-key)


Obtain an API Key from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
ALPHAVANTAGE_API_KEY="____"
``` 

#usage


Run an example script:

```sh
python app/my_script.py
```
Run the unemployment report:

```sh
python app/Unemployment.py

ALPHAVANTAGE_API_KEY="____" python app/unemployment.py
```''
