This second learning lunch is on making graphs in [R](http://www.r-project.org/) using the [ggplot2](http://ggplot2.org/) package. The goal is give designers on the graphics team ideas about how to quickly sketch with data, fluidly moving various visual mappings.

#What is R?

R is an extremely powerful, open source, statistical programming language. People have written thousands of [packages](http://cran.us.r-project.org/) to do all sorts of cool things in R, but today we're just looking at a single called ggplot2, which has tons of graphing functionality. 

###Getting started

First off, download R [here](http://cran.rstudio.com/) and install it. Once launched, the R program looks a lot like a Terminal or Command Prompt, it's a command line interface (CLI), where you type commands one at a time. Like other CLI's, you can hit the up arrow to see your previous commands, but it's easy to lose track of what you've been typing. I always write my R code in a text editor, then copy and paste that code into R. This also means that if I the data changes or I need to update a sketch, I can do so in a handful of clicks and keystrokes.

###Notes on syntax

Like other programming languages, R code is mostly made up of *variables* and *functions*. To assign a value to a variable, R uses the symbols `<-` (like `=` in many other languages). So to assign a value of 5 to x, you write `x <- 5` which is read as "x gets 5".

Many R packages, including ggplot2, use the `+` symbol to string functions together. The examples below follow a format similar to:
```
plot <- plot_function()
plot <- plot + scale_function()
plot <- plot + color_function()
plot
```
Which is equivilant to
```
plot <- plot_function + scale_function() + color_function()
plot
```
Note that the final `plot` is what displays the variable, which in this case means drawing the graph.

###Data types

Mostly, in ggplot, you'll be working with data in `data frames`, which are a way of representing spreadsheet-like data in R (rows and columns). You'll also be dealing with `lists` which are, yup, lists of values. To create a list, the R syntax is:

####Lists

```
mylist <- c(val1,val2,val3)
```
To get the 1st element of a list, type `mylist[1]` (<Nerd aside>this means R lists are 1 indexed, mylist[0] returns the type of the list elements</Nerd aside>)

####Data frames

Below is an example of creating a data frame by importing a spreadsheet.

Once you have a data frame, you can access rows and columns like so:
```
mydataframe[1]
```
returns the first column of the data frame *as a new data frame with one column and many rows*
```
mydataframe$column_name
```
returns the named column of the data frame *as a list*. Note that all data frame columns must be named. If you don't give them names, they default to `X1, X2, X3, etc.` Also note R doesn't like column names that start with numbers, so if, for example, you have a spreadsheet with a column named `2012_dollars` R will rename it to `X2012_dollars`. It also doesn't like spaces, so it will rename `2012 dollars` to `X2012.dollars`. Moving on.
```
mydataframe[1,]
```
returns the first row of the data frame *as a list*

So, to get the element in the 3rd column (named `org`), 2nd row, you could either type... (pause, see if you can answer)






...












...








```
mydataframe[3][2,]
```
or
```
mydataframe$org[2]
```

#What is ggplot2?

ggplot2 is a graphing package based on the theories of data visualization spelled out in [The Grammar of Graphics](http://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448) (D3 was similarly inspired). Fundamentally, it treats graphics as having three differnt types of components:
* data, which needs to be in a certain format (see below!)
* geometries, such as bar, line, scatter, etc.
* aesthetics (abbreviated aes), which spell out which data gets mapped to which aesthetic element (size, position, color, etc.)

###Getting started

To install ggplot2 in R, type
```
install.packages("ggplot2")
```
which will install it on your computer (you only need to ever do this once), then type
```
library("ggplot2")
```
which will load the package (you need to do this once per R session).

###Let's plot!


