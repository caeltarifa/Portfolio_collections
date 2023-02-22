[![ML Workflow](https://github.com/caeltarifa/Portfolio_collections/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/caeltarifa/Portfolio_collections/actions/workflows/main.yml)

# Machine Learning model collections
 <details>
    <summary><h3>ML models by Python</h3></summary>
    <p>

 - **Predictions**
 - **Classification**
 - **Clustering**
 - **Linear classification**

    </p>

  </details>

# Distributed computing for [Multi matches phone prefixes](https://github.com/caeltarifa/Portfolio_collections/blob/main/Parallel_programming.ipynb)
## 1. About efficient solution and tools implied.
Severals approaches have been considerated when looking up a solution for the solution:
* Many operators and their lists of massive prefixes and prices
* Recurring matches by a given number in the operator's list (considering thousands of matches)
* When each operator serves the same prefix, repetitive matches with a large quantity of prefixes occur.

Below is showed the technological pertinence in order to solve it, considering in-memory processing:

| Tool                                | Examination                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PySpark API                         | Spark provides in-memory processing of data, allowing to run much faster than traditional big data processing framework.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RDD (Resilient Distributed Dataset) | RDD has become the primary programming interface for working with semi-structured as well as structured data. Though RDD is one way to acchieve the solution for large dataset, there is also another tool as DataFrame which is queried by spark SQL. A contrastion to decide one road consists selecting the first one because the problem contains no any prioritization over data structure and/or data relations. Thereby, it is not neccesary to think about SQL here with dataFrame method. <br/><br/> Finally, RDDs are immutable, partitioned collections of records that can be processed in parallel across a distributed cluster of machines. |


### But, Why to need a processing in parallel across a distributed cluster of machines for massive data?
Seeking for a response, I reference this paper ["MapReduce: Simplified Data Processing on Large Clusters"](https://research.google.com/archive/mapreduce-osdi04.pdf). The paper highlights the benefits of parallel processing across a cluster of machines, such as

1. Performance: **Parallel processing across a cluster of machines can help to reduce the time it takes to analyze large datasets**
2. Scalability
3. Fault tolerance
4. Flexibility

