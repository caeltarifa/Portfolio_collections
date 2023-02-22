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

# Distributed computing for [multi matches phone prefixes problem](https://github.com/caeltarifa/Portfolio_collections/tree/main/CheapestOperator_py)
  
### [*Try out python program on googleColab here*](https://colab.research.google.com/drive/1b6yQSDVvUD8KxADdzCJJXfkTeAZi5HGJ?usp=sharing)

<details>
<summary><h3> 1. Specifications </h3></summary>
<p>

### **Code programming is used to solve and test these problem features**

* It is given price lists including price per minute for different phone number prefixes.
* When several prefixes match the same number, the longest one should be used.
* If a price list does not include a certain prefix you cannot use that operator to dial numbers starting with that prefix.
* Assume that each price list can have thousands of entries but they will all fit together in memory.
* Telephone numbers should be inputted in the same format as in price lists, for example “68123456789”.
* Handle any number of price lists (operators) and then can calculate which operator that is cheapest for a certain number. Find the cheapest operator for that number.
* Data format of operators' price list. The left column represents the telephone prefix (country + area code) and the right column represents the operators price per minute for a number starting with that prefix.
        
    | Prefix  | Price |
    |-------|-------------|
    |  46732 | 1.1         |
    | 46732 | 	 1.1       |
    | 46	  | 0.17        |
    | 4620	 | 0.0         |
    | 468	  | 0.15        |
</p>
</details>




<details>
<summary><h3> 2. Finding the cheapest operator </h3> </summary>
<p>
 
[[*Code for solution*]](https://github.com/caeltarifa/Portfolio_collections/blob/main/CheapestOperator_py/CheapestOperator.py)
 
A class to find the cheapest operator for a given telephone number. The class takes a telephone number and a SparkContext object during initialization, and loads price lists for each operator into a dictionary. The class then finds the cheapest operator for the given telephone number based on the longest matching prefix.

### **Requirements** <br>
This code requires PySpark to be installed. PySpark is the Python API for Apache Spark, which is a fast and general-purpose cluster computing system.

### **Usage** <br>
Instantiate a CheapestOperator object with a telephone number and a SparkContext object:

````python
from pyspark import SparkContext

number = "4673212345"
sc = SparkContext("local", "CheapestOperator")
operators_url = {
    'OperatorA':'./op_a.txt',
    'OperatorB':'./op_b.txt',
    'OperatorC':'./op_c.txt',
}
obj = CheapestOperator(number, sc)
obj.setup_dataset(operators_url)
print(obj.cheapest_operator()) # prints Cheapest operator and its price "Operator A 1.1"
sc.stop()
````
The ``operators_url`` dictionary should map operator names to the file paths of their price lists. Each price list file should contain lines with the format ``prefix price``, where ``prefix`` is a telephone number prefix and ``price`` is the price for that prefix.

### **Methods** <br>

``__init__(self, number:str, sc: SparkContext)``
The constructor for the CheapestOperator class. Takes a telephone number and a SparkContext object as arguments.

``setup_dataset(self, operators_url:dict)``
Loads the price lists for each operator into a dictionary. The ``operators_url`` dictionary should map operator names to the file paths of their price lists. Each price list file should contain lines with the format ``prefix price``, where ``prefix`` is a telephone number prefix and price is the price for that prefix.

``update_prefix_prices(self, operator_data_file)``
Updates ``self.prefix_prices_op`` with the prices from a new operator. The new operator's price list is passed as an RDD in the format ``prefix price operator``. For each prefix in the new price list, the function checks if the prefix is already in ``self.prefix_prices_op``, and if so, updates the cheapest price and operator. If the prefix is not already in ``self.prefix_prices_op``, the function adds the prefix and price to the dictionary.

``cheapest_operator(self)``
Finds the cheapest operator for the given telephone number based on the longest matching prefix. Returns the name of the cheapest operator and the price for the longest matching prefix. If no matching prefix is found, returns a message indicating that no operator was found for the given number.
</p>
</details>


<details>
<summary><h3> 3. Testing the solution </h3></summary>
<p>
 
 [[*Testing solution code*]](https://github.com/caeltarifa/Portfolio_collections/blob/main/CheapestOperator_py/CheapestOperator_test.py)

This code contains unit tests for the CheapestOperator class using PySpark. The tests cover different cases to ensure that the function cheapest_operator() returns the expected results for different input scenarios.

### **Prerequisites** <br>
In order to run these tests, you need to have ``PySpark`` and ``unittest`` installed in your environment.

### **Running the tests** <br>
To run the tests, simply execute the following command:
```python
python CheapestOperator_test.py
```

### **Test cases** <br>
The following test cases are included:
* ``test_cheapest_operator() ``: Tests the case where the cheapest operator is found for a valid phone number.
* ``test_invalid_number() ``: Tests the case where no operator is found for an invalid phone number.
* ``test_operator_B_only() ``: Tests the case where only one operator is available in the dataset.
* ``test_longest_prefix() ``: Tests the case where the longest prefix is chosen over the cheapest price.
* ``test_multiple_operators_same_price() ``: Tests the case where multiple operators have the same price for a given prefix.
* ``test_single_operator_single_prefix() ``: Tests the case where only one operator is available for a given prefix.
* ``test_single_operator_multiple_prefixes() ``: Tests the case where one operator has multiple prefixes in the dataset.
* ``test_same_price_different_operator() ``: Tests the case where different operators have the same price for a given prefix.
* ``test_case_insensitive_dict() ``: Tests the case where the operator keys are case-insensitive.

### **Data sources** <br>
The input datasets for the tests are stored in the following files:

  op_a.txt: Dataset for Operator A <br>
  op_b.txt: Dataset for Operator B <br>
  op_c.txt: Dataset for Operator C <br>

</p>
</details>



<details>
<summary><h3> 4. About efficient solution and a review of employed tools. </h3></summary>
<p>

 Severals approaches have been considerated when looking up a solution for the solution:
* Many operators and their lists of massive prefixes and prices
* Recurring matches by a given number in the operator's list (considering thousands of matches)
* When each operator serves the same prefix, repetitive matches with a large quantity of prefixes occur.

Below is showed the technological pertinence in order to solve it, considering in-memory processing:

| Tool                                | Examination                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PySpark API                         | Spark provides in-memory processing of data, allowing to run much faster than traditional big data processing framework.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RDD (Resilient Distributed Dataset) | RDD has become the primary programming interface for working with semi-structured as well as structured data. Though RDD is one way to acchieve the solution for large dataset, there is also another tool as DataFrame which is queried by spark SQL. A contrastion to decide one road consists selecting the first one because the problem contains no any prioritization over data structure and/or data relations. Thereby, it is not neccesary to think about SQL here with dataFrame method. <br/><br/> Finally, RDDs are immutable, partitioned collections of records that can be processed in parallel across a distributed cluster of machines. |

### But, why to need a processing in parallel across a distributed cluster of machines for massive data?
Seeking for a response, I'd reference this paper ["MapReduce: Simplified Data Processing on Large Clusters"](https://research.google.com/archive/mapreduce-osdi04.pdf). The paper highlights the benefits of parallel processing across a cluster of machines, such as

1. Performance: **Parallel processing across a cluster of machines can help to reduce the time it takes to analyze large datasets**
2. Scalability
3. Fault tolerance
4. Flexibility

 
</p>
</details>

