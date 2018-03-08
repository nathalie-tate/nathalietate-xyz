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
  printBody($body, 1, $title);
}

else
{
  printHeader(); 
  printBody(form(), 0);
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
  my $code = shift; 
  my $title = shift;

  my $song;
  my $artist;

  if ($title)
  {
    if($title =~ /(.*) Lyrics - (.*)/)
    {
      $artist = $1;
      $song = $2;
    }
  }

  $song = $song 
    ? qq[<h1>$song</h1>]
    : "";

  $artist = $artist
    ? qq[<h2>$song</h2>]
    : "";

  my $code = $code 
    ?  q[<hr /> <a href="https://nathalietate.xyz/services/zlyrics.cgi">Back</a>] 
    : "";

  print qq[
  <body>
    $artist
    $song
    $str
    $code
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
