#!/usr/bin/perl -SC

use warnings;
use strict;
use utf8;

use CGI qw/param header/;
use LWP::Simple;

printHeader();

if(param("lyrics"))
{
  printBody(fetch(param("lyrics")));
}

else
{
  printBody(form());
}


###############################################################################

sub printHeader
{
  print header().qq[ 
    <!DOCTYPE html>
    <html lang="en-US">
      <head>
        <meta charset="utf-8">
        <title>⚧ Home ⚢</title>
        <LINK href="/style.css" rel="stylesheet" type="text/css">
      </head>
  ];
}

sub printBody
{
  my $str = shift;

  print qq[
  <body>
    $str
  </body>
]}

###############################################################################

sub form
{
  qq[
    <form method=POST>
      <input name="lyrics" />
      <br>
      <input type="submit" value="Submit" />
    </form>
  ];
}

###############################################################################
sub fetch{
my $lyrics = shift;

die "zlyrics requires lyrics.\n" unless $lyrics;


my $html = get("https://search.azlyrics.com/search.php?q=$lyrics");
my @html;
my @newHtml;

if ($html =~/1\. <a href="(.+)" target="_blank">/)
{
  $html = get($1);
  @html = split /\n/, $html;

  for my $i (0..$#html)
  {
    if ($html[$i] =~ /<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->/)
    {
      push @newHtml, $html[$i] and ++$i until($html[$i] =~ /<\/div>/);
    }
  }
}
else
{
  die "Lyrics not found.\n";
}

my $output = join "\n", @newHtml;

$output =~ s/<i>//g;
$output =~ s/<\/i>//g;
$output =~ s/<b>//g;
$output =~ s/<\/b>//g;
$output =~ s/<br>//g;
$output =~ s/&quot;/"/g;
$output =~ s/<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->//;

$output;
}
