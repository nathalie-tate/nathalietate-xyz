#!/usr/bin/perl
# a script to automate blocking from blocklists

print "Enter the full path of your block list:\n";
my $path = <>;
$path = trim($path);

open FILE, "<",$path or die;

sub trim
{
	my $s = shift;
	$s =~ s/^\s+|\s+$//g;
	return $s
}

my @users= <FILE>;
close FILE;

for(@users)
{
	$_ = trim($_);
}

for (@users)
{
	system("t block $_");
}
