This first learning lunch is on [node.js](http://nodejs.org/), and is for a relatively small audience of graphics-folks-who-code (the data visualization team at the Post). As such, it's geared towards front end designers/developers who are comfortable with Javascript. *

#What is Node?

Node.js is a platform built for fast network applications. It runs on the V8 virtual machine, which is the same VM which compiles javascript in Chrome. 

#Why Use Node?

##The front end perspective

Much of the discussions around the merits of Node assume you're comparing it to other back end programming languages/platforms/frameworks. I discuss these merits below, but a lot of them might sound familiar from Javascript &mdash; using function callbacks to run code asynchronously, for example. But Node has advantages from a front end viewpoint too:

* Node is run on the server (javascript is run in-browswer on the client side). This not only means you can do beefy javascript or javascript-esque things on the server ([prerendering d3 server side, for example](http://mango-is.com/blog/engineering/pre-render-d3-js-charts-at-server-side.html)), but you can also do things which are impossible from the client, like modifying files, accessing databases, etc.

* While native node (i.e. the initial install) has plenty of functionality, most node applications implement **modules**. Modules (like Python packages or Ruby gems, and sort of like Javascript libraries) are written to accomplish all sorts of specific tasks. Lots more on modules is below.

* Node allows you to write your whole stack in Javascript, which you alreadly know amazingly super duper well. For example, you could pull from a database, manipulate the data, write it to a file, host the file, then render it from the browser &mdash; all in js.

##The back end perspective

Node runs on a single thread, with asynchronous event looping, just like Javascript. This means Node should be written using callback functions. As an example:

```
var data = getData(parameter);
doSomething(data);
doSomethingElse();
```

This is synchronous (bad bad bad) code which might send a request to an API for some data and wait for a response. Then, once the data arrives, manipulate it in some way. The asynchronous version is:

```
getData(parameter, function(data){
	doSomething(data);
});
doSomethingElse();
```
The asynchronous (good good good) code sends the same request to the API. But then, instead of waiting for a response, it moves on to the next task (dosomethingelse()) and does its thing. Then, once the data arrives from the API, it gets manipulated. This process is known as the [event loop](http://en.wikipedia.org/wiki/Event_loop).

From a back end perspective, this means Node is great for programs which are [I/O bound](http://en.wikipedia.org/wiki/I/O_bound), i.e. the major thing slowing them down is waiting for input/output. Instead of waiting piecemeal for data to come in or go out, Node can send out lots of requests at once, dealing with them as they come finish.

Programs can also be [CPU bound](http://en.wikipedia.org/wiki/CPU_bound), or slowed down by stuff happening on the processor. The general wisdom is that Node's no good for CPU bound programs &mdash; while the CPU is doing its thing, Node is waiting around, not serving up data or doing anything else. Still, Node can be fine for some computational work. If things are too slow, it might be time to learn another language!

#Modules


##npm
package.json, install

##Your code as modules



#Whirlwind Tour of Useful Modules


##fs

##

##Express

##Cheerio
w/ request for scraping

##d3

##Shrinkwrap

##Uglifyjs and Uglifycss

sourcemap is cool

##Mocha

##http-server


Async and when to use sync
ex http://nodejs.org/api/fs.html

Require/ modules
http://docs.nodejitsu.com/articles/getting-started/what-is-require

node runs server side, unlike most JS (in browser, client side)



