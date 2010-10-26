TAP Integration Service - tapd
==============================
> TAPs provides a lightweight integration service for existing system management databases,  spreadsheets, and flat files.  `tapd` serves this metadata in a netural, JSON format for consumption by any service, but specifically [rundeck][1].

## Overview
`tapd` provides an http deamon to serve system metadata in JSON for consumption by [rundeck][1].  

The underlying architecture relies on (a variation of) CGI.  The decision to use CGI stems from its property as the lowest common denominator among web integration technoglogies.  There are language bindings for almost every programming language and it supports system shells extremely well.  Other technologies like FastCGI and SCGI are also candidates for future bindings.

Each tap will make the 

## How to Use
Using `tapd` to create new taps is extremely easy.  The most common usage is the `.options` tap.  These taps are CGI scripts that live in a predefined directory.  The default directory is `/var/run/taps/`.  Any number of directories can be created under this directory which will translate into a path of the URL.

For example: /var/run/taps/example/example1.options

    #!/bin/bash

    echo content-type: application/json
    echo

    echo [\"`uname -a`\"]

Is a typical CGI Script (not parsing any parameters).  The output produces:

    content-type: text/html

    ["Darwin noahc-mbp.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386"]

Suitable for parsing in rundeck or any other automation tool.

[1]: http://rundeck.org "Rundeck.org"

## .options JSON Format
The resulting CGI must produce a JSON Map or JSON List.

`
{
    "Key1": "Value1",
    "Key2": "Value2",
    ...
    "KeyN": "ValueN",
}
`

`
[
    "Value1", "Value2", ..., "ValueN",
]
`

## .resources JSON Format (proposed)
`
{
    "{uuid}": {
        "hostname": "value",
        "ipv4": "x.x.x.x",
        "ipv6": "2001::XXXX",
        "tags": ["a","b","c","d"],
    }
}
`