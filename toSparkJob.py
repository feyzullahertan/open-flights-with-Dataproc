import matplotlib
from pyspark.sql import SparkSession, SQLContext, Row


gcs_bucket = ['Bucket_name']
spark = SparkSession.builder.appName("airflight").getOrCreate()

sc = spark.sparkContext
data_file = "gs://" + gcs_bucket + "dataset_name"

raw_rdd = sc.textFile(data_file).cache()
raw_rdd.take(5)




%matplotlib inline
ax = airline_stats.toPandas().plot.bar('protocol_type', subplots = True, figsize=(10,25))
ax[0].get_figure().savefig('report.png')

"""
Airline	2-letter (IATA) or 3-letter (ICAO) code of the airline.
Airline ID	Unique OpenFlights identifier for airline (see Airline).
Source airport	3-letter (IATA) or 4-letter (ICAO) code of the source airport.
Source airport ID	Unique OpenFlights identifier for source airport (see Airport)
Destination airport	3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
Destination airport ID	Unique OpenFlights identifier for destination airport (see Airport)
Codeshare	"Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
Stops	Number of stops on this flight ("0" for direct)
Equipment



"""

"""
SELECT LIMIT 20
airline,COUNT(dest_id)
FROM TABLO
GROUP BY airline,dest_id
ORDER BY dest_id


"""
