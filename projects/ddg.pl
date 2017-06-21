#!/usr/bin/perl
use strict;
use warnings;

my $cmd = "elinks https://duckduckgo.com/html?q=";

for my $i (0..$#ARGV)
{
  $cmd = $cmd.$ARGV[$i].'+';
}

$cmd = substr $cmd, 0, -1;

system($cmd);
