TAP Integration Service - tapd
==============================
> TAPs provides a lightweight integration service for existing system management databases,  spreadsheets, and flat files.  `tapd` serves node metadata in a netural, JSON format.

## Overview
`tapd` provides an http damon to serve node metadata in JSON for consumption JSON.  The underlying architecture relies on (a variation of) CGI as the API.  CGI represents the lowest common denominator and works with almost every programming language and shell.

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