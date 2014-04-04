This second learning lunch is on making graphs in [R](http://www.r-project.org/) using the [ggplot2](http://ggplot2.org/) package. The goal is give designers on the graphics team ideas about how to quickly sketch with data, fluidly moving various visual mappings.

#What is R?

R is an extremely powerful, open source, statistical programming language. People have written thousands of [packages](http://cran.us.r-project.org/) to do all sorts of cool things in R, but today we're just looking at a single called ggplot2, which has tons of graphing functionality. 

###Getting started

First off, download R [here](http://cran.rstudio.com/) and install it. Once launched, the R program looks a lot like a Terminal or Command Prompt, it's a command line interface (CLI), where you type commands one at a time. Like other CLI's, you can hit the up arrow to see your previous commands, but it's easy to lose track of what you've been typing. I always write my R code in a text editor, then copy and paste that code into R. This also means that if the data changes or I need to update a sketch, I can do so in a handful of clicks and keystrokes.

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
* statistics (stat), which tell ggplot how to analyze and sort the data (we just touch on this below)

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

If you skipped right down to this section, that's ok, most of this code is reusable and copy-paste-able.

* **Load the data:**

First, tell R where to look for files, go to Misc > Change Working Directoyr (or cmd-D on a Mac)
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/workingdir.png "change working directory")

Then type
```
data <- read.csv("ggplot_data.csv")
```
Which reads the file named `ggplot_data.csv` into a data frame, and assigns it to the variable named `data`.

In R, you can cut down huge data files to just what you need, but for our purposes I started with a small file which lists lobbying behavior by Landscaping & Excavation companies (the amount they spent per year, that amount in 2012 dollars, and their ranking among other similar companies by amount spent). I trimmed and expanded on the source data with a Python script (included in this repo), but it could be done in R, excel, by hand, etc.

##Plotting a line chart (aka fever chart)

Remember, ggplot2 splits data into data (check), aesthetics, and geometries.

* **Assigning aesthetics:**
The `head()` function is a good way to take a look at the first few rows of a data frame, like so

![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/head.png "the head function's output")

Which is a nice quick way to check out column names etc.

Now, run this command:

```
p <- ggplot(data, aes(x=year,y=rank,group=client,color=client))
```
This tells ggplot to use the `data` variable as its data, then map the following aesthetics:
* x values to the year column
* y values to the rank column
* group by client, so each client automatically gets put on its own group
* also color by client, so that each fever line/set of points/ etc. is a different color (this will automatically create a key saying which is which). Default ggplot colors are ugly but high contrast (they're evenly spaced out around the color wheel)

Now we tell ggplot to plot this as a line graph:
```
p + geom_line()
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/line1.png "basic fever chart")

Next, let's add points to the line
```
p + geom_line() + geom_point()
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/line2.png "fever chart with dots")

Awesome, this showed us 2 data points which were invisible before, since they only exist for 1 year.

And hey, why don't we scale the size of the point by the number of dollars spent? Within geom_point, we can add *more* aesthetics, which are specific just to that geometry (so they won't effect the line chart), like so
```
p + geom_line() + geom_point(aes(size=data$infl_amt))
```
Note that when we refer to a column in data, `infl_amt` isn't enough anymore, since geom_point has no concept of what data it's associated with.

![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/line3.png "fever chart with dots scaled by dollars")

Those smaller dots are tough to see, lets set a minimum and maximum radius.
```
p + geom_line() + geom_point(aes(size=data$infl_amt)) + scale_size_continuous(range=c(2,20))
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/line4.png "fever chart with dots scaled by dollars, larger dots")

And finally, let's flip the y axis so that the highest rank is on top, and limit the years to just 2005 and later.
```
p + geom_line() + geom_point(aes(size=data$infl_amt)) + scale_size_continuous(range=c(2,20)) + scale_y_reverse() + scale_x_continuous(limits=c(2005,2014))
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/line5.png "fever chart with dots scaled by dollars, larger dots")

Note that you can save any of these graphs as pdfs, then edit in Illustrator. Each element is a separate object, although you'll need to ungroup a lot and delete some invisible objects.

##Plotting an area chart

The difference between an area chart and a bar chart is pretty trivial. To get an area chart, try:

```
ggplot(data,aes(x=year,y=rank,group=client,fill=client)) + geom_area()
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/area1.png "area chart")

Yuck, this doesn't work well as an area chart, but you get the idea.

Just two differences between the line chart example. One, `geom_line()` is replaced by `geom_area()`, and two, `color=client` is replaced by `fill=client`. In R, `color` refers to stroke, in general, and `fill` to...fill. So `color=client` would draw color coded lines with black areas beneath them.

The default behavior is to stack areas. If you wanted to overlay areas you could try:

```
ggplot(data,aes(x=year,y=rank,group=client,fill=client)) + geom_area(position="identity",alpha=.5)
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/area2.png "area chart without stacking")

Still, yuck, but I'm sure you can imagine cases where this would be useful. Here `position="identity"` turns off stacking (the default behavior is `position=stack`), and `alpha=.5` sets an alpha value so you can (kind of) see all the traces.

##Plotting a bar graph
It's super easy to convert your line chart to a bar chart. The data stays the same, and the aesthetics need to change a bit. Here's the command:
```
p <- ggplot(data, aes(x=year,y=infl_amt,fill=client)) 
p + geom_bar(stat="identity")
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/bar1.png "stacked bar chart")

You'll notice a few differences.

The default behavior is to stack the bars. If you'd rather see them grouped, type:
```
p + geom_bar(stat="identity", position="dodge")
```
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/bar2.png "stacked bar chart")

Also, within geom_bar, we set `stat="identity"` (our first usage of `stat`, hooray!). This means that the height of the bars corresponds to the value of `infl_amt`. The default for bars is `stat=bin`, which makes the bar heights correspond to counts (the number of rows within each x category), so you don't need to map a varable to y. For example
```
p <- ggplot(data, aes(x=client,fill=client)) 
p + geom_bar()
```
(Note that you don't need to include `stat=bin` since it's the default behavior)
![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/bar3.png "binned bar chart")

##A trick to reshape data

One more R package (of the thousands out there) that can be useful. Let's say you want to graph two line charts about the One Call Concepts company: one which shows an amount, and one which shows the inflation adjusted amount. You could make a new .csv of just the One Call Concepts rows, no problem. Or, if you wanted to be sneaky in R, you could try:

```
data <- data[data$ultorg=="One Call Concepts",]
```

Remember `data$ultorg` is a *column*, named ultorg, and `data[something,]` is a *row*. So this translates in plain English to:
>"find all rows in data where the value in the ultorg column is equal to 'One Call
>Concepts', then return that as a new data frame and store in in `data`".

Next, install and load the package called "reshape2" (so that's `install.packages("reshape2")` then `library("reshape2")`). There's a function in this library called "melt" which ggplot2 users love. I'll show what it does by example:
```
data <- melt(data,measure.vars=c("amt","infl_amt"))
```

This reshapes data into:

![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/melt.png "output of melt function")

So the variables listed in `measure.vars` become new values in the `variable` column, with their values in `value`. This is useful, since ggplot always wants *every row* to include *every variable* mapped to an aesthetic (x,y,group,etc.)

So you could now graph:
```
ggplot(data,aes(x=year,y=value,group=variable,color=variable))+geom_line()
```

![alt text](https://raw.github.com/bchartoff/learninglunches/master/ggplot2/images/meltedline.png "melted line chart")

Cool!? Yes.

##Wrapping up

R and ggplot2 can do lots (lots!) more, but this is a great place to start with sketches. Sketching with ggplot2 is a great way to produce lots of visualizations quickly, and easily modify them as data changes. Whether you use the R output as a framwork for the final visualization or build it in Illustrator/ D3/ etc, it's always a great place to start. Come find me if you have questions!





