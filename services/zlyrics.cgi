#!/usr/bin/perl

use warnings;
use strict;

use CGI qw/param header/;
use LWP::Simple;

print header();

if(param("lyrics"))
{
  fetch(param("lyrics"));
}

else
{
  printForm();
}


###############################################################################

sub printForm
{
  print qq[
    <form method=POST>
      <input name="lyrics" />
      <br>
      <input type="submit" value="Submit" />
    </form>
  ];
}

###############################################################################
sub fetch{
my @lyrics = @_;

if(@lyrics = @ARGV){}
else
{
  die "zlyrics requires lyrics.\n";
}

my $lyrics = join "+",@lyrics;

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

print $output;
}
