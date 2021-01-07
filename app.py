#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import pymysql


st.title("hello Antoine!")

mydb = mysql.connector.connect(
    host="mysql-development",
    user="root",
    password="antoine",
    database = "suicide-app"
)
print(mydb)
cursor = mydb.cursor()
sql = "CREATE TABLE regions (id INT AUTO_INCREMENT PRIMARY KEY, region VARCHAR(255));"
cursor.execute(sql)
