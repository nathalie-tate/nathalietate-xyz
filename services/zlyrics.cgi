#!/usr/bin/perl -CS

use warnings;
use strict;
use utf8;

use CGI qw/param header/;
use LWP::Simple;

if(param("lyrics"))
{
  my ($body, $title)  = fetch(param("lyrics"));

  printHeader($title); 
  printBody($body);
}

else
{
  printHeader(); 
  printBody(form());
}


###############################################################################

sub printHeader
{
  my $title = shift;

  print header(-charset=>'utf8').qq[ 
    <!DOCTYPE html>
    <html lang="en-US">
      <head>
        <meta charset="utf-8">
        <title>⚧ ]. ($title//"zlyrics") .qq[ ⚢</title>
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

    <hr />
    <a href="https://nathalietate.xyz/services/zlyrics.cgi">Back</a>
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

  my $title;

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
      elsif ($html[$i] =~ /<title>(.+)<\/title>/)
      {
        $title = $1;
      }
    }
  }
  else
  {
    return "Lyrics not found";
  }

  my $output = join "\n", @newHtml;

  $output =~ s/<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->//;

  ($output, $title);
} 
