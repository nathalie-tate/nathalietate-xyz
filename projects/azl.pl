#!/usr/bin/perl
use strict;
use warnings;

my $cmd = "elinks http://search.azlyrics.com/search.php?q=";
for my $i (0..$#ARGV)
{
  $cmd = $cmd.$ARGV[$i].'+';
}

$cmd = substr $cmd, 0, -1;

system($cmd);
