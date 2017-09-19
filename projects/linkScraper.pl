#!/usr/bin/perl

# linkScraper.pl
# Nathalie Tate
# nrt@nathalietate.xyz

# This code may be freely modified or distrubuted under the terms of the MIT
# License

# Prints all of the links on a webpage. Takes URLs as commandline args or 
# from STDIN.

# Note that this is NOT recursive. If "foo.com" contains one link to "bar.com"
# and "bar.com" contains one link to "foobar.com", Then "./linkScraper.pl
# foo.com" will print "bar.com" Scripting it to be recursive should be a trivial
# task and is left as an exercise for the reader.

# Also note that this only looks for HTML hyperlinks. JavaScript buttons or 
# URLs written in plain text will not be detected

use strict;
use warnings;

use LWP::Simple;

use Getopt::Std;
our($opt_h, $opt_q);

sub trim
{
  my $s = shift;
  $s =~ s/^\s+|\s+$//g;
  return $s
}

@ARGV && getopts('hq');

$opt_h && die 
 "Prints all of the links on a webpage. Takes URLs as commandline args or from STDIN. Accepts input from redirects or pipes.
 USAGE:
    linkScraper [URLs] [options]       use specified URLs

 OPTIONS:
    -h                                 display this dialog
    -q                                 no prompt when reading from STDIN. Use when scripting or redirecting output.\n";


my @url;

if(@url = @ARGV){}
else
{
  if(!$opt_q)
  {
    print "Enter a list of URLs, separated by newlines. Press Ctrl-d when done.\n";
  }
  @url = <STDIN>;
}

foreach my $url_(@url)
{
  $url_ = trim($url_) or die "URL must not be empty\n";

  my $urlBase;

  $url_ =~ /^((https?:\/\/)?(www\.)?([^\.\s]+)(\.)([^\/]*))\/?.*$/;
  $urlBase = $1;

  my $html = get($url_) or die "Invalid URL\n(Make sure to include the protocol)\n";

  my @html = split /\n/, $html;

  for $_(@html)
  {
    if($_ =~ /href\s*=\s*[\'\"](\S+)[\'\"]/)
    {
      my $match = $1;
      if($match =~ /^https?:\/\//)
      {
        print "$match\n";
      }
      elsif($match =~ /(mailto\:.+)/)
      {
        print "$1\n";
      }
      elsif( $match =~ /^\/\/(.+)/)
      {
        print "$1\n";
      }
      elsif( !($url_ =~ /.*\/$/) && !($match =~ /^\/.*/))
      {
        print "$url_/$match\n";
      }
      elsif(($url_ =~ /(.*\/$)/) && ($match =~ /^\/.*/))
      {
        print "$1/$match\n"; 
      }
      else
      {
        print "$urlBase$match\n";
      }
    }
  }
}
