# Databricks notebook source
dbutils.widgets.text("Source", '', '')

# COMMAND ----------

source = getArgument("Source")

# COMMAND ----------

print(source)

# COMMAND ----------


