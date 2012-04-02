# HaltPy: A tool to determine if an arbitrary program is terminable

## Description

HaltPy is a simple, RESTful service to determine if any arbitrary program will
eventually terminate. Feed it the file name of any program's bootstrap source
and HaltPy responds with the answer to whether or not the program terminates. 

So easy, a Computer Scientist can do it.

## Why Use HaltPy

1. It's DRY. Not a single line of code in HaltPy is a duplicate. Guaranteed.

2. The answer as to whether an arbitrary program terminates is an extremely 
valuable one. The continued existence of Sarah Connor will be crucial in the
coming war against Skynet. Be prepared, with HaltPy.

3. Almost inexplicably, no one else has implemented this yet. Cutting edge.

## Usage

1. Download `halt.py`
    
2. Feed HaltPy the file name of some computer program's bootstrap:
    
    `$ ./halt.py main.c`
    
3. That's it. You've got your answer

## Kudos

HaltPy relies on <a href="http://docs.python-requests.org/en/latest/">Requests</a>
and <a href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a> 
to work its magic.

HaltPy also uses <a href="http://thecatapi.com/">The Cat API</a>. On the back 
end, most of the leg work is actually performed by a dynamically allocated cat
pool. Output is rendered by <a href="http://www.glassgiant.com/ascii/">Glass 
Giant</a>, in order to convert the machine language (translated into Sanskrit,
then XSLT, and finally ASCII art) into a human-readable form.
                   
## License

Copyright (c) April 1st 2012 Joshua Essex

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

