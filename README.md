# BrightSPARK LABS assessment
CLI tool that takes in a csv file, detailing records of individuals and their points at certain duties, and outputs YAML of the top 3 performing individuals.

The CSV file contains the following columns:
* `firstname`: String
* `lastname`: String
* `date`: String (format YYYY-MM-DD)
* `division`: Integer
* `points`: Integer
* `summary`: String

It then:
* Sorts the records by `division` and `points`.
* Selects the top three records.

It prints the records to stdout in the following YAML format:
```
records:
- name:
  details: In division from performing
- name:
  details: In division from performing
- name:
  details: In division from performing
```

## How to use cli tool
## Example

Input file:
```
firstname,lastname,date,division,points,summary
Terza,Lowton,2017-09-15,1,53,"Defensive Duties"
Kayle,Trayes,2017-10-23,9,83,"Offensive Duties"
Reba,Crosi,2017-10-23,6,84,"Offensive Duties"
Barnett,Dunnico,2018-02-26,5,24,"Offensive Duties"
Elke,Collete,2017-06-19,6,68,"Oversight Duties"
Tess,Gosson,2017-12-22,9,22,"Defensive Duties"
Zedekiah,Miller,2018-04-09,3,89,"Offensive Duties"
Zelma,Ivatt,2018-01-02,1,72,"Offensive Duties"
Vivia,Twidell,2017-11-17,9,72,"Offensive Duties"
Alvira,Elger,2017-05-02,6,58,"Oversight Duties"
```

Output:
```
records:
- name: Zelma Ivatt
  details: In division 1 from 2018-01-02 performing Offensive Duties
- name: Terza Lowton
  details: In division 1 from 2017-09-15 performing Defensive Duties
- name: Zedekiah Miller
  details: In division 3 from 2018-04-09 performing Offensive Duties
```

**NOTE:** The order of keys in YAML are irrelevant. So the following output is
also acceptable:
```
records:
- details: In division 1 from 2018-01-02 performing Offensive Duties
  name: Zelma Ivatt
- details: In division 1 from 2017-09-15 performing Defensive Duties
  name: Terza Lowton
- details: In division 3 from 2018-04-09 performing Offensive Duties
  name: Zedekiah Miller
```

## Assessment:
We will be assessing your solution according to the following:
1. **Code style and commenting**.
2. **Unit Tests**.
3. Overall design and architecture.
4. Suitability of data structures and algorithms used.
5. Handling of edge cases.
6. Logging and error reporting.
7. Ease of build and deployment.


Libraries:
`pyyaml`, `argparse` for options, `re` 

Test Runner:
`pytest`

# Instructions to convert python script into shell command