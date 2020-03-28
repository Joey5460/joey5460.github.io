Introduce
---------

Some Rst tags are similar to Markdown. For example, 

::

    - , ==== , ----

    **strong**, *emphasize*

Result in:

    - , ==== , ----

    **strong**, *emphasize*

.. contents::

Block 
-----

::

    a block example::

        This is an example for block 

Result in:

    a block example::

      This is an example for block 

Sections
--------
::

    Chapter 1
    ==========
    
    1.1
    ---

    1.1.1
    ~~~~~

      
Inline Markup
-------------

::

    - **bold**

    + *I*

    * code sample : ``print ("hello world")``

    #. autonumber first with 
    #. autonumber second  with 

Result in:

- **bold**

+ *I*

* code sample : ``print ("hello world")``

#. autonumber first with 
#. autonumber second  with 

Footnotes
---------

reference: [1]_


Hyperlinks
----------

`a link to my website <http://joey5460.github.com>`_

website_

.. _website: https://joey5460.github.com



Math
----
1. build-in math

.. math:: \frac{ \sum_{t=0}^{N}f(t,k) }{N}

2. this is inline math [2]_ :math:`\frac{ \sum_{t=0}^{N}f(t,k) }{N}`

Table
-----
Beatiful table

+------+------------+
|tag   | meaning    |
+======+============+
|``#.``| autonumber |
+------+------------+
| #.   | autonumber |
+------+------------+
| #.   | autonumber |
+------+------------+
| #.   | autonumber |
+------+------------+

- simple table

  ======== ========
  header1   header2
  ======== ========
  #. a       row1
  #. b       row2 
  ======== ========

- csv table

.. csv-table:: rst tutorial
	:header: "tag", "meaning"

	"\*", "bullet"
	"`-`", "bullet as well"
	"`+`", "also bullet"

.. [1] http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. [2] https://stackoverflow.com/questions/3610551/math-in-restructuredtext-with-latex#11226398
