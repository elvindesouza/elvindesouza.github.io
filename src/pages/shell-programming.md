---
title: "Shell Scripting - A Quick Reference"
permalink: /pages/sh
---

**[~](../../README.md)**

**[~/Pages](../pages.md)**

---

* TOC
{:toc}

---

# Shell Scripting - A Quick Reference

## Shebang

The `#!` syntax is used in scripts to indicate an interpreter for execution under UNIX / Linux operating systems. The directive must be the first line in the Linux shell script and must start with shebang #!. 

```
#!/usr/bin/env sh
#!/usr/bin/env bash
```

## Comments

`#`

## Execute Your Script
```
chmod +x <file>.sh
./<file>.sh
```

## Variables

*no spaces around `=`*

**export** vars to have them inherited

surround with `""` to prevent word splitting

The shell does not know where the variable ends and the rest starts. use `${}`

wildcards and escaping-

```
echo \*
echo * [will expand * to files in directory]
```

`" $ \` \ ` are interpreted by the shell even in quotes

 The backtick (`)is also often associated with external commands
 The backtick is used to indicate that the enclosed text is to be executed as a command


```
echo "A quote is \", backslash is \\, backtick is \`."
echo "A few spaces are    and dollar is \$. \$X is ${X}."
```

```
echo "$0" #is the basename
# $1 .. $9 are the first 9 additional parameters
echo "$@" # is all parameters from $1...
echo "$*" # same, but doesnt preserve whitespace
echo "$#" # no. of params
echo "$?" #exit value of the last run command
echo "$$" # PID of curr shell
echo "$!" # PID of last run bg proc
```

### shift
```
while [[ "$#" -gt "0" ]]; do
    echo "\$1 is $1"
    shift
done
```
## Conditionals

### test

[RTFM!](./Test-Reference)

*`[` is a symbolic link to `test`

*'[' is actually a program, just like ls and other programs, so it must be surrounded by spaces*

*a single "=" should be used for strings, or "-eq" for integers.*

*-lt, -gt, -le and -ge comparisons are only designed for integers, and do not work on strings. The string comparisons, such as !=*

*be careful with the spaces*

#### test usage
```
if [ $foo = "bar" ]; then
    echo a
elif [ ... ]; then
    echo c
else
    echo b
fi

```

#### Integer `test`
```
echo $X | grep "[^0-9]" >/dev/null 2>&1
if [ "$?" -eq "0" ]; then
    # If the grep found something other than 0-9
    # then it's not an integer.
    # $? is exit code of last run prog
    # sends output&errs to /dev/null
fi
```

### Alternative conditionals usage
*not very readable*
```
a=1
[ $a -ne 0 ] && echo "a isn't zero" || echo "a is zero"
```


## Looping Constructs

### for
```
for i in 1 2 3 4 5; do
    echo "Looping ... number $i"
done

for i in 123 4 5 *; do
    echo "$i"
done
```

### while

```

INPUT_STRING=hello
while [ "$INPUT_STRING" != "bye" ]; do
    echo "Please type something in (bye to quit)"
    read -r INPUT_STRING
    echo "You typed: $INPUT_STRING"
done

# colon always evals True
while :; do
    echo "Please type something in (^C to quit)"
    read -r INPUT_STRING
    echo "You typed: $INPUT_STRING"
done

```

## Case

```
while read -r input_text; do
    case $input_text in
    hello) echo English ;;
    *)
        echo Unknown Language: "$input_text"
        ;;
    esac
done <z
```

## External Commands

```
`cmd`
$(cmd)
```

## Functions

```

func()
{
    a=1
    b=2
    c=`expr $a + $b`
    c=$(a+b)
    echo "$c"
}

func 1 argu * b

# exit to end shell script
# return to end func, and return val
# no variable scope
```


# Basic Shellscripting Examples

*using bash*

```

#Automatically do an ls after each cd
 cd ()
 {
    if [ -n "$1" ]; then
        builtin cd "$@" && ls
    else
        builtin cd ~ && ls
    fi
 }


# using what we learned with test, and shell peculiarities
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

```


