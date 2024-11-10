# brightsparks-csv-to-yaml
CLI tool that takes in a csv file, detailing records of individuals and their
points at certain duties, and outputs YAML of the top performing individuals by
default but it can also be sorted by alternative means.

## Installation
Clone the repository. Then build the package.
```
python3 -m build
```
Then install it.
```
pip install -e .
```
You should now have `brightsparks-csv-to-yaml` as a command line tool.

## How to Use
The CSV file contains the following columns:
* `firstname`: String
* `lastname`: String
* `date`: String (format YYYY-MM-DD)
* `division`: Integer
* `points`: Integer
* `summary`: String

By default it then:
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

### Example
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

Command:
```
brightsparks-csv-to-yaml <input-file>
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
### Synopsis
```
brightsparks-csv-to-yaml [-h] [-c COUNT] [-s {firstname,lastname,date,division,points}]... filename
```
You can provide a `COUNT` of the number of records you want returned if you want something other than default.
You can provide a different means of sorting. E.g. if you invoke
```
brightsparks-csv-to-yaml -s firstname -s lastname filename
```
It would determine the top records based on alphabetical order of firstname and
in the event of ties, would rely on lastname. Note that lexicographically lesser
strings are considered higher in sorting, so if you had Alex and Blake, then
Alex would be the top record compared to Blake.

Similarly for dates, earlier dates are considered higher.

Division and points work as you would expect.

## Notes
[] **Code style and commenting**.
Declaration of private variables and then accessing them regardless.
`Record` class uses variables to store attributes. Consider using a dictionary
so that there isn't a need to convert Record instances to dictionary before yaml output.
[x] **Unit Tests**.
[x] Overall design and architecture.
[x] Suitability of data structures and algorithms used.
[x] Handling of edge cases.
[x] Logging and error reporting.
[x] Ease of build and deployment.