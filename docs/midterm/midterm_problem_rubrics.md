# SI 506: midterm exam problems
## Fall 2019
## Manual Grading Rubrics

Notes:

&lt;var&gt; = variable placeholder; student free to choose variable name.

## Problem 1 (find\_unique\_words(str\_list))

500 points

### Line 1: for &lt;string&gt; in str\_list:

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to write a for loop | 25 |   |
| Syntax correct | 25 |   |
| Iterates over string\_list iterable passed in as argument | 40 | Student must iterate over passed in list str\_list. Otherwise,student earns 0 points. |
| Indented correctly | 10 |   |

### Line 2: &lt; words&gt; = &lt;string&gt;.split()

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to split an object | 25 | If student attempts to split a list (incorrect) or string (correct) award full points. |
| Attempted &lt;string&gt;.split() on string\_list element | 20 | Student must split the str\_list element. Student earns 0 points if wrong object is split. |
| Split string using proper delimiter | 20 | &lt;string&gt;.split() or &lt;string&gt;.split(&#39; &#39;) accepted. |
| Assigned split expression to variable &lt;words&gt; | 25 | Student earns 0 points if list returned by the split operation is not assigned to a new variable. |
| Indented correctly | 10 |   |

### Line 3: for &lt; word&gt; in &lt; words&gt;:

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to write a for loop | 25 |   |
| Syntax correct | 25 |   |
| Iterates over &lt;words&gt; iterable | 40 | Student earns 0 points if they loop over the wrong iterable. |
| Indented correctly | 10 |   |

### Line 4: if &lt; word&gt; not in unique\_words:

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to write a conditional statement | 25 |   |
| Used membership operator in to test if &lt;word&gt; in target list unique\_words | 25 | Student should use membership operator not in but could solve the problem using in and an if/else statement. |
| Used membership operator not in to negate the return value of the if statement OR used the control statement continue together with an if/ else statement to perform the filtering operation. | 75 | if word not in unique\_words: OR if not word in unique\_words: OR if word in unique\_words:    continueelse:    unique\_words.append(word) Student earns points for either approach. |
| Student adds return statements (return True / return False) that force a premature exit from the function. | -25 | If student adds a return statement or return statements prematurely subtract -25 points. |
| Indented correctly | 10 |   |

### Line 5: unique\_words.append(word)

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to add &lt;word&gt; to target list unique\_words | 25 | If student attempts to append to the list any value other than a string, award 0 points. |
| Used list.append(&lt;word&gt;) method to add &lt;word&gt; to unique\_words. | 30 | If student used unique\_words.extend([&lt;word&gt;]) to extend unique\_words _with a list_ containing a single element &lt;word&gt;, they earn 25 points (-5 points deduction). |
| Indented correctly | 10 |   |

### Other Problem 1 issues

| Code | Points | Notes |
| --- | --- | --- |
| Problem submitted with syntax errors | -25 | If student submits a problem solution with syntax errors (e.g., Capitalized key words; broken comment lines) deduct 25 points from total score. |
| Student moves pre-positioned function variables outside of function | -25 | If student moves pre-positioned variable unique\_words = [] outside of function, deduct 25 points from total score. |

## Problem 2 (write\_long\_strings(contents,filename= &quot;midterm.txt&quot;))

### Line 1: write\_long\_strings(&lt;contents&gt;, &lt;filename&gt;=&quot;midterm.txt:):

| Code | Points | Notes |
| --- | --- | --- |
| Added &lt;contents&gt; as 1st parameter of function. | 25 |   |
| Added &lt;filename&gt; as 2nd parameter of function. | 25 |   |
| Assigned default parameter value &quot;midterm.txt&quot; to &lt;filename&gt; parameter. | 50 |   |

### Line 2: with open(&lt;filename&gt;,&#39;w&#39;) as &lt; file\_object&gt;:

| Code | Points | Notes |
| --- | --- | --- |
| Used with statement and built-in function open() to return a file object and assign to &lt;file\_object&gt; using filename argument for path. | 40 | If opened correctly using ye olde canonical way, student earns 25 points total if they 1) use open() to return a file object and 2) close the file object when done with it.  Otherwise, 0 points. If student fails to assign a new variable name for the returned file object (e.g., chose a  function parameter name as the name of the file object), student earns 0 points.  If student hardcodes name of the file in the open() function, student earns 0 points. |
| Sets open() parameter mode &#39;w&#39; correctly. | 50 | If opened correctly using ye olde canonical way, student earns 25 points total if they set the write mode parameter correctly. |
| Indented properly | 10 |   |

### Line 3: for &lt; item&gt; in &lt; contents&gt;:

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to write a for loop | 25 |   |
| Syntax correct | 25 |   |
| Iterates over &lt;contents&gt; iterable | 40 | If student fails to iterate over contents iterable, student earns 0 points. |
| Indented properly | 10 |   |

### Line 4: if len(&lt;item&gt;) &gt;  20 :

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to write a conditional statement. | 25 |   |
| Used the arithmetic operator greater than ( &gt; ) to test the condition | 25 |   |
| Returned the length of the &lt;item&gt; using the built-in len() function in order to test the condition. | 75 |   |
| Indented correctly | 10 |   |

### Line 5: &lt; file\_object&gt;.write(&lt;item&gt; + &quot; \n&quot;)

| Code | Points | Notes |
| --- | --- | --- |
| Attempted to write &lt;item&gt; to the target file using &lt;file\_object&gt;.write(&lt;item&gt;) | 30 | If student fails to use the file object to write the item to the file, student earns 0 points. If student treats &lt;item&gt; as if it is anything other than a string, deduct -15 points. |
| Added newline character (&#39;\n&#39;) to string &lt;item&gt; as part of the write operation | 25 |   |
| Indented correctly | 10 |   |

### Other Problem 2 issues

| Code | Points | Notes |
| --- | --- | --- |
| Problem submitted with syntax errors | -25 | If student submits a problem solution with syntax errors (e.g., Capitalized key words; broken comment lines) deduct 25 points from total score. |
| Student modifies function call by adding 2nd argument &#39;midterm.txt&#39; rather than defining function parameter with optional argument. | -25 | Deduct 25 points from total problem score. |
