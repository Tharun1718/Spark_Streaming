from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NYSEStockStreamingApp")
ssc = StreamingContext(sc, 1)

previous_max_prices = sc.textFile("previous_max_prices.txt").map(lambda line: line.split(",")).cache()
previous_max_prices = previous_max_prices.map(lambda x: (x[0], float(x[1])))

lines = ssc.socketTextStream("localhost", 9999)

stock_data = lines.map(lambda line: line.split(",")).map(lambda x: (x[0], (x[1], float(x[2]))))
joined_data = stock_data.transform(lambda rdd: rdd.join(previous_max_prices))
filtered_data = joined_data.filter(lambda x: x[1][0][1] >= x[1][1])

filtered_data.pprint()

ssc.start()
ssc.awaitTermination()