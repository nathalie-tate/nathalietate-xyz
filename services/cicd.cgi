#!/usr/bin/perl

use CGI qw/param/;

my @p = param;

open FH,"< /home/nathalie/tmp/log.tmp" or die;

print FH $_ for @p;
