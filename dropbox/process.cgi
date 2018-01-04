#!/usr/bin/perl
use strict;
use warnings;
use CGI qw{param redirect};
use Digest::SHA qw(sha256_hex);
#use CGI::Carp qw{fatalsToBrowser};

my $q = new CGI;
print CGI::header();
print $q->redirect('https://nathalietate.xyz/dropbox');

my $phash = q{cced8a7c9d48801908c360b2948c66a690c34b061eaa6815a1b29d673f8b97cf};
my @links = <"dropbox/*">;

my $pword = param('password');
my %paramHash;
foreach $_ (@links)
{
  $paramHash{$_} = param($_);
}

my $testHash = sha256_hex($pword.'XXX'); 

if ($testHash ne $phash)
{
  #print $q->redirect('https://nathalietate.xyz/dropbox');
}
else
{
  foreach $_ (keys %paramHash)
  {
    if ($paramHash{$_} == 1)
    {
      qx{rm $_};
    }
  }

  #print $q->redirect('https://nathalietate.xyz/dropbox');
}
print CGI::header();
print $q->redirect('https://nathalietate.xyz/dropbox');
