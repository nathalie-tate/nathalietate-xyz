#!/usr/bin/perl
use strict;
use warnings;

while(<>)
{
  chomp;
  system("perldoc -if $_") == 0 || system("perldoc -i $_");
}
