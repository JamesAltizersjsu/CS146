SID:014485458 James Altizer 3/27/24 LAB 6 graphs and topological sorting
0 --> 1 --> 2
 \         /
  \--> 3 <--
heres a sample DAG for the prerequisite dpeendencies, 0 dpends on everything as it is the prerequisite for al n-1 courses
I originally conceived of this as being a linked list with 0 pointing to 1 and so forth, and then i would iterate over the list
of  paris to come up with that list but im realizing that in actuality it wanted to generate a graph of all the possible 
connections, with each entry in the list consisting of 2 nodes and their corresponding edge. 
If there exists a cycle in the graph (i.e., a situation where a course depends on itself or there’s a circular dependency), it’s impossible to finish all courses.
Otherwise, we can perform a topological sort to order the courses such that prerequisites are satisfied.
If the topological sort is successful, we can complete all courses.
This means that under the false condition like [[1,0],[0,1]] you cant have both these edges being true as that creates 
a cyclic graph which cant be topologically sorted. so its false. this approach is agnostic of the value of the courses themselves
we are achieving linear sequence sorting using graphs instead of manually iterating over the sums, for a signifanct logarithmic
polynomial time complexity improvement. Initialize an in-degree array to track the number of prerequisites for each course.
Create an adjacency list to represent the graph.
Populate the in-degree array and adjacency list based on the input prerequisites.
Use a queue for the topological sort.
Start by adding all courses with in-degree 0 to the queue. to do this we can multiply the value by setting the in degree
of every a in a,b to +=1 and then as we append 0 onwards we iterate with a for loop and then lower the indegree of the neighbors
by 1 and then append to the graph. we do this until the queue is empty. we return true, else return false
two arguments are needed, numcourses, for number of courses, and prerequisites, which is the course pairs.
by using these bivariate arguments in the graph data structure we can test the validity of the input.
THANKS For READING HAVE A GREAT SPRING BREAK PROFESSOR SHUKLA, and to you grader
sincerely, James
