# Databricks notebook source
# MAGIC %md
# MAGIC # Rename this file variables.py after you fill in your variables.

# COMMAND ----------

#GENERAL
user_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split(".")[0]

# COMMAND ----------

#GENERAL
catalog='mlx_semmanuel'
schema = f'{user_name}_llm_workshop'
volume_name = 'cmu_movies'

secrets_scope=''
secrets_hf_key_name=''

workspace_url = "https://" + spark.conf.get("spark.databricks.workspaceUrl") 
base_url = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()

# COMMAND ----------

#CREATE ASSETS
spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
spark.sql(f"USE SCHEMA {schema}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {volume_name}") 

# COMMAND ----------

#DATA PREP
volume_path=f"/Volumes/{catalog}/{schema}/{volume_name}"

chunk_size=200
chunk_overlap=50

sync_table_name = 'movie_documents_for_sync'

# COMMAND ----------

#EMBEDDING MODEL
embedding_model_name=f'{user_name}-e5-small-v2'
registered_embedding_model_name = f'{catalog}.{schema}.{embedding_model_name}'
embedding_endpoint_name = f'{user_name}-e5-small-v2-endpoint' 

# COMMAND ----------

#VECTOR SEARCH
vs_endpoint_name=f'{user_name}-movie-recommender'
# co-forge vector search endpoint

vs_index = f'{user_name}_movie_index'
vs_index_fullname = f"{catalog}.{schema}.{vs_index}"

sync_table_fullname = f"{catalog}.{schema}.{sync_table_name}"

# COMMAND ----------

#LLM SERVING
llm_model_name=f'{user_name}-llama-2-7b-hf-chat'
registered_llm_model_name=f'{catalog}.{schema}.{llm_model_name}'
llm_endpoint_name = f'{user_name}-llama-2-7b-hf-chat-endpoint'
