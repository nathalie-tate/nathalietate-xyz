#!/usr/bin/perl
use strict;
use warnings;
use CGI qw{url_param redirect};
use Digest::SHA qw(sha256_hex);
use URI::Escape qw(uri_unescape uri_escape);

#use CGI::Carp qw{fatalsToBrowser};

my $phash = q{cced8a7c9d48801908c360b2948c66a690c34b061eaa6815a1b29d673f8b97cf};
my @links = <"dropbox/*">;

my $pword = url_param('password');
my %paramHash;
foreach $_ (@links)
{
  $paramHash{$_} = url_param(uri_escape($_));
}

my $testHash = sha256_hex($pword.'XXX'); 

if ($testHash ne $phash)
{
  print redirect('https://nathalietate.xyz/dropbox');
}
else
{
  foreach $_ (keys %paramHash)
  {
    if ($paramHash{$_} == 1)
    {
      $_ = uri_unescape($_)
      qx{rm $_};
    }
  }

  print redirect('https://nathalietate.xyz/dropbox');
}
print redirect('https://nathalietate.xyz/dropbox');
