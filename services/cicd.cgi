#!/usr/bin/perl

use strict;
use warnings;

use CGI::Carp qw/fatalsToBrowser/;

use CGI qw/Vars param/;
use JSON qw/decode_json/;

my %p = Vars(); 
my $dj = decode_json($p{POSTDATA});

$dj = $dj->{repository}->{name};

if($dj eq 'herculeze')
{ 
  print qq[Content-type:text-html\n\n];

  system("git -C /var/www/herculeze/ pull");
  print "Success";
}
