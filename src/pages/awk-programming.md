---
title: "The AWK Programming Reference"
permalink: /pages/awk
---

**[~](../../README.md)**

**[~/Pages](../pages.md)**

---

* TOC
{:toc}

---

[AWK Help](resources/AWK-Help)

[AWK Manpages](resources/AWK-Manpages)

# The Awk Reference

**NOTES**

AWK operates at the field level. It can easily access, transform, and format individual fields in a record. It also accepts regular expressions for pattern matching

It has C-type programming constructs, variables, and several built-it functions.

## General Syntax

AWK follows the general syntax of-
```
$ awk options `address {actions}` file
```
the syntax constituents are the same as in sed and also consists of two sections-an address and an action

the major difference is that the action is enclosed within curly braces

the address and action constitute what is known as an AWK program

these programs are mostly one line long, although they can span several lines as well

## AWK Filtering-Usage Example
```
$ awk `/director/ {print}` emplist
```

address section director selects the lines that are processed in the action section

if the address is missing, then the actions applies to all the lines in the file

if the action is missing, then the entire line will be printed

either the address or action is optional but both must be enclosed within a pair of single quotes

the print statement, when used without any field specifiers prints the entire line

printing is the default action of `awk`

### All equivalent
```
$ awk `/director/` emplist
$ awk `/director/{print}` emplist
$ awk `/director/{print $0}` emplist
```

## Variables

*all variables have a global scope in AWK*

```
$ awk -F "|" `$3=="director" && $6>700000
        count=count+1
        printf "%3d %-20s %-12s \n", count, $,...
` emplist
```

`-` <--left justify

## Logical Operators

## Relational Operators

## Number Processing

```
{print $1*$1}
```

## AWK Program on a File

## BEGIN and END Sections

## Arrays
`awk` handles one-dimensional arrays. No array declarations are necessary

an array is considered to be declared the moment it is used, it is automatically initialized to zero

## Built-in Variables

**NR** number of records read

**FS** input field separator

**OFS** output field separator

**NF** no. of fields in current record

**FILENAME** current input filename

**ARGC** no. of arguments

**ARGV** list of arguments

## Built-in Functions

`int(x)` return integer value of x

`sqrt(x)`

`length` length of complete record

`length(x)`

`substr(s1,s2,s3)` return string of length s3 with start position s2 in s1

`index(s1,s2)` return the position of string s2 in s1

`split(s,a)` split string s into array a

`system("cmd")` run a linux command

# Example Program for Practice

*WIP*
