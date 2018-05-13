#!/usr/bin/perl

use CGI qw/param/;

my @p = param;

open FH,"> /tmp/log.tmp" or die;

print FH $_ for @p;

print <<END
Content-type:text-html



Success

END
