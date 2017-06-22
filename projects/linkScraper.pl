#!/usr/bin/perl

# linkScraper.pl
# Nathalie Tate
# nrt@nathalietate.xyz

# This code may be freely modified or distrubuted under the terms of the MIT
# License

# Prints all of the links on a webpage. Takes URL as commandline arg or 
# interactively.

# Note that this is NOT recursive. If "foo.com" contains one link to "bar.com"
# and "bar.com" contains one link to "foobar.com", Then "./linkScraper.pl
# foo.com" will print "bar.com"

# Also note that this only looks for HTML hyperlinks. JavaScript buttons or 
# URLs written in plain text will not be detected

use strict;
use warnings;

sub trim
{
  my $s = shift;
  $s =~ s/^\s+|\s+$//g;
  return $s
}

my $url;

if($ARGV[0])
{ 
  $url = $ARGV[0];
}
else
{
  $url = <>;
}

$url = trim($url);

my $urlBase;

$url =~ /^((https?:\/\/)?(www\.)?([^\.\s]+)(\.)([^\/]*))\/?.*$/;
$urlBase = $1;

my @links;

system("wget $url -qO .tmp");

open TMP,"<",".tmp" or die;
my @html = <TMP>;
close TMP;

for $_(@html)
{
  if($_ =~ /href\s*=\s*[\'\"](\S+)[\'\"]/)
  {
    my $match = $1;
    if($match =~ /^https?:\/\//)
    {
      print "$match\n";
    }
    elsif( $match =~ /^\/\/(.+)/)
    {
      print "$1\n";
    }
    elsif( !($url =~ /.*\/$/) && !($match =~ /^\/.*/))
    {
      print "$url/$match\n";
    }
    elsif(($url =~ /(.*\/$)/) && ($match =~ /^\/.*/))
    {
      print "$1/$match\n"; 
    }
    else
    {
      print "$urlBase$match\n";
    }
  }
}

system("rm .tmp");
