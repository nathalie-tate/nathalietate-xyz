#!/usr/bin/perl

# Nathalie Tate
# Copyright (c) 2017, Some rights reserved.
# This Software may be freely modified and distributed under the terms of the 
# MIT Software License

# qutebrowser userscript to filter Searches on AO3 to remove content from
# undesireable authors. Due to limitations of qutebrowser and/or my knowledge of
# qutebrowser, instead of altering the HTML file currently being displayed,
# this script makes an offline copy, alters that, and then opens the local
# copy. It also changes links from relative to absolute, so links will resolve
# to the correct location on the AO3 servers, and not look for the files
# locally

# Default location of the blocklist is '~/.config/ao3Filter/blockList'

use strict;
use warnings;

#Variable Declarations
my @blockList;
my @html;
my $liCounter = 0;

sub trim
{
  my $tmp = shift;
  $tmp =~ s/^\s+|\s+$//g;  
  return $tmp;
}

#get list of authors
sub getBlockList
{
  open AUTHORLIST, "<","$ENV{'HOME'}/.config/ao3Filter/blockList" or die;

  @blockList = <AUTHORLIST>;
  close AUTHORLIST;
}

sub matchesAuthor
{
  my $author = shift;
  for (@blockList)
  {
    $author = trim $author;
    $_ = trim $_;
    if (($author) =~ /$_/)
    {
      return 1;
    }
  }
  return 0;
}

###MAIN 
getBlockList();

#read html into list

open QUTEHTMLREAD,"<","$ENV{'QUTE_HTML'}" or die;
@html = <QUTEHTMLREAD>;
close QUTEHTMLREAD;

for (0..@html-1)
{
  $liCounter = 1;
  if ($html[$_] =~ /^\s*\<li class="work blurb group"/)
  {
    if (matchesAuthor($html[$_ + 11]))
    {
      $html[$_] = "";
      my $line = $_ + 1;
      while($liCounter > 0)
      {
        if ($line >= @html)
        {
          $liCounter = 0;
        }
        elsif($html[$line] =~ /^\s*\<li.*\<\/li\>\s*$/)
        {}
        elsif($html[$line] =~ /\<li/)
        {
          $liCounter++;
        }
        elsif($html[$line] =~ /\<\/li\>/)
        {
          $liCounter--;
        }
        print $html[$line]."\n";
        $html[$line] = "";
        $line++;
      }
    }
  }
  # local links to global
  $html[$_] =~ s/href="/href="http:\/\/archiveofourown.org/g;
  $html[$_] =~ s/action="/action="http:\/\/archiveofourown.org/g;
}

open QUTEHTMLWRITE,">","/tmp/tmp.html" or die;
for(@html)
{
  print QUTEHTMLWRITE "$_\n";
}
close QUTEHTMLWRITE;
system("echo 'open /tmp/tmp.html' >> $ENV{QUTE_FIFO}");
