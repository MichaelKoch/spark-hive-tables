import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,from_json
spark = SparkSession.builder.master("local[4]") \
                    .appName('test') \
                    .enableHiveSupport() \
                    .getOrCreate()

df_import = spark.read\
                .option("multiLine", True)\
                .json("/app/data.json").cache()
                
df_import.show()
df_import.printSchema()


df_import.write.mode(saveMode="overwrite")\
                 .saveAsTable("products")

print("table: products imported rows :" + str(df_import.count()))
df_import.printSchema()
id=3333333
df_table = spark.sql(f"select Colors from products where styleId = {id}")
df_table.explain()
# df_table_colors = df_table.withColumn('Colors',explode("Colors"))

df_table.show()
df_table.printSchema()

