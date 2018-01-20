#!/usr/bin/perl
use strict;
use warnings;

my $cmd = "elinks https://duckduckgo.com/html?q=";

foreach (@ARGV)
{
  $cmd .= "$_+";
}

$cmd = substr $cmd, 0, -1;

system($cmd);
