This first learning lunch is on [node.js](http://nodejs.org/), and is for a relatively small audience of graphics-folks-who-code (the data visualization team at the Post). As such, it's geared towards front end designers/developers who are comfortable with Javascript.

#What is Node?

Node.js is a platform built for fast network applications. It runs on the [V8 virtual machine](http://code.google.com/p/v8/), which is the same VM which compiles javascript in Chrome. 

#Why Use Node?

##The front end perspective

Much of the discussions around the merits of Node assume you're comparing it to other back end programming languages/platforms/frameworks. I discuss these merits below, but a lot of them might sound familiar from Javascript &mdash; using function callbacks to run code asynchronously, for example. But Node has advantages from a front end viewpoint too:

* Node is run on the server (javascript is run in-browswer on the client side). This not only means you can do beefy javascript or javascript-esque things on the server ([prerendering d3 server side, for example](http://mango-is.com/blog/engineering/pre-render-d3-js-charts-at-server-side.html)), but you can also do things which are impossible from the client, like modifying files, accessing databases, etc.

* While native node (i.e. the initial install) has plenty of functionality, most node applications implement **modules**. Modules (like Python packages or Ruby gems, and sort of like Javascript libraries) are written to accomplish all sorts of specific tasks. Lots more on modules below.

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

From a back end perspective, this means Node is great for programs which are [I/O bound](http://en.wikipedia.org/wiki/I/O_bound), i.e. the major thing slowing them down is waiting for input/output. Instead of waiting piecemeal for data to come in or go out, Node can send out lots of requests at once, dealing with them as they finish.

Programs can also be [CPU bound](http://en.wikipedia.org/wiki/CPU_bound), or slowed down by stuff happening on the processor. The general wisdom is that Node's no good for CPU bound programs &mdash; while the CPU is doing its thing, Node is waiting around, not serving up data or doing anything else. Still, Node can be fine for some computational work. If things are too slow, it might be time to learn another language! Yay learning!

#Modules

To a large degree, the power of Node lies in its modules. You'll install modules using Node Packaged Modules, or [npm](https://www.npmjs.org/).

##npm

Let's say you're writing a program in node which requires two modules, bbq and buffalo. Once you've got npm installed, you could install the most recent versions of these two modules by running (from the command line):
```
$ npm install bbq
$ npm install buffalo
```
But npm is way cooler than that. Within your node app, you should have a file named `package.json`, that might look like this:
```
{
  "name": "myproject",
  "version": "0.0.1",
  "dependencies": {
  	"bbq":"~0.1.2",
  	"buffalo":"~2.3.1"
  }
}
```
Now, from within your app's directory, run 'npm install'. BOOM! You'll install all dependency modules at once. Not only that, but bbq and buffalo each have their *own* package.json files, and running `npm install` or `npm install bbq` will install everything inside *those* package.json's.

To use these modules in your app, include the code
```
var bbq = require('bbq');
var buffalo = require('buffalo');
```

###A note on versioning
Node app's are often made up of lots of moving parts, which are constantly getting updated and changed. Your app might work today, but break tomorrow when a module updates. To help deal with this problem, you should specify versions for each module. A version number like 2.3.1 indicates major version.minor version.patch version, the definitions of which are outlined by semantic versioning, or [semver](http://semver.org/) standards. It's pretty safe to assume that new patches won't break your app (in fact they might make it better/faster (.../harder/stronger)). So specifying a version like ~2.3.1 means use major version 2 and minor version 3, but any patches which come out (2.3.1, 2.3.3, etc.) This is the same as writing 2.3.X, although it's a bit more informative to use a ~ and specify exactly which patch was stable at build time. It's also possible to freeze every version in place (not just of your dependencies, but of the depencies of your dependcies too) using npm [shrinkwrap](http://blog.nodejs.org/2012/02/27/managing-node-js-dependencies-with-shrinkwrap/). You can read more on clickthrough, but basically it's a nice way to lock down stable versions of an app, maybe especially useful if you've got some wonky or experimental dependencies.

##Your code as modules

You can treat your own code as a module. Say you've written some code in `utilities.js`. If you'd like to access it from another node script, `app.js`. In `app.js` include:
```
var utilities = require('path/to/utilities')
```
(note no file extension)
and in `utilities.js` you can either export specific functions/variables like so:

```
exports.myVariable = "value";
exports.myFunction = function(){
	doThings();
}
```
or export the module as an object of function like so:
```
module.exports = function(){
	startMyApp();
}
```

#Whirlwind Tour of Useful Modules

##Uglifyjs and Uglifycss

[Uglifyjs](https://www.npmjs.org/package/uglify-js) is a great module which is a js minifier and a lot more. It can optimize js code with various flags (remove unreachable code, delete all `console.*` functions, etc.), plus you can export a source map which allows for easy mapping between minified js and readable source js from the browser's dev console.

There's also an [uglifycss](https://www.npmjs.org/package/uglifycss) which is just a minimizer, more or less.

(Note: you don't need to be writing full node apps to use many of these modules. Something like uglifyjs is standalone and can be run from the command line, once installed with npm).

##Cheerio

[Cheerio](https://www.npmjs.org/package/cheerio) is the most popular scraping module in node. Basically, cheerio nicely repackages some jQuery functions for elegant parsing of the html DOM tree. That's mostly what web-scraping is, picking out html elements by css selector, parent/child, etc.

To scrape, you probably also want to use the [request](https://www.npmjs.org/package/request) module for intially pulling down the webpage.

##d3

Once you install [d3](https://www.npmjs.org/package/d3) with npm and include in in your node script with `require('d3')`, you can just write d3 like always. That easy. Same goes for [raphael](https://www.npmjs.org/package/raphael) and most javascript libraries.

##fs

Filesystem, or [fs](http://nodejs.org/api/fs.html) comes standard with node installation. It's your basic file processing module, letting you not only read/write but do various command-line-y things like move, delete, chmod, etc.

##http-server
[http-server](https://www.npmjs.org/package/http-server) is a great, simple way to launch a crazy simple server (at localhost:8080 by default). You can install the module globally with
```
$ npm install http-server -g
```
Then launch with `$ http-server` to host to current directory (you can also specify a path to another directory with `$ http-server path/to/dir`)

##Express

[Express](http://expressjs.com/) is a web application framework like Rails in Ruby or Django in Python. There's a whole lot that could be said about it, but basically it provides a nice structure for building an app, and having all the moving pieces talking to each other correctly. To get started, you could first install the express-generator globally:
```
$ npm install -g express-generator
```
Then, from any directory, if you just run
```
$ express
```
Express will create a basic directory structure for you like so:

![alt text](https://raw.github.com/bchartoff/learninglunches/master/node/express.png "basic express app file structure")

img
So, for example, `app.js` might set up your server and connect to a database, then define a few routes like:
```
http://myurl.com/graphic/graphicID
```
which GETs a graphic from a database, and
```
http://myurl.com/update/graphicID/newdata
```
which POSTs new data to a given graphic.

The methods which spell out exactly how to grab and update these graphics would live in the `routes` folder, while the [jade](https://www.npmjs.org/package/jade) template (default with express, it's basically html templating &mdash; you could use straight up html too) to display the graphics would live in `views`, styled by `public/stylesheets/style.css`.

There's a lot more of cool things you can do in express, and there are lot of other Node frameworks ([sails](http://sailsjs.org/#!), for example). 

#Learn More

Node has only been around for about five years, and is still an extremely active and ever-changing community. A lot of node-specific sites and blogs are focussed more on new developments and exciting updates, and less on learning the basics. That being said, there are tons of topic-specific tutorials and forum posts all over the web. Often, if you have a problem, you might also google "npm my problem" &mdash; chances are good there's a module out there to help you. Be careful though, sometimes the solution is simpler than you think, and layering module on top of module can get messy.

You can also buy a textbook (or borrow one from a coworker), or ask me questions in person or on the internet. Keep on learning.



